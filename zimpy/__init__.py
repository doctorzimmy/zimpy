"""
zimpy
=====

Teaching-focused helper library for data cleaning.

Currently includes:
- ventclean: spot/remove sneaky Unicode gremlins in data
- datewizard (coming soon): fix ugly/broken date formats
"""

__version__ = "0.1.0"

from . import ventclean
from . import datewizard  # safe to include even if it's mostly placeholder
