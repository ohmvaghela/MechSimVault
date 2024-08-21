#!/bin/bash

# Create a Python script to print all comments
echo "
from userComments.models import Comments

comments = Comments.objects.all()

for comment in comments:
    print(f'Comment by {comment.user_id.email} on {comment.simulation_id.title}: {comment.message}')
" > print_comments.py

# Run the Python script using Django shell
python3 manage.py shell < print_comments.py

# Clean up by removing the temporary Python script
rm print_comments.py
