Development Environment Setup Guide
===================================

This section outlines the steps necessary to setup the development environment for the |Project Name| project. 

Dependencies
------------
* `Python 3.11 64-Bit <https://www.python.org/downloads/windows/>`_

Setup
-----

Install the CLI tool in development mode by navigating to the Source directory and issuing the following command:

.. code-block:: console

   python setup.py develop

Tests
-----
To run the PyTests, execute the following steps:
1. Open a command prompt window.
2. Activate the virtual environment at Source\.venv\ by executing the activate.bat file.
3. Issue the following command from the root of the project to run the tests:

.. code-block:: console

   pytest Source/tests/

Build
-----

Build the production version of the CLI tool by navigating to the Source directory and issuing the following command:

.. code-block:: console

   python setup.py sdist bdist_wheel

Publish
-------

The built distributable package should be uploaded to the the `Nexus Repository<http://localhost:8081/>`_.


.. |Project Name| replace:: Unreal Bot
