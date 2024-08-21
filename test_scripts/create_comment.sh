#!/bin/bash

# Define comment details
comments=(
    "user1@example.com|Simulation Title 4|This is a comment for simulation 1"
    "user2@example.com|Simulation Title 3|This is a comment for simulation 2"
    "user3@example.com|Simulation Title 2|This is a comment for simulation 3"
    "user4@example.com|Simulation Title 1|This is a comment for simulation 4"
    "user5@example.com|Simulation Title 5|This is a comment for simulation 5"
)

# Create comments using Django shell
for comment in "${comments[@]}"; do
    IFS='|' read -r email sim_title message <<< "$comment"
    echo "
from siteUser.models import SiteUser
from simulations.models import Simulation
from userComments.models import Comments

user = SiteUser.objects.get(email='$email')
simulation = Simulation.objects.get(title='$sim_title')

comment = Comments.objects.create(
    user_id=user,
    simulation_id=simulation,
    message='$message'
)
comment.save()
" | python3 manage.py shell
    echo "Comment added for $email on $sim_title."
done
