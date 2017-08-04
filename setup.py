from setuptools import setup


description = None
with open("README.rst", 'r') as fp:
    description = fp.read()


requirements = None
with open("requirements.txt", 'r') as fp:
    requirements = fp.readlines()


setup(
    name='flake8-graphql',
    version='0.0.1',
    description='A flake8 plugin to lint your graphql queries',
    long_description=description,
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
    install_requires=requirements,
    license="GPLv3",
    zip_safe=False,
    keywords='flake8, graphql',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
