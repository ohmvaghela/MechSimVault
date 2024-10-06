#!/bin/bash

# Perform login and extract tokens
login_response=$(curl -s -D - -X POST http://localhost:8000/siteUser/login_user/ \
  -H "Content-Type: application/json" \
  -d '{"email":"newuser1@example.com", "password":"ohm123ohm"}')

login_status=$(echo "$login_response" | grep HTTP | awk '{print $2}')
login_body=$(echo "$login_response" | sed -n '/{/,/}/p')

# Extract refresh_token from headers, accounting for arbitrary spaces
refresh_token=$(echo "$login_response" | grep -oP 'Set-Cookie:\s*refresh_token=\K[^;]*')

if [ "$login_status" -eq 200 ]; then
  access_token=$(echo "$login_body" | jq -r '.access_token')

  echo "- Login successful."

  # Perform the update data request using the access_token
  update_response=$(curl -s -w "\n%{http_code}" -X POST http://localhost:8000/siteUser/update/ \
    -H "Authorization: Bearer $access_token" \
    -H "Content-Type: application/json" \
    -d '{"full_name":"ohm N vaghela"}')

  update_status=$(echo "$update_response" | tail -n1)
  update_body=$(echo "$update_response" | sed '$d')

  if [ "$update_status" -eq 202 ]; then
    echo "- Update successful."
  else
    echo "Update failed. Status code: $update_status"
    echo "Response: $update_body"
  fi

  # Refresh JWT Token
  refresh_response=$(curl -s -w "\n%{http_code}" -X POST http://localhost:8000/api/token/refresh/ \
    -H "Content-Type: application/json" \
    -d "{\"refresh\": \"$refresh_token\"}")

  refresh_status=$(echo "$refresh_response" | tail -n1)
  refresh_body=$(echo "$refresh_response" | sed '$d')

  if [ "$refresh_status" -eq 200 ]; then
    new_access_token=$(echo "$refresh_body" | jq -r '.access')
    echo "- Token refresh successful."
    access_token=$new_access_token
  else
    echo "Token refresh failed. Status code: $refresh_status"
    echo "Response: $refresh_body"
  fi

  # Get simulations
  simulations_response=$(curl -s -w "\n%{http_code}" -X GET http://localhost:8000/sim/get_sim/ \
    -H "Content-Type: application/json")

  simulations_status=$(echo "$simulations_response" | tail -n1)
  simulations_body=$(echo "$simulations_response" | sed '$d')

  if [ "$simulations_status" -eq 200 ]; then
    echo "- Simulation fetch successful."
  else
    echo "Simulation fetch failed. Status code: $simulations_status"
    echo "Response: $simulations_body"
  fi

  # Get simulations by ID
  sim_by_id_response=$(curl -s -w "\n%{http_code}" -X GET http://localhost:8000/sim/get_sim_by_id/1 \
    -H "Content-Type: application/json")

  sim_by_id_status=$(echo "$sim_by_id_response" | tail -n1)
  sim_by_id_body=$(echo "$sim_by_id_response" | sed '$d')

  if [ "$sim_by_id_status" -eq 200 ]; then
    echo "- Simulation fetch by ID successful."
  else
    echo "Simulation fetch by ID failed. Status code: $sim_by_id_status"
    echo "Response: $sim_by_id_body"
  fi

  # Add simulations
  add_sim_response=$(curl -s -w "\n%{http_code}" -X POST http://localhost:8000/sim/add_sim/ \
    -H "Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW" \
    -H "Authorization: Bearer $access_token" \
    -F "title=first simulation" \
    -F "description=first simulation description" \
    -F "Softwares=ansys" \
    -F "simulation_image=@./ztestdata/photos/sim1_image.png" \
    -F "zip_file=@./ztestdata/sims/sim1.zip" \
    -F "zip_photos=@./ztestdata/sims/sim1.zip")

  add_sim_status=$(echo "$add_sim_response" | tail -n1)
  add_sim_body=$(echo "$add_sim_response" | sed '$d')

  if [ "$add_sim_status" -eq 201 ]; then
    echo "- Add simulation successful."
  else
    echo "Add simulation failed. Status code: $add_sim_status"
    echo "Response: $add_sim_body"
  fi

else
  echo "Login failed. Status code: $login_status"
  echo "Response: $login_body"
fi
