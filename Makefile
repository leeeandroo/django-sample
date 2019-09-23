.PHONY: develop install install-dev build clean

SHELL = /bin/bash
PYTHON = $(shell which python3.7 || which python3.6 || which python3.5 || which python3.4)

default: bin/python3

bin/python3:
	virtualenv . -p ${PYTHON} --no-site-packages
	bin/pip3 install --upgrade pip wheel

install: bin/python3
	bin/pip install --upgrade -r requirements.txt

develop:
	bin/python3 setup.py develop

install-dev:
	bin/pip install --upgrade -r requirements-dev.txt

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