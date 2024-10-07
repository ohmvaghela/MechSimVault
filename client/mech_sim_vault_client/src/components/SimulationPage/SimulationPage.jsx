import React, { useEffect, useState } from "react";

import "./SimulationPage.css";
import axios from "axios";
import SlideShow from "./SlideShow/SlideShow";
import PostDesciption from "./PostDescription/PostDescription";
import Comment from "./Comment/Comment";
import { useParams } from "react-router-dom";
import { tokenVerifier } from "../../Utils";
import { useBackendUrlContext, useUserContext, useUserDataContext } from "../../Context/Context";

// Function to dynamically import images from the public/animals directory
export default function SimulationPage() {
  const [sim, setSim] = useState([]);
  const { id } = useParams();
  const { setUserData } = useUserDataContext();
  const { setStat } = useUserContext();
  const { backendUrl } = useBackendUrlContext();

  function updateLocalStorage() {
    setStat(false);
    localStorage.removeItem("access_token");
    localStorage.removeItem("profile_picture");
    setUserData([]);
  }

  const fetchSimulation = async () => {
    tokenVerifier(backendUrl)
      .then((isTokenValid) => {
        if (!isTokenValid) {
          updateLocalStorage();
        }
      })
      .catch((err) => {
        console.log("Error verifying token", err);
      });
    try {
      const response = await axios.get(
        `${backendUrl}/sim/get_sim_by_simid/${id}`
      );
      setSim(response.data);
    } catch (err) {
      console.error(err);
    }
  };
  useEffect(() => {
    fetchSimulation();
  }, [id]);
  return (
    <>
      <div className="swiper-parent">
        <SlideShow sim={sim} />
      </div>
      <PostDesciption sim={sim} />
      <Comment sim={sim} />
    </>
  );
}
