"""Tests for the map parser.

TODO: remove the `skip` marks as the parser gets implemented.
"""

from pathlib import Path

import pytest

from parser import MapParseError, parse_map


def test_parser_is_not_implemented_yet() -> None:
    """Placeholder: the parser stub must raise until it is written."""
    with pytest.raises(NotImplementedError):
        parse_map("any_map.txt")


@pytest.mark.skip(reason="TODO: parser not implemented yet")
def test_parses_valid_map(tmp_path: Path) -> None:
    """A valid map is parsed into a network with drones and zones."""
    map_file = tmp_path / "valid.txt"
    map_file.write_text(
        "nb_drones: 2\n"
        "start_hub: hub 0 0 [color=green]\n"
        "end_hub: goal 2 0 [color=yellow]\n"
        "hub: mid 1 0 [zone=priority max_drones=2]\n"
        "connection: hub-mid [max_link_capacity=2]\n"
        "connection: mid-goal\n"
    )
    parse_map(str(map_file))


@pytest.mark.skip(reason="TODO: parser not implemented yet")
def test_rejects_missing_nb_drones(tmp_path: Path) -> None:
    """The first line must define the number of drones."""
    map_file = tmp_path / "no_drones.txt"
    map_file.write_text("start_hub: hub 0 0\nend_hub: goal 1 0\n")
    with pytest.raises(MapParseError):
        parse_map(str(map_file))


@pytest.mark.skip(reason="TODO: parser not implemented yet")
def test_rejects_duplicate_connection(tmp_path: Path) -> None:
    """`a-b` and `b-a` describe the same connection."""
    map_file = tmp_path / "duplicate.txt"
    map_file.write_text(
        "nb_drones: 1\n"
        "start_hub: hub 0 0\n"
        "end_hub: goal 1 0\n"
        "connection: hub-goal\n"
        "connection: goal-hub\n"
    )
    with pytest.raises(MapParseError):
        parse_map(str(map_file))
