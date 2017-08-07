# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import ast
import json

from graphql import Source, validate, parse, build_client_schema
from graphql.error import GraphQLError


class GraphQLChecker(object):
    """
    flake8 plugin that lints your graphql strings
    """
    name = 'flake8-graphql'
    version = '0.1.2'

    gql_schema = None

    def __init__(self, tree, *args, **kwargs):
        self.tree = tree

    @classmethod
    def add_options(cls, parser):
        parser.add_option(
            '--gql-schema',
            parse_from_config=True,
            help='Path to GraphQL schema file to validate graphql code against',
        )

    @classmethod
    def parse_options(cls, options):
        cls.gql_schema = options.gql_schema

    def run(self):
        schema = None
        if self.gql_schema is not None:
            with open(self.gql_schema, 'r') as fp:
                schema = build_client_schema(json.load(fp))

        for node in ast.walk(self.tree):
            if isinstance(node, ast.Call) and getattr(node.func, 'id', None) == 'gql':
                first_arg = node.args[0]

                if isinstance(first_arg, ast.Str):
                    query = first_arg.s
                    try:
                        source = Source(query)
                        gql_ast = parse(source)
                    except GraphQLError as e:
                        yield (node.lineno, node.col_offset, 'GQL100: ' + e.message, type(self))
                    else:
                        validation_errors = validate(schema, gql_ast)
                        for error in validation_errors:
                            yield (node.lineno, node.col_offset, 'GQL200: ', + str(error), type(self))
