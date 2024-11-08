#!/bin/bash

gunicorn -c gunicorn.py MechSimVault.wsgi