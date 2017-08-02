# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import ast


class GraphQLChecker(object):
    """
    flake8 plugin that lints your graphql strings
    """
    name = 'flake8-graphql'
    version = '0.1.0'

    def __init__(self, tree, *args, **kwargs):
        self.tree = tree

    messages = {
        'GQL100': 'Cannot parse graphql syntax',
    }

    def run(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Str):
                yield (node.lineno, node.col_offset, "Found a string: " + node.s, type(self))
