# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import ast

from graphql import Source, parse


class GraphQLChecker(object):
    """
    flake8 plugin that lints your graphql strings
    """
    name = 'flake8-graphql'
    version = '0.1.0'

    def __init__(self, tree, *args, **kwargs):
        self.tree = tree

    def run(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Call) and hasattr(node.func, 'id') and node.func.id == 'gql':
                if isinstance(node.args[0], ast.Str):
                    try:
                        query = node.args[0].s
                        Source(query)
                        parse(query)
                    except Exception as e:
                        yield (node.lineno, node.col_offset, 'GQL100: ' + str(e), type(self))
