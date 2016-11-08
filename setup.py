from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-swaggerconsole',
    version=version,
    description="adds swagger file visualization",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Brock Anderson',
    author_email='brock@bandersgeo.ca',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.swaggerconsole'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        swagger_console=ckanext.swaggerconsole.plugin:SwaggerConsolePlugin
    ''',
)
