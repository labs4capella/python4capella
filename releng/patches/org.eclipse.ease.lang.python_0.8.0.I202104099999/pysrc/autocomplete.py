'''
Copyright (c) 2017 Martin Kloesch and others.
All rights reserved. This program and the accompanying materials
are made available under the terms of the Eclipse Public License v2.0
which accompanies this distribution, and is available at
https://www.eclipse.org/legal/epl-2.0/

Contributors:
 * Martin Kloesch - initial API and implementation
'''
try:
    # Try to use jedi library for best results
    import jedi as _pyease_jedi
except ImportError:
    _pyease_jedi = None

import __main__

try:
    # Additional analysis using EASE code_completion library
    from code_completion.completion import parse as _pyease_cc
except ImportError:
    # Fallback to no-op generator
    def _pyease_cc(*args, **kwargs):
        return
        yield

try:
    # If possible try to use docutils to generate better docstrings
    from docutils.core import publish_string as _pyease_docutils_ps

    def _pyease_html_documentation(docstring):
        try:
            return _pyease_docutils_ps(docstring, writer_name="html", settings_overrides={'report_level':'quiet'}).decode("utf-8")
        except Exception:
            return docstring

except ImportError:
    # Fallback to no-op function
    def _pyease_html_documentation(docstring):
        return docstring


class _pyease_CompletionProvider:
    '''
    EASE ICompletionProvider wrapping to different code completion
    libraries.

    Currently wraps to:
        * jedi (for longer inputs)
        * code_completion (EASE)
    '''

    def getProposals(self, context):
        # Java class because of problem with python list serialization
        java_completions = java.util.ArrayList()
        
        source = context.getOriginalCode()
        completions = []
    
        # code_completion library for simple default proposals
        completions.extend(_pyease_cc(source))
                
        # Jedi library for best proposals (only if available)
        if _pyease_jedi:
            # jedi.Script for static checks
            script = _pyease_jedi.Script(source)
            completions.extend(script.completions())
    
            # jedi.Interpreter for dynamic checks
            interpreter = _pyease_jedi.Interpreter(source, [__main__.__dict__])
            completions.extend(interpreter.completions())
        
        # Remove duplicates
        completions_no_duplicates = {}
        for completion in completions:
            to_check = completion
            if hasattr(completion, 'name'):
                to_check = completion.name
            if to_check not in completions_no_duplicates:
                completions_no_duplicates[to_check] = completion
    
        # Parse completions to Java suitable format
        for comp in completions_no_duplicates.values():
            # Safety fallback, should always use name
            proposal = comp.name if hasattr(comp, 'name') else comp

            # Ignore internals
            if not proposal.startswith('_pyease'):
                # code_completion library object
                if hasattr(comp, 'documentation') and comp.documentation:
                    help_resolver = org.eclipse.ease.lang.python.ui.completion.PythonHelpResolver(comp.documentation.plain, comp.documentation.html)
        
                # jedi object
                elif hasattr(comp, 'doc') and comp.doc:
                    help_resolver = org.eclipse.ease.lang.python.ui.completion.PythonHelpResolver(
                        comp.doc,
                        _pyease_html_documentation(comp.doc)
                    )
    
                # No documentation
                else:
                    help_resolver = None
    
                java_completions.add(
                    org.eclipse.ease.ui.completion.ScriptCompletionProposal(
                        context,
                        proposal,
                        proposal,
                        None,
                        1,
                        help_resolver
                    )
                )

        return java_completions

    def isActive(self, context):
        '''
        Always active.
        '''
        return True

    class Java:
        implements = ['org.eclipse.ease.ui.completion.ICompletionProvider']


# Set up connection between eclipse and python
_pyease_jedi_completion_provider = _pyease_CompletionProvider()
_pyease_jedi_completion_provider_wrapper.setPythonPprovider(
    _pyease_jedi_completion_provider)
