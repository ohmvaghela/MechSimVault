import React, { useState } from 'react'
import { useBackendUrlContext, useUserContext } from '../../../Context/Context';
import axios from 'axios';
import Alert from "react-bootstrap/Alert";
import "bootstrap/dist/css/bootstrap.min.css";
import "../SimulationPage.css"

export default function AddComment(props) {
  const { stat } = useUserContext();
  const [commentText, setCommentText] = useState("");
  const [showAlert, setShowAlert] = useState(false);
  const { backendUrl } = useBackendUrlContext();

  const handleComment = async (e) => {
    e.preventDefault();
    const token = localStorage.getItem("access_token");
    try {
      const response = await axios.post(
        `${backendUrl}/comment/add_comment/${props.comment_id}/`,
        { message: commentText },
        {
          headers: {
            Authorization: `Bearer ${token}`, 
            "Content-Type": "application/json",
          },
          withCredentials: true,
        }
      );
      console.log(response.data);
      setShowAlert(true);
      setCommentText(""); 
      props.setCommentAdd(true);
      setTimeout(() => setShowAlert(false), 2000); 
    } catch (err) {
      console.error(err);
    }
  };
  if (stat) {
    const profile_picture = localStorage.getItem("profile_picture");
    return (
      <>
        {showAlert && (
          <Alert
            variant="success"
            onClose={() => setShowAlert(false)}
            dismissible
          >
            Comment added successfully!
          </Alert>
        )}
        <form className="add-comments" onSubmit={handleComment}>
          <img
            className="add-comment-image"
            src={profile_picture || "/default_profile_photo.jpg"}
            // src="/sim3.jpg"
          />
          <textarea
            className="add-comment-input"
            value={commentText}
            onChange={(e) => setCommentText(e.target.value)}
            placeholder="Add your comment here..."
          />
          <button className="add-comment-button" type="submit">
            comment
          </button>
        </form>
      </>
    );
  } else {
    return (
      <div className="pre-comment-alert">Please Login Before Commenting</div>
    );
  }
}
