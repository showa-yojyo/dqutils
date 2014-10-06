# -*- coding: utf-8 -*-
"""dqutils.dq5.database - TBW"""

import dqutils.database

CONTEXT = dict(
    title="DRAGONQUEST5",
    mapper='LoROM',)

def process_xml(xml):
    """A transfer function."""
    dqutils.database.process_xml(CONTEXT, xml)
