import axios from 'axios';
import React, { useEffect, useState } from 'react'
import AddComment from './AddComment';
import { Link } from 'react-router-dom';
import { fetchImage } from '../../../Utils';
import "../SimulationPage.css"
import { useBackendUrlContext } from '../../../Context/Context';

export default function Comment(props) {
  const [comments, setComments] = useState([]);
  const { backendUrl } = useBackendUrlContext();
  const [commentAdd, setCommentAdd] = useState(false);
  const fetchUserDetails = async (userId) => {
    try {
      const userResponse = await axios.get(
        `${backendUrl}/siteUser/get_users_by_id/${userId}/`
      );
      const user = userResponse.data;
      const fetchurl = `${backendUrl}${user.profile_picture}/`;
      // const profilePicResponse = await axios.get(fetchurl);
      // const profilePicture = profilePicResponse.data;
      const profilePicture = await fetchImage(fetchurl);

      return {
        full_name: user.full_name,
        profile_picture: profilePicture,
      };
    } catch (e) {
      console.error(
        `Error fetching user details or profile picture for user ${userId}:`,
        e
      );
      return null;
    }
  };
  const getComments = async (comment_id) => {
    try {
      const response = await axios.get(
        `${backendUrl}/comment/get_comments_by_sim/${comment_id}/`
      );
      const comments = response.data;

      const updatedComments = await Promise.all(
        comments.map(async (comment) => {
          
          const userDetails = await fetchUserDetails(comment.user);
          if (userDetails) {
            return {
              ...comment,
              full_name: userDetails.full_name,
              profile_picture: userDetails.profile_picture,
            };
          }
          return comment;
        })
      );

      setComments(updatedComments);
    } catch (e) {
      console.error(e);
    }
  };

  useEffect(()=>{
    if(props.sim.id){
      getComments(props.sim.id)
    }
  },[props.sim.id])

  useEffect(()=>{
    if(props.sim.id && commentAdd===true){
      getComments(props.sim.id)
      setCommentAdd(false);
    }

  },[commentAdd])

  return (
    <>
      <div className="Comment-Section">
        <div className="Comment-Count">
          Comment({Object.keys(comments).length})
        </div>
        <AddComment comment_id={props.sim.id} setCommentAdd={setCommentAdd}/>
        <hr />

        {comments.map((comment) => (
          <React.Fragment key={comment.id}>
            <div className="Comment">
              <Link to={`/UserPage/${comment.user}`}>
                <img
                  className="comment-user-image"
                  src={comment.profile_picture || `/default_profile_photo.jpg`}
                  alt="Profile"
                />
              </Link>
              <Link className="Link-user-name" to={`/UserPage/${comment.user}`}>
                <div className="comment-user-name">{comment.full_name}</div>
              </Link>
              <div className="comment-description">{comment.message}</div>
              <div className="comment-date">{comment.date}</div>
            </div>
            <hr />
          </React.Fragment>
        ))}
      </div>
    </>
  );
}