#!/bin/bash

# Define sub-comment details
sub_comments=(
    "user1@example.com|1|This is a sub-comment for comment 1"
    "user2@example.com|2|This is a sub-comment for comment 2"
    "user3@example.com|3|This is a sub-comment for comment 3"
    "user4@example.com|4|This is a sub-comment for comment 4"
    "user5@example.com|5|This is a sub-comment for comment 5"
)

# Create sub-comments using Django shell
for sub_comment in "${sub_comments[@]}"; do
    IFS='|' read -r email comment_id message <<< "$sub_comment"
    echo "
from siteUser.models import SiteUser
from userComments.models import Comments
from subComments.models import SubComments

user = SiteUser.objects.get(email='$email')
comment = Comments.objects.get(id=$comment_id)

sub_comment = SubComments.objects.create(
    user_id=user,
    comment_id=comment,
    message='$message'
)
sub_comment.save()
" | python3 manage.py shell
    echo "Sub-comment added by $email on comment $comment_id."
done
