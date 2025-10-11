#!/usr/bin/fish

set firstTime false

if not [ -d .venv ]
	echo "Creating python $(python --version) venv"
	python -m venv .venv
	set firstTime true
end

if not [ -x (which ffmpeg) ] 
	if not [ -x "/usr/bin/ffmpeg" ]
		echo 'ERROR: you need to install ffmpeg at /usr/bin/'
		exit 1
	end
end

set vpython .venv/bin/python
set vpip .venv/bin/pip

function installDependencies
	echo 'Installing dependencies...'
	$vpip install "kivy[base]"

end

if $firstTime; or [ "$argv" = "install" ]
	installDependencies
end

$vpython main.py	

