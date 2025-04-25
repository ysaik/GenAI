PYTHON_FILES := $(shell find . -name '*.py' -not -path '*.venv*')
YAML_FILES := $(shell find . \( -name .github -o -name .git -o -name .venv \) -prune -o -type f -name '*.y*ml' -print)

.PHONY: pylint bandit codespell yamllint pycodestyle

pylint:
	pylint --rcfile=$(CURDIR)/.pylintrc $(PYTHON_FILES)

codespell:
	codespell -L wan -q 2 -S "./.git"

yamllint:
	yamllint $(YAML_FILES)

pycodestyle:
	pycodestyle $(PYTHON_FILES)

bandit:
	bandit $(PYTHON_FILES)

all:
	@echo "Running all linters..."
	@$(MAKE) pylint
	@$(MAKE) codespell
	@$(MAKE) yamllint
	@$(MAKE) pycodestyle
	@$(MAKE) bandit
	@echo "All linters completed."