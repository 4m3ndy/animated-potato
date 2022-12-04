#!/bin/bash

set -ev

export HOST=0.0.0.0
export PORT=12345
export METRICS_FILE_PATH="data/metrics_from_special_app.txt"

source /opt/animated-potato/env/bin/activate
gunicorn -b ${HOST}:${PORT} -w 4 wsgi:app