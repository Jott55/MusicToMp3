#!/usr/bin/fish
if not test -d .venv
	echo "Creating python $(python --version) venv"
	python -m venv .venv
end

set vpython .venv/bin/python
set vpip .venv/bin/pip

function installDependencies
	echo 'Installing dependencies...'
	$vpip install ffmpeg-python
end

if test -z ($vpip list | grep -e ffmpeg-python); or test "$argv" = "install"
	installDependencies
end

$vpython main.py	

