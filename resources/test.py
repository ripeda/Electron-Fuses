"""
Simple CI test to check if the module is working.
"""

import sys
import electron_fuses


def main(electron_binary: str):
    if electron_binary.endswith(".app"):
        electron_binary = electron_fuses.ResolveFramework(electron_binary).framework()

    print(f"Using Electron binary: {electron_binary}")

    obj = electron_fuses.FuseConfig(electron_binary)
    print(obj)


if __name__ == "__main__":
    main(sys.argv[1])