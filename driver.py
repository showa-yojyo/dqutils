# -*- coding: UTF-8 -*-
#
# $Id$
"""dqutils 
あいうえお
"""

def run_load_strings():
    from dqutils.dq3.stringloader import load_strings
    load_strings(0x23, 0x27)

def run_load_battle_messages():
    from dqutils.dq3.message import load_battle_messages
    load_battle_messages()

def run_load_messages():
    from dqutils.dq3.message import load_messages
    #load_messages(0x0008, 0x000A)
    load_messages()

def run_parse_structs():
    from dqutils import configmanager, struct
    rompath = configmanager.get_config().get('ROM', 'DRAGONQUEST3')
    assert rompath
    confpath = 'dqutils/test/conf/dq3-C20000.conf'
    struct.parse_structs(rompath, confpath)


def run_dq6_load_strings():
    from dqutils.dq6.string import load_strings
    load_strings()

def run_dq6_message_battle():
    from dqutils.dq6.message import load_battle_messages
    load_battle_messages()

def run_dq6_message():
    from dqutils.dq6.message import load_messages
    load_messages(idfirst = 0x1B01)

def test_dq6():
    run_dq6_load_strings()
    run_dq6_message_battle()
    run_dq6_message()

def run_dq5_message():
    from dqutils.dq5.message import load_messages, load_battle_messages
    load_messages(idfirst = 0x0C7C)
    load_battle_messages()

def run_dq5_string():
    from dqutils.dq5.string import load_all_strings
    load_all_strings()

def test_dq5():
    #run_dq5_message()
    run_dq5_string()

if __name__ == '__main__':
    #run_load_strings()
    #run_load_battle_messages()
    #run_load_messages()
    #run_parse_structs()
    #test_dq6()
    #test_dq5()


    from dqutils.test import test_suite
    import unittest
    unittest.main(defaultTest="test_suite")

