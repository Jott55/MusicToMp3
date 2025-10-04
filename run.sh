#!/bin/bash
python -m venv .venv

vpython=.venv/bin/python
vpip=.venv/bin/pip

$vpip install ffmpeg-python kivy
$vpython main.py
