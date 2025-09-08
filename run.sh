#!/bin/bash
python -m venv .venv
.venv/bin/pip install ffmpeg-python
.venv/bin/python main.py
