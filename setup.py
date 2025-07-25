#!/usr/bin/python3
"""Setup"""
from setuptools import find_packages
from distutils.core import setup

version = "0.1.0"

with open("README.rst") as f:
    long_description = f.read()

setup(
    name="ofxstatement-bkb",
    version=version,
    author="Eleanor Young",
    author_email="developer@nausicaea.net",
    url="https://github.com/nausicaea/ofxstatement-bkb",
    description=("BKB plugin for ofxstatement"),
    long_description=long_description,
    license="GPLv3",
    keywords=["ofx", "banking", "statement", "iso-20022", "Basler Kantonalbank", "BKB"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "Topic :: Office/Business :: Financial :: Accounting",
        "Topic :: Utilities",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU Affero General Public License v3",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    namespace_packages=["ofxstatement", "ofxstatement.plugins"],
    entry_points={
        "ofxstatement": ["bkb = ofxstatement.plugins.bkb:BkbPlugin"]
    },
    install_requires=["ofxstatement"],
    extras_require={"test": ["pytest"]},
    include_package_data=True,
    zip_safe=True,
)
