# Torch Platform Integration Testing

Repository for integration testing of Torch Platform.  This is a living project that should evolve with requirements
and discoveries of connected features and services.

# Dependencies

OSX/Linux:
- pyenv

Windows:
- 

Additional Dependencies:
- Poetry
- Python 3.x
- Pytest

# Setup

## OSX/Linux:
```shell
brew install pyenv
pyenv install 3.10.19
pyenv local 3.10.19
```
Add the following to your `~/.zshrc`

```shell
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

```
pip install poetry
poetry install
```

# Outline

Tests are located in the root of src/inttest/python and further broken down by service.

The following primary components are tested

## ORCUS

To run all tests

```shell
make test
```

to run a single test

```shell
make test-single <test_name>
```
(eg. `make test-single test_admin_config`)