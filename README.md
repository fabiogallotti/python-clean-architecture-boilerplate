# python_clean_architecture_boilerplate

A boilerplate for a clean architecture implementation in python

## Setup

### Prerequisites

#### Development environment setup

- Install pyenv

    ```bash
    brew update
    brew install pyenv
    ```

  - Append to  `~/.zshrc` :

    ```bash
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    ```

- Install pyenv-virtualenv

    ```bash
    brew install pyenv-virtualenv
    ```

  - Append to  `~/.zshrc` :

    ```bash
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    ```

- Install Python build dependencies, because pyenv builds python from source

    ```bash
    brew install openssl readline sqlite3 xz zlib
    ```

- Install Python version

    ```bash
    pyenv install 3.9.1
    ```

- Install Poetry

    ```bash
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
    ```

  - Set virtualenv inside the project's root directory

    ```bash
    poetry config virtualenvs.in-project true
    ```

### Install

- Activate a compatible python version, `pyenv local 3.9.1`
- Install the repo with all its dependencies: `make install`

### Lint

- `make lint` will execute all the required checks

### Test

- `make test-unit` will execute only the unit tests.
- `make test` will execute all the tests, also the integration ones.
