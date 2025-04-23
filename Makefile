PYTHON_FILES := $(shell find . -name '*.py' -not -path '*.venv*')
YAML_FILES := $(shell find . -name '*.y*ml' -print)

.PHONY: pylint bandit codespell yamllint pycodestyle

pylint:
	pylint --rcfile=$(CURDIR)/.pylintrc $(PYTHON_FILES)

bandit:
	bandit -c $(PYTHON_FILES)

codespell:
	codespell -L wan -q 2 -S "./.git"

yamllint:
	yamllint $(YAML_FILES)

pycodestyle:
	pycodestyle $(PYTHON_FILES)
