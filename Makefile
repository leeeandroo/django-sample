.PHONY: develop install install-dev build clean

SHELL = /bin/bash
PYTHON = $(shell which python3)

default: bin/python3

bin/python3:
	virtualenv . -p ${PYTHON}
	bin/pip3 install --upgrade pip wheel
	bin/pip3 install --upgrade setuptools

install: bin/python3
	bin/pip3 install --upgrade -r requirements.txt

develop:
	bin/python3 setup.py develop

install-dev:
	bin/pip3 install --upgrade -r requirements-dev.txt

build:
	bin/python manage.py collectstatic --noinput
	bin/python manage.py migrate

clean:
	# virtualenv
	rm -Rf bin include lib local
	# buildout and pip
	rm -Rf develop-eggs eggs *.egg-info
	rm -Rf src parts build dist
	rm -Rf .installed.cfg pip-selfcheck.json