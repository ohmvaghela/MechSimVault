import React from 'react'

// imageUtils.js

export const fetchAndSetImage = async (url) => {
  try {
    const response = await fetch(url);
    const blob = await response.blob();
    const base64Image = await new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onloadend = () => resolve(reader.result);
      reader.onerror = reject;
      reader.readAsDataURL(blob);
    });
    // You can now use the base64Image as needed
    localStorage.setItem('profile_picture', base64Image);
  } catch (error) {
    console.error('Error fetching and setting image:', error);
  }
};

