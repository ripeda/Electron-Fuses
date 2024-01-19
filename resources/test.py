"""
Simple CI test to check if the module is working.
"""

import sys
import electron_fuses


def main(electron_binary: str):
    obj = electron_fuses.FuseConfig(electron_binary)
    print(obj)


if __name__ == "__main__":
    main(sys.argv[1])