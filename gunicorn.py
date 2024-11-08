# location of gunicorn executable
# command = '/usr/bin/gunicorn'

# Loaction of manage.py
# pythonpath = '/MechSimVault'
# pythonpath = '/home/ohm/webd/MechSimVault'

bind = '0.0.0.0:8000'

workers = 3

# Run server
# gunicorn -c gunicorn.py Test.wsgi 
