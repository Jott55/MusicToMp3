#!/bin/bash
vpython=.venv/bin/python
vpip=.venv/bin/pip
firstTime=false

if ! [ -d '.venv' ]; then
    echo "Creating python $(python --version) venv"
    python -m venv .venv
    firstTime=true
fi

if ! [ -x $(which ffmpeg) ]; then
    if ! [ -x '/usr/bin/ffmpeg' ]; then
        echo "ERROR: you need to install ffmpeg at /usr/bin/"
        exit 1
    fi
fi

installDependencies() {
    echo "installing dependencies"
    $vpip install 'kivy[base]'
}

if $firstTime || [ "$1" = "install" ]; then
    installDependencies
fi

$vpython main.py