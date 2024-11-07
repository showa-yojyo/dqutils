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

### Dump data in CSV format

Subpackages `dqutils.dq3`, `dqutils.dq5` and `dqutils.dq6` provide a simple data
dump CLI tool. All tools have a common interface.

In the command line arguments, specify the address, object size and number of
objects.

In stdin, specify the layout of the object (not user-friendly)

The tool outputs data in CSV. The first column of output is the object index,
the rest is the data.

Suppose you want to dump the first five records of shop data. The data are
stored at address 0xC30900. The size of each object is eight. The structure of a
shop object is as follows:

| offset | bit mask |
|-------:|:--------:|
| 0 | 0x7f |
| 0 | 0x80 |
| 1 | 0xff |
| 2 | 0xff |
| 3 | 0xff |
| 4 | 0xff |
| 5 | 0xff |
| 6 | 0xff |
| 7 | 0xff |

In this case, run the following command:

```console
$ python -m dqutils.dq3.dumptool 0xC30900 8 5 --delimiter : <<< '#$00:#$007F
#$00:#$0080
#$01:#$00FF
#$02:#$00FF
#$03:#$00FF
#$04:#$00FF
#$05:#$00FF
#$06:#$00FF
#$07:#$00FF'
```

The output is:

```text
0000:06:1:08:1A:19:10:18:21:03
0001:02:1:77:B8:B9:BA:BB:00:00
0002:00:0:36:03:0D:3E:3F:55:79
0003:02:1:B8:B9:BA:BB:BF:00:00
0004:00:0:07:06:22:41:66:5C:00
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
