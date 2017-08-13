# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import ast
import collections
import re

from graphql import Source, parse
from graphql.error import GraphQLError


Position = collections.namedtuple('Position', ['line_no', 'col_offset'])


def get_col_line_offset(message):
    """
    Retrieve the line and column offset from a GraphQL erro message
    """
    pattern = re.compile(r'\((?P<line_no>\d+):(?P<col_offset>\d+)\)')
    match = pattern.search(message)
    if match is None:
        return None

    groupdict = match.groupdict()
    return Position(int(groupdict['line_no']), int(groupdict['col_offset']))


class GraphQLChecker(object):
    """
    flake8 plugin that lints your graphql strings
    """
    name = 'flake8-graphql'
    version = '0.2.5'

    def __init__(self, tree, *args, **kwargs):
        self.tree = tree

    @classmethod
    def add_options(cls, parser):
        parser.add_option(
            '--gql-identifier',
            type=str,
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
                        import ipdb; ipdb.set_trace()
                        line_no = node.lineno
                        col_offset = node.col_offset

                        lines = e.message.split('\n')
                        position = get_col_line_offset(lines[0])
                        if position is not None:
                            line_no += position.line_no - 1

                        yield (line_no, col_offset, 'G100 ' + lines[0], type(self))
