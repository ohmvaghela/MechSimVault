#!/bin/bash

# Define simulation details
simulations=(
    "user1@example.com|Simulation Title 1|Description 1|Software 1"
    "user2@example.com|Simulation Title 2|Description 2|Software 2"
    "user3@example.com|Simulation Title 3|Description 3|Software 3"
    "user4@example.com|Simulation Title 4|Description 4|Software 4"
    "user5@example.com|Simulation Title 5|Description 5|Software 5"
)

# Create simulations using Django shell
for sim in "${simulations[@]}"; do
    IFS='|' read -r email title description software <<< "$sim"
    echo "
from siteUser.models import SiteUser
from simulations.models import Simulation

user = SiteUser.objects.get(email='$email')
simulation = Simulation.objects.create(
    user_id=user,
    title='$title',
    description='$description',
    Softwares='$software'
)
simulation.save()
" | python3 manage.py shell
    echo "Simulation for $email created successfully."
done