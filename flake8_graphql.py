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
    version = '0.2.0'

    def __init__(self, tree, *args, **kwargs):
        self.tree = tree

    @classmethod
    def add_options(cls, parser):
        parser.add_option(
            '--gql-identifier',
            type='string',
            default='gql',
            help='Name of function or class to identify GraphQL strings with',
            parse_from_config=True,
        )

    @classmethod
    def parse_options(cls, options):
        cls.gql_identifier = options.gql_identifier

    def run(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Call) and getattr(node.func, 'id', None) == self.gql_identifier:
                first_arg = node.args[0]

                if isinstance(first_arg, ast.Str):
                    query = first_arg.s
                    try:
                        Source(query)
                        parse(query)
                    except GraphQLError as e:
                        yield (node.lineno, node.col_offset, 'GQL100: ' + e.message, type(self))
