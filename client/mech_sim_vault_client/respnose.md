## Login

POST http://localhost:8000/siteUser/login_user/
Content-Type: application/json

{
  "email":"newuser1@example.com",
  "password":"ohm123ohm"
}


HTTP/1.1 200 OK
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Set-Cookie: refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNDQ3MzkxMiwiaWF0IjoxNzI0Mzg3NTEyLCJqdGkiOiIwZDcxZWY3YTQxOTA0MDE2OGU3MTMwZWMzYWY2NWIyZCIsInVzZXJfaWQiOjJ9.ggUMCJ7BvITV_7ctZaI6pkrjttPQFs_DlItZzxrBgTU; HttpOnly; Path=/; SameSite=Strict; Secure

{
  "message": "Login successful",
  "user": "newuser1@example.com",
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI0MzkwNTEyLCJpYXQiOjE3MjQzODc1MTIsImp0aSI6IjM1ZTkwOWU0YTgwNjQ0MDM5NzQ4ODI2YzJhN2UxNDg1IiwidXNlcl9pZCI6Mn0.rjO01nDrgUMBXQM04HcwB9Edc7jU_5OSL_7wqUoXw2A"
}

## Get sim
GET http://localhost:8000/sim/get_sim/

Content-Type: application/json

HTTP/1.1 200 OK
Date: Fri, 23 Aug 2024 04:34:51 GMT
Server: WSGIServer/0.2 CPython/3.10.12
Content-Type: application/json
Vary: Accept
Allow: GET, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 1612
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin

[
  {
    "id": 52,
    "upload_date": "2024-08-22",
    "likes": 0,
    "dislikes": 0,
    "title": "first simulation",
    "description": "first simulation description",
    "Softwares": "ansys",
    "simulation_image": "/media/simulations/sim1_image.png",
    "zip_file": "/media/simulations/sim1.zip",
    "zip_photos": "/media/simulations/sim2.zip",
    "user_id": 2
  },
]