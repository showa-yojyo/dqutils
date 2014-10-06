# -*- coding: utf-8 -*-
"""dqutils.dq3.database - TBW"""

import dqutils.database

CONTEXT = dict(
    title="DRAGONQUEST3",
    mapper='HiROM',)

def process_xml(xml):
    """A transfer function."""
    dqutils.database.process_xml(CONTEXT, xml)
