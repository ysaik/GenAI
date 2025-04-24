PYTHON_FILES := $(shell find . -name '*.py' -not -path '*.venv*')
YAML_FILES := $(shell find . -type f -name "*.yaml" -o -name "*.yml" -not -path "*.github*" -a -not -path "*venv**")

.PHONY: pylint bandit codespell yamllint pycodestyle

pylint:
	pylint --rcfile=$(CURDIR)/.pylintrc $(PYTHON_FILES)

codespell:
	codespell -L wan -q 2 -S "./.git"

yamllint:
	yamllint $(YAML_FILES)

pycodestyle:
	pycodestyle $(PYTHON_FILES)

all:
	@echo "Running all linters..."
	@$(MAKE) pylint
	@$(MAKE) codespell
	@$(MAKE) yamllint
	@$(MAKE) pycodestyle
	@echo "All linters completed."