# Development

## Setup Local Env

Create a virtualenv to work with and install the package for editing.

    python3 -m venv myvenv
    source myvenv/bin/activate
    pip install -e .[dev]

## Release

First, bump the version in `sink/__init__.py` and then run the release script:

    ./release.sh
