Flake8 GraphQL
==============

|TravisCI| |PyPi|

Plugin for linting graphql query strings within your code.

Mark your query strings with any function or class named ``gql`` to perform linting:


.. code:: python

    def gql(query):
        return query

    myquery = gql("""
    {
      empireHero: hero(episode: EMPIRE) {
      name
    }
    jediHero: hero(episode: JEDI) {
      name
    }
    """)

You can also customise the identifier to any value with the ``--gql-identifier`` option. This can
be set with command line arguments or within ``setup.cfg``.

.. code:: shell

   $ flake8 --gql-identifier=GQL


.. code:: python

    class GQL(str):
        pass

    myquery = GQL("""
    {
      project(name: "GraphQL") {
        tagline
      }
    }
    """)

.. |TravisCI| image:: https://travis-ci.org/MichaelAquilina/flake8-graphql.svg?branch=master
   :target: https://travis-ci.org/MicahelAquilina/flake8-graphql

.. |PyPi| image:: https://badge.fury.io/py/flake8-graphql.svg
   :target: https://badge.fury.io/py/flake8-graphql
