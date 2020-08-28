# !/usr/bin/env python3

import pathlib
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

# test dependencies
test_deps = [
    'pytest',
    'pytest-cov',
]
extras = {
    'test': test_deps,
}

# This call to setup() does all the work
setup(
    name="nse-install",
    version="0.0.1",
    description="Install and update external NSE script for nmap",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/remiflavien1/nse-install",
    author="shadawck",
    author_email="hug211mire@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Topic :: System :: Installation/Setup",
        'Topic :: Security',
    ],
    packages=["nse-install"],
    include_package_data=True,
    keywords='security, nse, nmap, pentest, scan, enumeration',
    tests_require=test_deps,
    extras_require=extras,
    install_requires=required,
    entry_points={
        "console_scripts": [
            "nse=nse.__main__",
        ]
    },
)
