#!/bin/sh

if [ -n "$DATABASE_URL" ]
    then
    # https://stackoverflow.com/a/29793382
    echo "Waiting on MySQL"
    while ! mysqladmin ping -h db --silent; do
        # Show some progress
        echo -n '.';
        sleep 1;
    done
    echo "Ready"
    # Give it another second.
    sleep 1;
fi

mkdir -p /run/uwsgi
chown -R www-data:www-data /run/uwsgi
exec uwsgi --ini /app/ctfd/docker-uwsgi/uwsgi-ctfd.ini

