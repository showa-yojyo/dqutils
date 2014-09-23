#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Run unit tests for dqutils package."""

def run_load_strings():
    """TBW"""
    from dqutils.dq3.string import load_string
    load_string(0x23)

def run_load_battle_messages():
    """TBW"""
    from dqutils.dq3.message import print_all_battle
    print_all_battle()

def run_load_messages():
    """TBW"""
    from dqutils.dq3.message import print_all
    #load_messages(0x0008, 0x000A)
    print_all()

def run_parse_structs():
    """TBW"""
    from dqutils import config
    rompath = config.get_config().get('ROM', 'DRAGONQUEST3')
    assert rompath
    #confpath = 'dqutils/test/conf/dq3-C20000.conf'
    #struct.parse_structs(rompath, confpath)

def run_dq6_load_strings():
    """TBW"""
    from dqutils.dq6.string import print_all
    print_all()

def run_dq6_message_battle():
    """TBW"""
    from dqutils.dq6.message import print_all_battle
    print_all_battle()

def run_dq6_message():
    """TBW"""
    from dqutils.dq6.message import load_msg
    load_msg(0x1B01)

def test_dq6():
    """TBW"""
    run_dq6_load_strings()
    run_dq6_message_battle()
    run_dq6_message()

def run_dq5_message():
    """TBW"""
    from dqutils.dq5.message import load_msg
    from dqutils.dq5.message import print_all_battle
    load_msg(0x0C7C)
    print_all_battle()

def run_dq5_string():
    """TBW"""
    from dqutils.dq5.string import print_all
    print_all()

def test_dq5():
    """TBW"""
    #run_dq5_message()
    run_dq5_string()

if __name__ == '__main__':
    from dqutils.test import test_suite
    import unittest
    unittest.main(defaultTest="test_suite")
