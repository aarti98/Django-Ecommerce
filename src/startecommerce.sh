#!/bin/bash
NAME=ecommerce
DJANGODIR=/home/ubuntu/Projects/Django-Ecommerce/src           # Django project directory
SOCKFILE=/home/ubuntu/Projects/Django-Ecommerce/src/run/gunicorn.sock  # we will communicte using this unix socket
USER=ubuntu                                        # the user to run as
GROUP=ubuntu                                   # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=ecommerce.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=ecommerce.wsgi                     # WSGI module name
 
echo "Starting $NAME as `whoami`"

# Activate the virtual environment
##################################
#source /home/ubuntu/.local/bin/virtualenvwrapper.sh
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
export WORKON_HOME="$HOME/.virtualenvs"
export PROJECT_HOME="$HOME/Projects"

#source /usr/share/virtualenvwrapper/virtualenvwrapper.sh

workon housing
#################################



# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=- &

