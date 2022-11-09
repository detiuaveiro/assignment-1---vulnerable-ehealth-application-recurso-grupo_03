#!/bin/bash
export FLASK_APP=app/__init__.py
export FLASK_ENV=development
export FLASK_DEBUG=1

flask run