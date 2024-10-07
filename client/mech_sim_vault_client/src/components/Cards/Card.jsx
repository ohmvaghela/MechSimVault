import React, { useEffect, useState } from "react";
import "./Cards.css";
import Button from "react-bootstrap/Button";
import OverlayTrigger from "react-bootstrap/OverlayTrigger";
import Tooltip from "react-bootstrap/Tooltip";
import "bootstrap/dist/css/bootstrap.min.css";
import { Link } from "react-router-dom";
import axios from "axios";
import { render } from "@testing-library/react";
import { useBackendUrlContext } from "../../Context/Context";

export default function Card(props) {
  const [imageSrc, setImageSrc] = useState("");
  const { backendUrl } = useBackendUrlContext();

  useEffect(() => {
    const loadImage = async () => {
      const image = await fetchImage(`${backendUrl}${props.sim.simulation_image}`);
      setImageSrc(image);
    };
    loadImage();
  }, []);

  return (
    <div className="Card">

      <Link to={`/simulation/${props.sim.id}`} className="Card-Title">
      <img className="Card-img" src={imageSrc} />
      </Link>
      <Link to={`/simulation/${props.sim.id}`} className="Card-Title">
        {props.sim.title}
      </Link>
      <Link to={`/userpage/${props.sim.user_id}`} className="Card-Name">By Someone</Link>
      <div className="Card-Value">
        <Thumbsup likes={props.sim.likes}/>
        <Downloads />
        <Comments />
      </div>
      <hr/>
      <div className="Card-Software">
      Software : {props.sim.Softwares}

      </div>
    </div>
  );
}
export function Downloads() {
  const renderTooltip = (props) => (
    <Tooltip id="button-tooltip" {...props}>
      Downloads
    </Tooltip>
  );

  return (
    <OverlayTrigger
      placement="bottom"
      delay={{ show: 50, hide: 50 }}
      overlay={renderTooltip}
    >
      <div className="Emotes">
        <i className="fas fa-download"></i> 
      </div>
    </OverlayTrigger>
  );
}
export function Thumbsup(props) {
  const renderTooltip = (props) => (
    <Tooltip id="button-tooltip" {...props}>
      Likes
    </Tooltip>
  );

  return (
    <OverlayTrigger
      placement="bottom"
      delay={{ show: 50, hide: 50 }}
      overlay={renderTooltip}
    >
      <div className="Emotes">
        <i className="fas fa-thumbs-up"></i> {props.likes}
      </div>
    </OverlayTrigger>
  );
}
export function Comments() {
  const renderTooltip = (props) => (
    <Tooltip id="button-tooltip" {...props}>
      Comment
    </Tooltip>
  );

  return (
    <OverlayTrigger
      placement="bottom"
      delay={{ show: 50, hide: 50 }}
      overlay={renderTooltip}
    >
      <div className="Emotes">
        <i className="fas fa-comment"></i> 
      </div>
    </OverlayTrigger>
  );
}

const fetchImage = async(url)=>{
  try{
    const response = await fetch(url);
    const blob = await response.blob();
    const simimage = await new Promise((resolve,reject)=>{
      const reader = new FileReader();
      reader.onloadend = ()=> resolve(reader.result);
      reader.onerror = reject;
      reader.readAsDataURL(blob);
    });
    return simimage;
  }catch(error){
    console.error('error fetching image',error);
  }
}