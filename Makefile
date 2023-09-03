# Makefile

# Variables
VENV_NAME?=venv
PYTHON=${VENV_NAME}/bin/python

# Targets

all: venv

venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: requirements.txt
	test -d $(VENV_NAME) || virtualenv $(VENV_NAME)
	${PYTHON} -m pip install --upgrade pip
	${PYTHON} -m pip install -Ur requirements.txt
	touch $(VENV_NAME)/bin/activate

lint:
	black main.py test_diatomic.py
	flake8 main.py test_diatomic.py


run:
	${PYTHON} main.py

test:
	${PYTHON} -m pytest

clean:
	rm -rf $(VENV_NAME)

.PHONY: all venv run test clean
