# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals


def test_no_query(flake8dir):
    flake8dir.make_example_py("""
        name = 'hello world'
        name.split(' ')
    """)
    result = flake8dir.run_flake8()
    assert result.out_lines == []


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
    assert result.out_lines == [
        './example.py:5:9: GQL100: Syntax Error GraphQL (1:1) Unexpected Name "queryd"',
        '',
        '1: queryd countries { name } }',
        '   ^',
    ]
