from setuptools import setup

with open("README.rst", "r") as f:
    description = f.read()

version_info = (0, 2, 3)
version = '.'.join(map(str, version_info))

setup(
    name='sqlalchemy-vertica',
    version=version,
    description='Vertica dialect for sqlalchemy',
    long_description=description,
    license='MIT',
    url='https://github.com/startappdev/sqlalchemy-vertica',
    download_url='https://github.com/startappdev/sqlalchemy-vertica/tarball/%s' % (version,),
    author='StartApp Inc.',
    author_email='ben.feinstein@startapp.com',
    packages=(
        'sqlalchemy_vertica',
    ),
    install_requires=(
        'six >= 1.10.0',
        'sqlalchemy >= 1.1.5',
    ),
    extras_require={
        'pyodbc': [
            'pyodbc >= 3.0.10',
        ],
        'turbodbc': [
            'turbodbc >= 1.0.1',
            'numpy >= 1.12.0',
        ],
        'vertica-python': [
            'psycopg2 >= 2.6.2',
            'vertica-python >= 0.6.13',
        ],
    },
    entry_points={
        'sqlalchemy.dialects': [
            'vertica.pyodbc = '
            'sqlalchemy_vertica.dialect_pyodbc:VerticaDialect [pyodbc]',
            'vertica.turbodbc = '
            'sqlalchemy_vertica.dialect_turbodbc:VerticaDialect [turbodbc]',
            'vertica.vertica_python = '
            'sqlalchemy_vertica.dialect_vertica_python:VerticaDialect [vertica-python]'
        ]
    }
)
