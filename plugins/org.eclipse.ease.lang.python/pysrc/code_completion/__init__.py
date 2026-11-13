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
Code completion library.

Performs static as well as dynamic checks.
If possible relies on :mod:`ast` module for parsing the input.

Long running calculations are performed asynchronously and cached
to increase performance. Initial cache filling might take some time
though.

Tries to also get documentation for found proposals.

:author: Martin Kloesch <martin.kloesch@gmail.com>
'''
from code_completion.completion import parse
from code_completion.completion import CompletionProposal
from code_completion.documentation import Documentation

# Try to cache available modules asap
from code_completion.utility import _module_fetcher_thread
_module_fetcher_thread.start()

__all__ = ['parse', 'CompletionProposal', 'Documentation']
