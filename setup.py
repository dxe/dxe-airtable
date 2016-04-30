from __future__ import absolute_import, print_function, unicode_literals
from codecs import open
from os import path
from setuptools import find_packages, setup
from dxe_airtable import __version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dxe_airtable',
    version=__version__,
    description='Airtable library files used by DxE tech.',
    long_description=long_description,
    url='https://github.com/directactioneverywhere/dxe-airtable',
    author='DxE Tech Working Group',
    author_email='tech@directactioneverywhere.com',
    license='GPL-3.0',
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Topic :: Internet :: WWW/HTTP',
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    keywords='development',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests"
    ]
)
