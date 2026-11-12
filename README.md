*This project has been created as part of the 42 curriculum by fsayuri-*

# fly-in

## Description

`fly-in` is a drone routing simulation written in Python 3.10+.

The program reads a network of connected zones from a text file and must move a
fleet of drones from a `start_hub` to an `end_hub` in the smallest possible
number of turns. Each zone and each connection has a capacity, zones have a
type that changes the cost of entering them (`normal`, `priority`, `restricted`
and `blocked`), and every turn is simulated synchronously: all drones move at
the same time, and a drone that leaves a zone frees its slot in that same turn.

The project is fully object-oriented, uses no graph libraries (`networkx`,
`graphlib`, etc. are forbidden) and is checked with `flake8` and `mypy`.

## Instructions

### Requirements

- Python 3.10 or newer
- [`uv`](https://docs.astral.sh/uv/) 

### Installing `uv`

`uv` is a single binary and does not need `sudo`. On Linux and macOS:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

The installer puts the binary in `~/.local/bin`. If that directory is not in
your `PATH` yet, add it to your shell configuration (`~/.zshrc` or `~/.bashrc`):

```sh
export PATH="$HOME/.local/bin:$PATH"
```

Alternatives without `sudo`:

```sh
pip install --user uv
# or
pipx install uv
```

Check the installation:

```sh
uv --version
```

If the machine has an old system Python, `uv` can install a newer one for you:

```sh
uv python install 3.12
```

### Install, run and test

All commands are available through the `Makefile`:

```sh
make install   # uv sync: creates .venv and installs the dev tools
make run       # runs the program with MAP (default: maps/map.txt)
make debug     # same, under pdb
make test      # runs the test suite with pytest
make lint      # flake8 + mypy
make clean     # removes __pycache__, .mypy_cache and .pytest_cache
```

Pass a specific map file with `MAP`:

```sh
make run MAP=maps/easy/01.txt
```

The equivalent commands without `make` are:

```sh
uv sync
uv run python main.py maps/map.txt
uv run python -m pytest -q
```

### Current status

The repository currently contains the project skeleton: the `Makefile`, the
`pyproject.toml` with the development dependencies, the CLI entry point
(`main.py`), the parser stub (`parser.py`) and the first parser tests. The
parser, the object model, the pathfinding, the scheduler, the simulator and the
renderer are still to be implemented.
