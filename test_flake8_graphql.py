# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals


def test_no_query(flake8dir):
    flake8dir.make_example_py("""
        name = 'hello world'
        name.split(' ')
    """)
    result = flake8dir.run_flake8(['--select=GQL'])
    assert result.out_lines == []


def test_GQL100_function_pass(flake8dir):
    flake8dir.make_example_py("""
        def gql(query):
            return query

        query = gql("query { countries { name } }")
    """)
    result = flake8dir.run_flake8(['--select=GQL'])
    assert result.out_lines == []


def test_GQL100_class_pass(flake8dir):
    flake8dir.make_example_py("""
        class gql(object):
            def __init__(self, query):
                self.query = query

        query = gql("query { countries { name } }")
    """)
    result = flake8dir.run_flake8(['--select=GQL'])
    assert result.out_lines == []


def test_GQL100_import_pass(flake8dir):
    flake8dir.make_example_py("""
        import gql

        query = gql("query { countries { name } }")
    """)
    result = flake8dir.run_flake8(['--select=GQL'])
    assert result.out_lines == []


def test_GQL100_function_fail(flake8dir):
    flake8dir.make_example_py("""
        def gql(query):
            return query

        query = gql("queryd countries { name } }")
    """)
    result = flake8dir.run_flake8(['--select=GQL'])
    assert result.out_lines == [
        './example.py:4:9: GQL100: Syntax Error GraphQL (1:1) Unexpected Name "queryd"',
    ]


def test_GQL100_class_fail(flake8dir):
    flake8dir.make_example_py("""
        class gql(object):
            def __init__(self, query):
                self.query = query

        query = gql("queryd countries { name } }")
    """)
    result = flake8dir.run_flake8(['--select=GQL'])
    assert result.out_lines == [
        './example.py:5:9: GQL100: Syntax Error GraphQL (1:1) Unexpected Name "queryd"',
    ]


def test_GQL100_import_fail(flake8dir):
    flake8dir.make_example_py("""
    import gql

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
    result = flake8dir.run_flake8(['--select=GQL'])
    assert result.out_lines == [
        './example.py:4:12: GQL100: Syntax Error GraphQL (4:9) Expected {, found Name "foobars"',
    ]


def test_GQL100_custom_identifer_fail(flake8dir):
    flake8dir.make_example_py("""
    from example import GQL

    def my_function():
        return GQL('''
        query FooQuery($bazValue:String!)

            foobars(boo:"A", baz:$bazValue){
                name
                surname
            }
        }
        ''')
    """)
    result = flake8dir.run_flake8(['--select=GQL', '--gql-identifier=GQL'])
    assert result.out_lines == [
        './example.py:4:12: GQL100: Syntax Error GraphQL (4:9) Expected {, found Name "foobars"',
    ]
