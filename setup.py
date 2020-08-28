# !/usr/bin/env python3

import pathlib
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open("nse_install/__init__.py") as ver:
    init = ver.read()

version = init.split("=")[-1].strip().strip("\"")


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
    name="nse_install",
    version=version,
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
        "Topic :: System :: Installation/Setup",
        'Topic :: Security',
    ],
    packages=["nse_install"],
    #package_dir={'nse_install':'nse_install'}, 
    #package_data={
    #    'nse_install': ['script.toml'],
    #},
    package_data = {
        # If any package contains .toml include them
        '': ['*.toml'],
    },
    data_files=[
        ('/etc/nse_install/', ['script.toml']),
    ],
    include_package_data=True,
    keywords='security, nse, nmap, pentest, scan, enumeration',
    tests_require=test_deps,
    extras_require=extras,
    install_requires=required,
    entry_points={
        "console_scripts": [
            "nse_install=nse_install.__main__:main",
        ]
    },
)
