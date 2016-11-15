#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='grill-maya',
    version='0.1.0.0',
    packages=find_packages(),
    description='Maya tools expanding the grill framework.',
    author='Christian Lopez Barron',
    author_email='christianlb.vfx@outlook.com',
    url='https://github.com/chrizzFTD/grill-maya',
    download_url='https://github.com/chrizzFTD/grill-maya/releases/tag/0.1.0.0',
    classifiers=[],
    package_data={
        "grill_maya": ["*.py"]
    }
)
