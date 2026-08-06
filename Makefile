.PHONY install debug run clean lint lint-strict

PYTHON ?= python3 # ?= is an equivalent for "if not defined" in Makefile. It allows the user to override the default value by passing a different value when invoking make.
CONFIG ?= config.txt
MAIN_SCRIPT ?= a_maze_ing.py

install:
	$(PYTHON) -m pip install -r requirements.txt

run:
	$(PYTHON) $(MAIN_SCRIPT) $(CONFIG)

debug:
	$(PYTHON) -m pdb $(MAIN_SCRIPT) $(CONFIG)

clean:
	rm -rf __pycache__ .mypy_cache dist/ build/ mazegen_amazeing.egg-info/
	rm -f maze.txt

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict
