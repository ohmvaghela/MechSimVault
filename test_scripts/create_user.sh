#!/bin/bash

# Define user details
users=(
    "user1@example.com|User One|Bio for user one|Institution One|Role One|Country One|Contact Info One|Skill One, Skill Two"
    "user2@example.com|User Two|Bio for user two|Institution Two|Role Two|Country Two|Contact Info Two|Skill Three, Skill Four"
    "user3@example.com|User Three|Bio for user three|Institution Three|Role Three|Country Three|Contact Info Three|Skill Five, Skill Six"
    "user4@example.com|User Four|Bio for user four|Institution Four|Role Four|Country Four|Contact Info Four|Skill Seven, Skill Eight"
    "user5@example.com|User Five|Bio for user five|Institution Five|Role Five|Country Five|Contact Info Five|Skill Nine, Skill Ten"
)

# Create users using Django shell
for user_data in "${users[@]}"; do
    IFS='|' read -r email full_name bio institution role country contact_info skills <<< "$user_data"
    echo "
from siteUser.models import SiteUser

site_user = SiteUser.objects.create(
    email='$email',
    full_name='$full_name',
    bio='$bio',
    institution='$institution',
    role='$role',
    country='$country',
    contact_info='$contact_info',
    skills='$skills'
)
site_user.set_password('ohm123ohm')
site_user.save()
" | python3 manage.py shell
    echo "User $email created."
done
