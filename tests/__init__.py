"""dqutils.tests.__init__: dummy module"""

import pytest

from dqutils.config import get_config

requires_config = pytest.mark.skipif(get_config() is None, reason="No configuration provided")
