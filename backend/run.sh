#!/bin/bash
# run.sh

export FLASK_APP=app.py
export APP_SETTINGS="config.DevelopmentConfig"
flask run --host=0.0.0.0 --port=5000