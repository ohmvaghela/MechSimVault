#!/bin/bash

# Create a Python script to list all simulations
echo "
from simulations.models import Simulation

simulations = Simulation.objects.all()

for sim in simulations:
    print(sim)
" > list_simulations.py

# Run the Python script using Django shell
python3 manage.py shell < list_simulations.py

# Clean up by removing the temporary Python script
rm list_simulations.py