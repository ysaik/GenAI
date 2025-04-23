PYTHON_FILES := $(shell find . -name '*.py' -not -path '*.venv*')
YAML_FILES := $(shell find . -name '*.y*ml' -print)

pylint:
  pylint --rcfile=$(CURDIR)/.pylintrc $(PYTHON_FILES)

bandit:
  bandit -c .bandit.yaml $(PYTHON_FILES)

codespell:
  codespell -L wan -q 2 -S "./.git"

yamllint:
  yamllint $(YAML_FILES)
