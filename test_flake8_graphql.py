# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals


def test_GQL101_pass_1(flake8dir):
    flake8dir.make_example_py("""
        query = "query { countries { name } }"
    """)
    result = flake8dir.run_flake8()
    assert result.out_lines == []


def test_GQL101_fail_1(flake8dir):
    flake8dir.make_example_py("""
        query = "queryd { countries { name } }"
    """)
    result = flake8dir.run_flake8()
    assert result.out_lines == [
    ]
