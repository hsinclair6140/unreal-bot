# Documentation

## Overview
This directory is intended for documentation only and contains Sphinx code that can be edited, built, and published to a GitHub Pages website. 

See the repository's GitHub Pages for the built results of the documentation within this repository. 

## Building the Docs Through GitHub Actions Automation
Merging any non-main branch into main will trigger a GitHub Action that will build and publish the docs to repository's GitHub Pages website. The 'pages' branch will be used for publishing and should not be used for any other reason.

## Building the Docs Locally
The following section provides instructions on how to build the HTML locally. This step is not necessary, but may be useful for a quick preview of what the built HTML may look like.

### Dependencies
#### Python
##### Version
[Python 3.11-64 bit](https://www.python.org/downloads/windows/).

##### Python Package Dependencies
To quickly setup the Python virtual environment, execute the doc_env_setup.bat file. This will create a Python virtual environment that can be used to build the docs. 

Alternatively, to manually install the Python dependencies to an existing environment, run the following command using the desired Python environment:

`pip install -r doc_requirements.txt`

### Build
To build the Sphinx code, run the following command in the root of the project:

`sphinx-build doc _build`

The HTML will be built to _build folder and can be preview by opening the HTML files within.
