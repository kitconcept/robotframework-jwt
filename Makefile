SHELL := /bin/bash
CURRENT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

all: clean build test

clean:
	@echo "Clean"
	rm -rf .py27

build:
	@echo "Build"
	virtualenv-2.7 || virtualenv .py27
	.py27/bin/pip install -r requirements.txt
	.py27/bin/python setup.py develop

test:
	@echo "Run Tests"
	.py27/bin/pybot test.robot

