UV ?= uv
MAP ?= maps/easy/01_linear_path.txt

.PHONY: install run debug clean lint lint-strict test

install:
	$(UV) sync

run:
	$(UV) run python main.py $(MAP)

debug:
	$(UV) run python -m pdb main.py $(MAP)

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .mypy_cache .pytest_cache

lint:
	$(UV) run flake8 .
	$(UV) run mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	$(UV) run flake8 .
	$(UV) run mypy . --strict

test:
	$(UV) run python -m pytest -q
