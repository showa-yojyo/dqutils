# About dqutils

[![Test](https://github.com/showa-yojyo/dqutils/actions/workflows/test.yml/badge.svg?branch=develop)](https://github.com/showa-yojyo/dqutils/actions/workflows/test.yml)
[![Release](https://github.com/showa-yojyo/dqutils/actions/workflows/release.yml/badge.svg?branch=master)](https://github.com/showa-yojyo/dqutils/actions/workflows/release.yml)

**dqutils** is a Python package for looking program data in Dragon Quest series.

This package provides the following features:

* (DQ3, 5 and 6) View all text data of scenatio and battle scene.
* (DQ3, 5 and 6) View all string data.
* (DQ3, 5 and 6) Dump arrays of structs.

## Setup

### How to install

As the package is not currently published on any package registry (e.g. PyPI),
install directly from your local repositories. For example:

```console
$ git clone https://github.com/showa-yojyo/dqutils
...
$ cd $SOME_DIRECTORY
$ pipenv install /path/to/dqutils
```

### How to configure

Before run a dqutils tool, you must make one of the directory below:

* `$XDG_CONFIG_HOME/dqutils`
* `$HOME/.config/dqutils`
* `$HOME/.dqutils`

Under one of the directory above, put a text file named `config` and edit as
follows:

```ini
# $XDG_CONFIG_HOME/dqutils/config example:
[ROM]
DRAGONQUEST3 = /path/to/DRAGONQUEST3.smc
DRAGONQUEST5 = /path/to/DRAGONQUEST5.smc
DRAGONQUEST6 = /path/to/DRAGONQUEST6.smc
```

## How to test

UNDER CONSTRUCTION (issue #11) (available only for developers?)

Run the following command under the project root directory:

```console
PYTHONPATH=./src:./tests pipenv run python -m unittest discover ./tests
```

You can use Hatch as well as Pipenv:

```console
PYTHONPATH=./src:./tests hatch test ./tests
```

## Build the Package

To build the package, install the required packages and run the build command
with Pipenv. The generated files will be in the `dist` directory. For example:

```console
$ cd $REPOSITORY_ROOT
$ pipenv sync
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
Installing dependencies from Pipfile.lock (xxxxxx)...
All dependencies are now up-to-date!
$ pipenv run python -m build
* Creating isolated environment: venv+pip...
* Installing packages in isolated environment:
  - hatchling
* Getting build dependencies for sdist...
* Building sdist...
* Building wheel from sdist
* Creating isolated environment: venv+pip...
* Installing packages in isolated environment:
  - hatchling
* Getting build dependencies for wheel...
* Building wheel...
Successfully built dqutils-x.y.z.tar.gz and dqutils-x.y.z-py3-none-any.whl
```

## Usage

### View Texts

To print all of the message data in Dragon Quest 3, run:

```console
python -m dqutils.dq3 print-scenatio-messages
python -m dqutils.dq3 print-battle-messages
```

To print all of the string data in Dragon Quest 3, run:

```console
python -m dqutils.dq3 print-strings
```

### View Sprites, Sounds, Bytecodes, etc.

TBW

## License

See the `LICENSE` file under the installation directory.

## Authors

* プレハブ小屋
  * Web site (GitHub): [showa-yojyo (プレハブ小屋)](https://github.com/showa-yojyo/)
  * E-mail: <yojyo@hotmail.com>
  * Twitter: [@showa_yojyo](https://twitter.com/showa_yojyo)
