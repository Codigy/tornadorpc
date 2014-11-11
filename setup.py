#!/usr/bin/env/python

import setuptools

with open("README.md") as readme:
    long_description = readme.read()
    with open("README", "w") as pypi_readme:
        pypi_readme.write(long_description)

setuptools.setup(
    name="tornadorpc",
    version="0.3",
    packages=["tornadorpc"],
    author="Josh Marshall, ress, codigy",
    install_requires=["tornado", "jsonrpclib"],
    author_email="info@codigy.ru",
    url="https://github.com/codigy/tornadorpc",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    description="TornadoRPC is a an implementation of both JSON-RPC and XML-RPC handlers for the Tornado framework.",
    long_description=long_description
)
