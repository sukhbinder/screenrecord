# screenrecord

[![PyPI](https://img.shields.io/pypi/v/screenrecord.svg)](https://pypi.org/project/screenrecord/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/screenrecord?include_prereleases&label=changelog)](https://github.com/sukhbinder/screenrecord/releases)
[![Tests](https://github.com/sukhbinder/screenrecord/actions/workflows/test.yml/badge.svg)](https://github.com/sukhbinder/screenrecord/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/screenrecord/blob/master/LICENSE)

Record screen with python

The backstory for this tool is [here](https://sukhbinder.wordpress.com/?s=screenrecord)

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

Examples:

  # Record the active window (you select it with mouse) as a GIF
  record demo.gif -aw

  # Record fullscreen for 10 seconds at 15 FPS
  record fullscreen.mp4 -f -dur 10 --fps 15

  # Record a specific region as a GIF with infinite loop
  record region.gif --bbox 0 0 50 50 -l 0

  # Record active window, save individual frames to temp folder
  record clip.gif -aw -s

```

![demo usage of screenrecord](https://raw.githubusercontent.com/sukhbinder/screenrecord/main/usage.gif)

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
