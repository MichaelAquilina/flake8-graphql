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

def test_GQL100_fail_2(flake8dir):
    flake8dir.make_example_py("""
    def gql(q):
        return q


    def my_function():
        return gql('''
        query FooQuery($bazValue:String!)

            foobars(boo:"A", baz:$bazValue){
                name
                surname
            }
        }
        ''')
    """)
    result = flake8dir.run_flake8()
    assert result.out_lines == [
        './example.py:6:12: GQL100: Syntax Error GraphQL (4:9) Expected {, found Name "foobars"',
        '',
        '3: ',
        '4:         foobars(boo:"A", baz:$bazValue){',
        '           ^',
        '5:             name',
    ]
