from setuptools import setup


setup(
    name='flake8-graphql',
    version='0.0.1',
    description='A flake8 plugin to lint your graphql queries',
    long_description='',
    author="Michael Aquilina",
    author_email="michaelaquilina@gmail.com",
    url='https://github.com/michaelaquilina/flake8-graphql',
    entry_points={
        'flake8.extension': [
            'GQL = flake8_graphql:GraphQLChecker',
        ],
    },
    py_modules=['flake8_graphql'],
    include_package_data=True,
    install_requires=[
        'flake8!=3.2.0',
    ],
    license="GPLv3",
    zip_safe=False,
    keywords='flake8, graphql',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
