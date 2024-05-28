#!/usr/bin/env bash

cd /usr/local/bin/swu
.venv/bin/gunicorn --config gunicorn_config.py main:app