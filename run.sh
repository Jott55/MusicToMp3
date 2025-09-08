#!/bin/bash
python -m venv .venv
source .venv/bin/activate
pip install ffmpeg-python
.venv/bin/python main.py
