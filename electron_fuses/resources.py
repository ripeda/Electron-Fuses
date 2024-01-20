"""
constants.py: Fuses constants
"""

import enum


# https://github.com/electron/fuses/blob/v1.7.0/src/constants.ts#L1
SENTINEL: str = "dL7pKGdnNz796PbbjQWNKmHXBZaB9tsX"


# https://github.com/electron/fuses/blob/v1.7.0/src/constants.ts#L3-L8
class FuseState(enum.Enum):
    DISABLE: int = 0x30
    ENABLE:  int = 0x31
    REMOVED: int = 0x72
    INHERIT: int = 0x90


# https://github.com/electron/fuses/blob/v1.7.0/src/config.ts#L8-L17
class FuseV1Options(enum.Enum):
    RUN_AS_NODE:                               int = 0x00
    ENABLE_COOKIE_ENCRYPTION:                  int = 0x01
    ENABLE_NODE_OPTIONS_ENVIRONMENT_VARIABLE:  int = 0x02
    ENABLE_NODE_CLI_INSPECT_ARGUMENTS:         int = 0x03
    ENABLE_EMBEDDED_ASAR_INTEGRITY_VALIDATION: int = 0x04
    ONLY_LOAD_APP_FROM_ASAR:                   int = 0x05
    LOAD_BROWSER_PROCESS_SPECIFIC_V8_SNAPSHOT: int = 0x06
    GRANT_FILE_PROTOCOL_EXTRA_PRIVILEGES:      int = 0x07


class SentinelNotFound(Exception):
    pass