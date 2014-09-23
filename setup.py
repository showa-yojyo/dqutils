#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""setup script for dqutils package"""

from distutils.core import setup
setup(name='dqutils',
      version='1.1.0',
      description='dqutils (Python version)',
      author='yojyo@hotmail.com',
      author_email='yojyo@hotmail.com',
      url='http://www.geocities.jp/showa_yojyo/dq/',
      packages=['dqutils',
                'dqutils.dq3',
                'dqutils.dq5',
                'dqutils.dq6',
                'dqutils.test'],
      package_data={'dqutils.test':['conf/*.conf', 'conf/*.conf.error']})
