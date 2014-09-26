# -*- coding: utf-8 -*-
""" dqutils.romimage module - TBW
"""

import mmap
from dqutils.config import get_config

# pylint: disable=too-few-public-methods
class RomImage(object):
    """TBW"""

    def __init__(self, title):
        self.title = title
        self.fin = None
        self.image = None

    def __enter__(self):
        rompath = get_config().get('ROM', self.title)
        fin = open(rompath, 'rb')
        image = mmap.mmap(fin.fileno(), 0, access=mmap.ACCESS_READ)

        self.fin, self.image = fin, image

        return self.image

    def __exit__(self, exc_type, exc_value, traceback):
        if self.image:
            self.image.close()
        if self.fin:
            self.fin.close()
