#!/bin/bash
export FLASK_APP=app_sec/__init__.py
export FLASK_ENV=development
export FLASK_RUN_PORT=5051
export FLASK_DEBUG=1

flask run