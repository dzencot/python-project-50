# Difference calculator

[![Actions Status](https://github.com/dzencot/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/dzencot/python-project-50/actions) [![Python CI](https://github.com/dzencot/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/dzencot/python-project-50/actions/workflows/pyci.yml) [![Maintainability](https://api.codeclimate.com/v1/badges/ecdc4410853420af5ae0/maintainability)](https://codeclimate.com/github/dzencot/python-project-50/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/ecdc4410853420af5ae0/test_coverage)](https://codeclimate.com/github/dzencot/python-project-50/test_coverage)

### Links

This project was built using these tools:

| Tool                                                                   | Description                                             |
|------------------------------------------------------------------------|---------------------------------------------------------|
| [uv](https://docs.astral.sh/uv/)                                       | "An extremely fast Python package and project manager, written in Rust" |
| [Pytest](https://pytest.org)                                           | "A mature full-featured Python testing tool"            |
| [ruff](https://docs.astral.sh/ruff/)                                   | "An extremely fast Python linter and code formatter, written in Rust" |

---

### Setup

```bash
make install
```


### Run tests

```bash
make test
```

### Usage

```bash
uv run gendiff -h
usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```
