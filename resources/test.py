
import sys
import electron_fuses


def main(electron_binary: str = sys.argv[1]):
    obj = electron_fuses.FuseConfig(electron_binary)
    print(obj)

    # Find value of RUN_AS_NODE
    print(obj.config[electron_fuses.FuseV1Options.RUN_AS_NODE])

if __name__ == "__main__":
    main()