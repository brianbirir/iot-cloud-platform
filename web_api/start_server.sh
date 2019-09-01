#!/bin/bash

function setup_server() {
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
}

function start_server() {
    echo Starting Gunicorn WSGI server........
    exec /usr/local/bin/gunicorn "src:create_app('config.DevelopmentConfig')" --bind 0.0.0.0:8000 --workers 4
}

setup_server
start_server

exit 0