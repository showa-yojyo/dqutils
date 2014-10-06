# -*- coding: utf-8 -*-
"""dqutils.dq6.database - TBW"""

import dqutils.database

CONTEXT = dict(
    title="DRAGONQUEST6",
    mapper='HiROM',)

def process_xml(xml):
    """A transfer function."""
    dqutils.database.process_xml(CONTEXT, xml)
