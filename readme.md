<h1 align="center">

 MechSimVault

</h1>

<div align='center'>

<img src="./readme_img/mech.svg" width=400/>

</div>

<h1 align="center">

Purpose

</h1>
<div align="center">

## - This is free cloud-based collaboration environment that helps engineering teams manage, view, and share simulations, similar to grabCAD but for sharing simulations

</div>

## Setting local django enviroment
- Django : `v5.1`
- Python `3.10.12`
- Setting env variables
  ```sh
  SECRET_KEY= # django secret key
  DEBUG=False # set True for testing | false for production
  ALLOWED_HOSTS=localhost,127.0.0.1 # add more based on requirement

  # If you are using PostgreSQL
  DATABASE_URL= # postgreSQL connection url

  # If you are using MYSQL db
  MYSQL_DATABASE= # set MYSQL_DATABASE
  MYSQL_USER= # set MYSQL_USER
  MYSQL_PASSWORD= # set MYSQL_PASSWORD
  MYSQL_HOST= # set MYSQL_HOST
  MYSQL_PORT= # set MYSQL_PORT

  # client port or url 
  CORS_ALLOWED_ORIGINS=http://localhost:3000,http://example.com
  ```
- Setup python virtual env 
  ```
  workon <python 3.10.12- virtual env name>
  ```
- Setting up model
  ```
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```
- Running server
  ```
  python3 manage.py runserver
  ```

## Testing for server
- Create user using the rest client code present in rest_client folder

  ```yaml
  ### Create 
  # POST http://localhost:8001/siteUser/create_user/
  POST https://mechsimvault.backend.vibevaulttech.co.in/siteUser/create_user/
  Content-Type: application/json

  {
    "email": "newuser1@example.com",
    "password": "ohm123ohm",
    "full_name": "New User",
    "bio": "This is a new user.",
    "institution": "Example Institution",
    "role": "Developer",
    "country": "INDIA",
    "contact_info": "1234567890",
    "skills": "Python, Django"
  }

  ```
- Alternate CURL request 
  ```
  curl -X POST \
    https://mechsimvault.backend.vibevaulttech.co.in/siteUser/create_user/ \
    -H 'Content-Type: application/json' \
    -d '{
      "email": "newuser1@example.com",
      "password": "ohm123ohm",
      "full_name": "New User",
      "bio": "This is a new user.",
      "institution": "Example Institution",
      "role": "Developer",
      "country": "INDIA",
      "contact_info": "1234567890",
      "skills": "Python, Django"
    }'
  ```
- Then run following in root dir
  > ### - Change the host url in the unitTest.sh 
 
  ```bash
  sudo chmod +x unitTest.sh
  ./unitTest.sh <url>
  # example uses
  ./unitTest.sh localhost:8000
  ./unitTest.sh my.domain.name
  ```
- If there is any issue with server it will popup
- For other API calls check for APIs present in rest_client

## Containerizing Application
- `Server`: From the root dir of repo run
  ```
  docker build -t <image-name>:<tag> .
  ```
  ```
  docker build -t ohmv10/mech-server:<tag> .
  ```
- `Client`: From the client dir of repo run
  ```
  docker build -t <image-name>:<tag> .
  ```
  ```
  docker build -t ohmv10/mech-client:<tag> .
  ```
  
## Running app locally using docker image 
- Docker compose (They are running on custom bridge network)
- Make sure "/home/docker-volume" exist and is empty and has appropriate permission
- Then run docker compose up
```yaml
version: '3.8'

services:
  mech-server:
    image: ohmv10/mech-server:v1.2
    ports:
      - "8000:8000"
    environment:
      SECRET_KEY: # SECRET_KEY 
      DEBUG: # DEBUG 
      ALLOWED_HOSTS: # ALLOWED_HOSTS 
      DATABASE_URL: # DATABASE_URL 
      CORS_ALLOWED_ORIGINS: # CORS_ALLOWED_ORIGINS 
      MYSQL_DATABASE: # MYSQL_DATABASE 
      MYSQL_USER: # MYSQL_USER 
      MYSQL_PASSWORD: # MYSQL_PASSWORD 
      MYSQL_HOST: # MYSQL_HOST 
      MYSQL_PORT: # MYSQL_PORT 
    networks:
      - mech-net

  mech-client:
    image: ohmv10/mech-client:v1.0
    ports:
      - "3000:3000"
    networks:
      - mech-net

  mysql:
    image: mysql:9.0.1
    container_name: mysql
    environment:
      MYSQL_ROOT_PASSWORD: password
      MYSQL_DATABASE: mech_sim_db
      MYSQL_USER: admin
      MYSQL_PASSWORD: password
    ports:
      - "3306:3306"
    volumes:
      - /home/docker-volume:/var/lib/mysql
    networks:
      - mech-net

volumes:
  mysql-data:
    driver: local

networks:
  mech-net:
    driver: bridge

```


# Hosting a containerized application using Kubernetes on Google Cloud 
- Secret files are not present in kubernetes folder
- Following is boiler plate code fill it with info
- Here I am assuming you have a domain and obtained a tls/ssl certificate
- Also reserve a static IP for both server and client
- The app wont work untill it is deployed on HTTPS as the CORS wont allow to attach cookies to the requests
- Add this file 
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mech-server-secret
type: Opaque
data:
  SECRET_KEY: # 64 byte encoding 

---

apiVersion: v1
kind: Secret
metadata:
  name: mysql-secret
type: Opaque
data:
  mysql-root-password: # 64 byte encoding 
  mysql-database: # 64 byte encoding 
  mysql-user: # 64 byte encoding 
  mysql-password: # 64 byte encoding 
```


# After adding these files if you want to auto

- If you are using GKE then directly run
```sh
# mode is gke or minikube
./create-cluster.sh <mode>
./create-cluster.sh gke
./create-cluster.sh minikube

```
> ### `gke` mode will automatically reserve static global ip in google cloud 
- If you are using minikube then change storageclass in `pvc.yaml`
```sh
  # from 
  
  storageClassName: standard-rwo
  # to 
  
  name: mech-server
  storageClassName: media-storageclass
  
  ---

  name: mysql-pvc
  storageClassName: mysql-storageclass
```

