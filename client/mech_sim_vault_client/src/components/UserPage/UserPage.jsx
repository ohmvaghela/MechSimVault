import React, { useEffect, useState } from "react";
import "./UserPage.css";
import Card from "../Cards/Card";
import { Link, useParams } from "react-router-dom";
import axios from "axios";
import { useBackendUrlContext, useUserContext, useUserDataContext } from "../../Context/Context";
import { tokenVerifier } from "../../Utils";

export default function UserPage() {
  const { id } = useParams();
  const [sims, setSims] = useState([]);
  const [ImageSrc, setImageSrc] = useState("");
  const [cardUser, setCardUser] = useState({});
  const [isUser, setIsUser] = useState(false);
  const { setUserData } = useUserDataContext();
  const {  setStat } = useUserContext();
  const { backendUrl } = useBackendUrlContext();

  function updateLocalStorage() {
    setStat(false);
    localStorage.removeItem("access_token");
    localStorage.removeItem("profile_picture");
    setUserData([]);
  }
  useEffect(() => {
    const sims_fetch = async () => {
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
          `${backendUrl}/sim/get_sim_by_id/${id}`
        );
        setSims(response.data);
      } catch (err) {
        console.log(err);
      }
    };
    sims_fetch();
    const user = JSON.parse(localStorage.getItem("userData"));
    if (user && user.id === Number(id)) setIsUser(true);
  }, [id]);

  useEffect(() => {}, []);

  useEffect(() => {
    const loadImage = async (name) => {
      const image = await fetchImage(`${backendUrl}${name}`);
      setImageSrc(image);
    };

    const userSet = async () => {
      try {
        const response = await axios.get(
          `${backendUrl}/siteUser/get_users_by_id/${id}`
        );
        // console.log("response.data", response.data);
        setCardUser(response.data);
        loadImage(response.data.profile_picture);
      } catch (err) {
        console.log(err);
      }
    };
    userSet();
  }, [id]);

  return (
    <div className="User-Page">
      <UserDetails user={cardUser} isUser={isUser} image={ImageSrc} />
      <UserSimulations sims={sims} />
    </div>
  );
}

function UserDetails(props) {
  return (
    <>
      <div className="User-Details">
        {/* change the default photo over here */}
        <img
          src={props.image || "/default_profile_photo.jpg"}
          className="User-Image"
          alt="User Profile"
        />
        <div className="User-Text-Details">
          <div className="User-Page-User-Name">{props.user.full_name}</div>
          <div className="User-Page-Desc">{props.user.bio}</div>
          <div className="User-Page-Softwares">{props.user.skills}</div>
        </div>

        <div className="User-Page-Upload">
          {props.isUser && (
            <Link to="/upload_sim">
              <button className="User-Page-Upload-Button">
                Upload <br /> Simulation
              </button>
            </Link>
          )}
        </div>
      </div>
    </>
  );
}

function UserSimulations(props) {
  return (
    <>
      <div className="Cards-container">
        {props.sims.map((sim) => (
          <Card key={sim.id} sim={sim} />
        ))}
      </div>
    </>
  );
}

const fetchImage = async (url) => {
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
