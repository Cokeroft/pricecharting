#!/usr/bin/env bash

virtualenv -p python3 venv > setup.log
source venv/bin/activate >> setup.log
pip install -r requirements.txt >> setup.log

python super-nintendo.py