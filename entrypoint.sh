#!/bin/bash

# Collect static files
#echo "Collect static files"
#python manage.py collectstatic --noinput

# ################################
# ##### configure crontab. #######
# ################################
#echo "Configure crontab."
#python manage.py crontab add
#python manage.py crontab add
#echo "Confirm crontab configuration."
#python manage.py crontab show
# ################################

set -o xtrace
set -e
set -o pipefail

if [ -d "$SRC_DIR"  ]; then
    echo "$SRC_DIR"
    cd $SRC_DIR
fi

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000