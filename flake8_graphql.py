# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import ast

from graphql import Source, parse
from graphql.error import GraphQLError


class GraphQLChecker(object):
    """
    flake8 plugin that lints your graphql strings
    """
    name = 'flake8-graphql'
    version = '0.1.1'

    def __init__(self, tree, *args, **kwargs):
        self.tree = tree

    def run(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Call) and getattr(node.func, 'id', None) == 'gql':

                first_arg = node.args[0]

                if isinstance(first_arg, ast.Str):
                    query = first_arg.s
                    try:
                        Source(query)
                        parse(query)
                    except GraphQLError as e:
                        yield (node.lineno, node.col_offset, 'GQL100: ' + e.message, type(self))
