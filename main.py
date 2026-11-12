"""Command line entry point.

TODO: parse the map, run the scheduler/simulator and print the turns.
"""

import sys
from parser import parse_map


def main(argv: list[str]) -> int:
    """Run the CLI with the command line arguments.

    TODO: check that exactly one map path was given, then call parse_map.
    """
    path = argv[0]
    try:
        parse_map(path)
    except FileNotFoundError:
        print(f"Error: cannot open map file '{path}': No such file or directory")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
