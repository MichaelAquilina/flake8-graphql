Flake8 GraphQL
==============

|TravisCI|

Plugin for linting graphql query strings within your code.

Mark your query strings with any function named gql to perform linting:

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


.. |TravisCI| image:: https://travis-ci.org/MichaelAquilina/flake8-graphql.svg?branch=master
   :target: https://travis-ci.org/MicahelAquilina/flake8-graphql
