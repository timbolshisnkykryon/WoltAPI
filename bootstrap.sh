#!/usr/bin/env sh

export FLASK_APP=./wolt-look/index.py
pipenv run flask --debug run -h 0.0.0.0