# About dqutils

**dqutils** is a Python package for looking program data in Dragon Quest series.

This package provides the following features:

* (DQ3, 5 and 6) View all text data of scenatio and battle scene.
* (DQ3, 5 and 6) View all string data.
* (DQ3, 5 and 6) Dump arrays of structs.

## Setup

### Installation

If you want to use this package, you need Python 3.0 or higher.
Python 2.x are no longer supported.

    $ git clone https://github.com/showa-yojyo/dqutils.git
    $ pip install -e ./dqutils

### Setting

First, you must make the directory `.dqutils` in your home directory.
This directory contains the setting files that dqutils package refers to.

    $ mkdir -p ~/.dqutils

Then, touch the file `config` and edit as follows for example:

    # dqutils rc file
    [ROM]
    DRAGONQUEST3 = /path/to/DRAGONQUEST3.smc
    DRAGONQUEST5 = /path/to/DRAGONQUEST5.smc
    DRAGONQUEST6 = /path/to/DRAGONQUEST6.smc

### Testing

UNDER CONSTRUCTION (issue #11) (available only for developers?)

For example:

    $ cd $REPOSITORY_ROOT
    $ PYTHONPATH=./src pipenv run python -m unittest discover .
    ....................................s.........................................................
    ----------------------------------------------------------------------
    Ran 94 tests in 0.130s

    OK (skipped=1)

## Usage

### View Texts

To print all of the message data in Dragon Quest 3, type:

    $ python -m dqutils.dq3 print-scenatio-messages
    $ python -m dqutils.dq3 print-battle-messages

To print all of the string data in Dragon Quest 3, type:

    $ python -m dqutils.dq3 print-strings

### View Sprites, Sounds, Bytecodes, etc.

TBW

## License

See the `LICENSE` file under the installation directory.

## Authors

* プレハブ小屋
  * Web site (GitHub): [showa-yojyo (プレハブ小屋)](https://github.com/showa-yojyo/)
  * E-mail: yojyo@hotmail.com
  * Twitter: [@showa_yojyo](https://twitter.com/showa_yojyo)
