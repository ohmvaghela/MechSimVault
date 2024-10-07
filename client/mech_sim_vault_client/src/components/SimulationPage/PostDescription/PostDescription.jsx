import React, { useEffect, useState } from 'react'
import Like from './Like';
import Share from './Share';
import Download from './Download';
import axios from 'axios';
import { fetchImage } from '../../../Utils';
import { Link } from 'react-router-dom';
import "../SimulationPage.css"
import { useBackendUrlContext } from '../../../Context/Context';

export default function PostDesciption(props) {
  const [user, setUser] = useState([]);
  const [imageSrc, setImageSrc] = useState("");
  const { backendUrl } = useBackendUrlContext();

  const getUser = async (user_id) => {
    try {
      const resposne = await axios.get(
        `${backendUrl}/siteUser/get_users_by_id/${user_id}`
      );
      setUser(resposne.data);
      const fetchUrl = `${backendUrl}${resposne.data.profile_picture}/`;
      const image = await fetchImage(fetchUrl);
      setImageSrc(image);
  
    } catch (e) {
      console.error(e);
    }
  };
  useEffect(()=>{
    if(props.sim.user_id){
      getUser(props.sim.user_id);
    }
  },[props.sim])
  return (
    <>
      {/* {console.log("post props",props)} */}
      <div className="SimPage-Content">
        <div className="SimPage-Title">{props.sim.title}</div>
        <div className="User">
          <Link to={`/UserPage/${user.id}`}>
            <img src={imageSrc || "/default_profile_photo.jpg"} className="User-Photo" />
          </Link>
          <Link className="Link-user-name" to={`/UserPage/${user.id}`}>
            <div className="User-Name"> {user.full_name}</div>
          </Link>
          <div className="Post-creation">{props.sim.upload_date}</div>
          <div className="Post-modifier">
            <div className="Post-modifier">
              <Like likes={props.sim.likes} sim_id={props.sim.id} />
              <Share />
              <Download sim={props.sim} />
            </div>
          </div>
        </div>
        <div className="Post-Description">{props.sim.description}</div>
      </div>
    </>
  );
}

