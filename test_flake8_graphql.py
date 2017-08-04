# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals


def test_GQL100_pass_1(flake8dir):
    flake8dir.make_example_py("""
        def gql(query):
            return query


        query = gql("query { countries { name } }")
    """)
    result = flake8dir.run_flake8()
    assert result.out_lines == []


def test_GQL100_fail_1(flake8dir):
    flake8dir.make_example_py("""
        def gql(query):
            return query


        query = gql("queryd countries { name } }")
    """)
    result = flake8dir.run_flake8()
    assert result.out_lines[0] == (
        './example.py:5:13: GQL100: Syntax Error GraphQL (1:1) Unexpected Name "queryd"'
    )
