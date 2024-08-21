from siteUser.models import SiteUser

users = [
    {
        "email": "user1@example.com",
        "full_name": "User One",
        "bio": "Bio for user one",
        "institution": "Institution One",
        "role": "Role One",
        "country": "Country One",
        "contact_info": "Contact Info One",
        "skills": "Skill One, Skill Two",
    },
    {
        "email": "user2@example.com",
        "full_name": "User Two",
        "bio": "Bio for user two",
        "institution": "Institution Two",
        "role": "Role Two",
        "country": "Country Two",
        "contact_info": "Contact Info Two",
        "skills": "Skill Three, Skill Four",
    },
    {
        "email": "user3@example.com",
        "full_name": "User Three",
        "bio": "Bio for user three",
        "institution": "Institution Three",
        "role": "Role Three",
        "country": "Country Three",
        "contact_info": "Contact Info Three",
        "skills": "Skill Five, Skill Six",
    },
    {
        "email": "user4@example.com",
        "full_name": "User Four",
        "bio": "Bio for user four",
        "institution": "Institution Four",
        "role": "Role Four",
        "country": "Country Four",
        "contact_info": "Contact Info Four",
        "skills": "Skill Seven, Skill Eight",
    },
    {
        "email": "user5@example.com",
        "full_name": "User Five",
        "bio": "Bio for user five",
        "institution": "Institution Five",
        "role": "Role Five",
        "country": "Country Five",
        "contact_info": "Contact Info Five",
        "skills": "Skill Nine, Skill Ten",
    },
]

for user_data in users:
    site_user = SiteUser.objects.create(
        email=user_data['email'],
        full_name=user_data['full_name'],
        bio=user_data['bio'],
        institution=user_data['institution'],
        role=user_data['role'],
        country=user_data['country'],
        contact_info=user_data['contact_info'],
        skills=user_data['skills']
    )
    site_user.set_password("ohm123ohm")
    site_user.save()

