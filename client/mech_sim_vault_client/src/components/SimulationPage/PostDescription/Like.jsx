import React, { useEffect, useState } from 'react';
import OverlayTrigger from "react-bootstrap/OverlayTrigger";
import Tooltip from "react-bootstrap/Tooltip";
import Alert from "react-bootstrap/Alert";
import "bootstrap/dist/css/bootstrap.min.css";
import { useBackendUrlContext, useUserContext } from '../../../Context/Context';
import "../SimulationPage.css";
import axios from 'axios';

export default function Like(props) {
  const { stat } = useUserContext();
  const [showAlert, setShowAlert] = useState(false);
  const [likes, setLikes] = useState(0);
  const [likesTrigger, setLikesTrigger] = useState(false);
  const { backendUrl } = useBackendUrlContext();

  const renderTooltip = (props) => (
    <Tooltip id="button-tooltip" {...props}>
      Like
    </Tooltip>
  );

  const handleLikeClick = async () => {
    if (stat) {
      const userId = JSON.parse(localStorage.getItem("userData")).id;
      const url = `${backendUrl}/sim/add_likes/${userId}/${props.sim_id}/`;

      try {
        const response = await fetch(url, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
        });

        if (response.ok) {
          console.log("Like added successfully");
          setLikesTrigger(prev => !prev); // Toggle the trigger state
        } else {
          console.error("Failed to add like");
        }
      } catch (error) {
        console.error("Error:", error);
      }
    } else {
      setShowAlert(true);
      setTimeout(() => setShowAlert(false), 2000); // Hide alert after 2 seconds
    }
  };

  const updateLikes = async () => {
    try {
      const response = await axios.get(`${backendUrl}/sim/get_likes_by_sim/${props.sim_id}`);
      setLikes(response.data.likes);
      console.log(response.data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    setLikes(props.likes);
  }, [props.likes]);

  useEffect(() => {
    if (props.sim_id) {
      updateLikes();
    }
  }, [likesTrigger, props.sim_id]);

  return (
    <>
      {showAlert && (
        <Alert variant="danger" onClose={() => setShowAlert(false)} dismissible>
          You need to be logged in to like.
        </Alert>
      )}
      <OverlayTrigger
        placement="bottom"
        delay={{ show: 50, hide: 50 }}
        overlay={renderTooltip}
      >
        <div className="flexBox-element" onClick={handleLikeClick}>
          <i className="fas fa-thumbs-up"></i>
          {likes}
        </div>
      </OverlayTrigger>
    </>
  );
}
