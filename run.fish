#!/usr/bin/fish
if not test -d .venv
	echo "Creating python $(python --version) venv"
	python -m venv .venv
end

set vpython .venv/bin/python
set vpip .venv/bin/pip

if not test ($vpip list | grep -e ffmpeg-python -e kivy)
	echo 'Installing dependencies...'
	$vpip install ffmpeg-python
	$vpip install "kivy[base]"
end

$vpython main.py	

