"""
__init__.py: electron-fuses package
"""

__version__:      str = "1.2.0"
__author__:       str = "RIPEDA Consulting"
__license__:      str = "3-clause BSD License"
__author_email__: str = "info@ripeda.com"

from .config    import FuseConfig
from .resources import FuseState, FuseV1Options, SentinelNotFound
from .resolve   import ResolveFramework