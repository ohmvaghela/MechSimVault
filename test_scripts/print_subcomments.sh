#!/bin/bash

# Create a Python script to print all sub-comments
echo "
from subComments.models import SubComments

sub_comments = SubComments.objects.all()

for sub_comment in sub_comments:
    print(f'Sub-comment by {sub_comment.user_id.email} on comment {sub_comment.comment_id.id}: {sub_comment.message} at {sub_comment.date}')
" > print_sub_comments.py

# Run the Python script using Django shell
python3 manage.py shell < print_sub_comments.py

# Clean up by removing the temporary Python script
rm print_sub_comments.py
