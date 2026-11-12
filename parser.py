"""Map file parser.

TODO: implement the input format described in AGENT.md section 2:
comments, `nb_drones`, `start_hub` / `end_hub`, `hub` metadata and
bidirectional `connection` lines.
"""


from resource import error


class MapParseError(Exception):
    """Error raised for an invalid map file.

    TODO: carry the line number and a clear cause in the message.
    """


def parse_map(path: str) -> None:
    """Read a map file and build the network model.

    TODO: open the file, validate every line and return a Map object.
    For now this is only a placeholder.
    """
    with open(path, "r", encoding="utf-8") as file:
        for lineno, raw in enumerate(file, start=1):
            line = raw.split("#", 1)[0].strip()
            if not line:
                continue
            print(f"{lineno}: {line}")
