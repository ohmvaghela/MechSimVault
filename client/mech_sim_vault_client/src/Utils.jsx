import axios from 'axios';
import React from 'react'

export const fetchImage = async (url) => {

  try {
    const response = await fetch(url);
    const blob = await response.blob();
    const simimage = await new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onloadend = () => resolve(reader.result);
      reader.onerror = reject;
      reader.readAsDataURL(blob);
    });
    return simimage;
  } catch (error) {
    console.error("error fetching image", error);
  }
};

export async function tokenVerifier(backendUrl) {
 
  const token = localStorage.getItem('access_token');
  if (token) {
    try {
      const response = await axios.post(`${backendUrl}/token_verifier/token_verify/`, { token: token });
      if (response.data.access) {
        localStorage.setItem('access_token', response.data.access);
      }
      return true;
    } catch (err) {
      console.log('Token verification or refresh failed', err);
      return false;
    }
  } else {
    console.log('No access token available');
    return false;
  }
}

