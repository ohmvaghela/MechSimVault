import React, { useEffect, useState } from "react";
import Card from "./Card";
import axios from "axios";
import { tokenVerifier } from "../../Utils";
import { useBackendUrlContext, useUserContext, useUserDataContext } from "../../Context/Context";

export default function Cards() {
  const { backendUrl } = useBackendUrlContext();
  const [sims, setSims] = useState([]);
  const { userData, setUserData } = useUserDataContext();
  const { stat, setStat } = useUserContext();

  function updateLocalStorage() {
    setStat(false);
    localStorage.removeItem("access_token");
    localStorage.removeItem("profile_picture");
    setUserData([]);
  }

  useEffect(() => {
    const sims_fetch = async () => {
      try {
        const isTokenValid = await tokenVerifier(backendUrl);
        if (!isTokenValid) {
          updateLocalStorage();
        }
      } catch (err) {
        console.log("Error verifying token", err);
      }

      try {
        const response = await axios.get(`${backendUrl}/sim/get_sim/`);
        setSims(response.data);
      } catch (err) {
        console.log(err);
      }
    };
    sims_fetch();
  }, [backendUrl]);

  return (
    <div className="Cards-container">
      {sims.map((sim) => (
        <Card key={sim.id} sim={sim} />
      ))}
    </div>
  );
}
