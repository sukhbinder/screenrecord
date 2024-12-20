# screenrecord

[![PyPI](https://img.shields.io/pypi/v/screenrecord.svg)](https://pypi.org/project/screenrecord/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/screenrecord?include_prereleases&label=changelog)](https://github.com/sukhbinder/screenrecord/releases)
[![Tests](https://github.com/sukhbinder/screenrecord/actions/workflows/test.yml/badge.svg)](https://github.com/sukhbinder/screenrecord/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/screenrecord/blob/master/LICENSE)

Record screen with python

## Installation

Install this tool using `pip`:
```bash
pip install screenrecord
```
## Usage

For help, run:
```bash
record --help
```
You can also use:
```bash
python -m record --help
```

![demo usage of screenrecord](usage.gif)

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:
```bash
cd screenrecord
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
