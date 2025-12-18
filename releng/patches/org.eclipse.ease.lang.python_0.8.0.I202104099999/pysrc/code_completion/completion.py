#################################################################################
# Copyright (c) 2017 Martin Kloesch and others.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# https://www.eclipse.org/legal/epl-2.0/
#
# Contributors:
#     Martin Kloesch - initial API and implementation
#################################################################################
'''
Source code parsers and completion providers.

Performs static as well as dynamic checks.
If possible relies on :mod:`ast` module for parsing the input.

This file concentrates on parsing the input and finding matches.
For utility methods, module lookups, etc see
:mod:`code_completion.utility`

:author: Martin Kloesch <martin.kloesch@gmail.com>
'''
import ast
import collections
import re
import types

from code_completion import utility
from code_completion import documentation


def _strip_brackets(src, opendelim='(', closedelim=')'):
    '''
    Removes code outside of current bracket.

    :param src:         Source code to be stripped.
    :type src:          str
    :param opendelim:   Opening bracket character.
    :type opendelim:    chr
    :param closedelim:  Closing bracket character.
    :type closedelim:   chr
    :returns:           Stripped code.
    :rtype:             str
    :raises SyntaxError:    If more closing than opening delimiters.
    '''
    brackets_stack = []
    try:
        for i in range(len(src)):
            if src[i] == opendelim:
                brackets_stack.append(i)
            elif src[i] == closedelim:
                brackets_stack.pop()
        if brackets_stack:
            src = src[brackets_stack[-1]+1:]
    except IndexError:
        raise SyntaxError(
            'Too many closing brackets ({}) in input.'.format(closedelim)
        )

    return src


def _strip_input(src):
    '''
    Strips all unnecessary code from the given input
    and returns the resulting code.

    :param src: Code to be stripped.
    :type src:  str
    :returns:   Stripped code.
    :rtype:     tuple<str, bool>
    :raises SyntaxError:    If invalid code given.
    '''
    stripped = len(src) > len(src.rstrip())
    src = src.rstrip()

    # Remove code outside current bracket
    src = _strip_brackets(src, '(', ')')
    src = _strip_brackets(src, '[', ']')
    src = _strip_brackets(src, '{', '}')

    return src, stripped


class CompletionProposal:
    '''
    Data-storage class for a completion proposal.

    Stores information about the proposed value as string
    and if available documentation for said proposal.
    '''
    #: String to be displayed for completion proposal.
    #: :type: str
    name = None
    
    #: String needed to complete input for this proposal.
    #: :type: str
    completion = None
    
    #: Documentation for proposal.
    #: :type: :class:`documentation.Documentation`
    documentation = None
    
    def __init__(self, name, completion=None, documentation=None):
        '''
        Constructor only stores parameters to members.

        :param proposal:        Code completion proposal.
        :type proposal:         str
        :param completion:      String to be appended.
        :type completion:       str
        :param documentation:   Documentation for proposal.
        :type documentation:    
            :class:`Documentation<documentation.Documentation`
        '''
        self.name = name
        self.completion = completion
        self.documentation = documentation

    def __hash__(self):
        return hash(self.name)


def parse(src, dot=False):
    '''
    Parses the given source code using :mod:`ast` module
    and yields all potential autocompletion matches.

    If syntax errors occured code is split and recursively parsed.

    :param src: Input to be parsed for autocompletion.
    :type src:  str
    :param dot: Flag set if original input ended with dot.
                Used for recursive implementation, do not use.
    :type dot:  bool
    :yields:    Autocompletion matches.
    :ytype:     :class:`CompletionProposal`
    '''
    # Special care has to be taken about input ending with '.'
    try:
        src, stripped = _strip_input(src)
    except SyntaxError:
        return

    # Check if code ends with '.'
    if src.endswith('.'):
        dot = True
        src = src[:-1]
    else:
        dot = dot or False

    # Parse code to abstract syntax tree
    try:
        module = ast.parse(src)
        body = module.body[-1]

        # Dispatch parsing to more suitable method
        for completion in parser_lookup[body.__class__](body, dot):
            yield completion

    except SyntaxError:
        # Try possible incomplete statement scenarios
        _only_from = re.search(
            r'^\s*from\s+(?P<name>[a-zA-Z0-9_\.]*)$',
            src,
            re.MULTILINE
        )
        _import_from = re.search(
            r'^\s*from\s+(?P<module>[a-zA-Z0-9_\.]+)\s+import$',
            src,
            re.MULTILINE
        )

        # Check if empty import (no module name given)
        if re.search(r'^\s*import$', src, re.MULTILINE):
            for completion in utility.modules():
                yield CompletionProposal(completion, completion)

        # Check if start of import from statement (from foo)
        elif _only_from:
            if dot:
                completions = utility.inspect_import(
                    _only_from.group('name'),
                    '',
                    True
                )
                for completion in completions:
                    yield CompletionProposal(completion, completion)
            else:
                submodules = _only_from.group('name').split('.')
                if len(submodules) > 1:
                    completions = utility.inspect_import(
                        '.'.join(submodules[:-1]),
                        submodules[-1],
                        True
                    )
                    for completion in completions:
                        yield CompletionProposal(
                            completion, 
                            completion[len(submodules[-1]):]
                        )
                else:
                    for completion in _import(submodules[0], True):
                        yield CompletionProposal(
                            completion, 
                            completion[len(submodules[0]):]
                        )

        # Check if unfinished import from statement (from foo import )
        elif _import_from:
            module = _import_from.group('module')
            completions = utility.inspect_import(module)
            for completion in completions:
                yield CompletionProposal(
                    completion, 
                    completion[len(module):]
                )

        else:
            # Recursively check last word in input
            if not stripped:
                subset = re.split('\s+', src)[-1]
                if subset != src:
                    for completion in parse(subset, dot):
                        yield completion
            else:
                for completion in _list_globals():
                    yield completion

    except IndexError:
        # Return list of all globals
        for completion in _list_globals():
            yield completion


def _import_wrapper(imp, dot=False):
    '''
    Wrapper for :class:`ast.Import` statements parsing information
    and dispatching data to different functions.

    :param imp: Import statement to be parsed.
    :type imp:  :class:`ast.Import`
    :yields:    Completion based on import statement.
    :ytype:     :class:`CompletionProposal`
    '''
    modulename = imp.names[-1].name
    submodules = modulename.split('.')

    # Simple import, use root modules
    if len(submodules) == 1 and not dot:
        for completion in _import(submodules[0]):
            yield completion
    else:
        if dot:
            completions = utility.inspect_import(
                '.'.join(submodules),
                '',
                True
            )
            for completion in completions:
                yield CompletionProposal(
                    completion, 
                    completion
                )
        else:
            completions = utility.inspect_import(
                '.'.join(submodules[:-1]),
                submodules[-1],
                True
            )
            for completion in completions:
                yield CompletionProposal(
                    completion, 
                    completion[len(submodules[-1]):]
                )


def _import(pattern):
    '''
    Autocompletion parser for 'import foo' inputs.

    :param pattern: Start of module names
    :type pattern:  str
    :yields:    Autocompletion matches.
    :ytype:     :class:`CompletionProposal`
    '''
    # Only root module given (import foo)
    for completion in utility.modules(pattern):
        yield CompletionProposal(
            completion, 
            completion[len(pattern):]
        )


def _import_from(imp, dot):
    '''
    Autocompletion parser for 'from foo import bar' inputs.

    :param imp: ImportFrom object to be parsed.
    :type imp:  :class:`ast.ImportFrom`
    :param dot: Flag to signalize if input ended with '.'
    :type dot:  bool
    :yields:    Autocompletion matches.
    :ytype:     :class:`CompletionProposal`
    '''
    return [
        CompletionProposal(p, p[len(imp.names[0].name):])
        for p in utility.inspect_import(
            imp.module,
            imp.names[0].name
        )
    ]


class ExpressionchainItem(
                            collections.namedtuple(
                                'ExpressionchainItem',
                                ('name', 'call')
                            )
                          ):
    '''
    Data storage class for an item in an expression chain.

    Stores information about the name as well if item was called.

    Example:
        Foo().bar.baz().foobar
        ->
        (Foo, True),
        (bar, False),
        (baz, True),
        (foobar, False)
    '''


def _expression(expr, dot):
    '''
    Autocompletion parser for Python expressions.

    :param expr: Expression object to be parsed.
    :type expr:  :class:`ast.Expression`
    :param dot:  Flag to signalize if input ended with '.'
    :type dot:   bool
    :yields:     Autocompletion matches.
    :ytype:      :class:`CompletionProposal`
    '''
    # Attribute chain for expression (foo.bar.baz -> ['foo', 'bar', 'baz'])
    attribute_chain = []

    # Iterate over ast chain
    prev = None
    while expr:
        # Start of expression chain
        if isinstance(expr, ast.Expr):
            expr = expr.value

        # Only use right side of operations
        elif isinstance(expr, ast.BinOp):
            prev = expr
            expr = expr.right

        # Use attribute name
        elif isinstance(expr, ast.Attribute):
            attribute_chain.append(
                ExpressionchainItem(
                    expr.attr,
                    isinstance(prev, ast.Call)
                )
            )
            prev = expr
            expr = expr.value

        # Cache call information for later use
        elif isinstance(expr, ast.Call):
            prev = expr
            expr = expr.func

        # Special attribute case for first element
        elif isinstance(expr, ast.Name):
            attribute_chain.append(
                ExpressionchainItem(
                    expr.id,
                    isinstance(prev, ast.Call)
                )
            )
            prev = expr
            expr = None

        # Should not occur
        else:
            raise Exception(
                'Invalid expression type {}'.format(expr.__class__)
            )

    # Need attribute chain in correct order
    attribute_chain = list(reversed(attribute_chain))

    # Special care for input ending with '.'
    if dot:
        namespace_lookup = attribute_chain
        to_match = ''
    else:
        # Special care for chains ending in calls
        if attribute_chain[-1].call:
            return

        namespace_lookup = attribute_chain[:-1]
        to_match = attribute_chain[-1].name

    # Get last namespace in attribute chain
    namespace = utility.full_globals()

    for item in namespace_lookup:
        # Get value with given name
        value = namespace.get(item.name)
        if not value:
            return

        # Try to get return type for value
        if item.call:
            if isinstance(value, types.FunctionType):
                # Use annotations
                if hasattr(value, '__annotations__') and \
                   'return' in value.__annotations__:
                        namespace = vars(value.__annotations__.get('return'))
                        continue
                # Do not guess return type
                else:
                    return

        # HACK: Problem with py4j JavaObjects and some builtin types
        # if hasattr(value, '__dict__'):
        #     namespace = vars(value)
        namespace = {k: getattr(value, k) for k in dir(value)}

    # Get all matches
    for k, v in namespace.items():
        if k.startswith(to_match):
            yield(CompletionProposal(
                k,
                k[len(to_match):], 
                documentation.Documentation.from_object(v)
            ))


def _assing(assign, dot):
    '''
    Autocompletion parser for Python assign operations.

    Takes left-hand part of assignment and feeds it to
    :func:`_expression`

    :param assign:  Assign object to be parsed.
    :type expr:     :class:`ast.Assign`
    :param dot:     Flag to signalize if input ended with '.'
    :type dot:      bool
    :yields:        Autocompletion matches.
    :ytype:         :class:`CompletionProposal`
    '''
    for completion in _expression(assign.value, dot):
        yield(completion)


def _list_globals(*args):
    '''
    Yields list of all global variables.

    :yields:     Autocompletion matches.
    :ytype:      :class:`CompletionProposal`
    '''
    for k, v in utility.full_globals().items():
        if not k.startswith('__'):
            yield(CompletionProposal(
                k,
                k, 
                documentation.Documentation.from_object(v)
            ))


#: Command pattern for different parsers
parser_lookup = collections.defaultdict(
    lambda: _list_globals, {
        ast.Import: _import_wrapper,
        ast.ImportFrom: _import_from,
        ast.Expr: _expression,
        ast.Assign: _assing
    }
)


__all__ = ['CompletionProposal', 'parse']
