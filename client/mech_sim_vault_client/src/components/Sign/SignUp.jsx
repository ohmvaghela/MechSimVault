import React, {  useState, useRef } from "react";
import "./Sign.css";

import "bootstrap/dist/css/bootstrap.min.css";
import validator from "validator";
import axios from "axios";
// import { useUserDataContext, useUserStatContext } from "../../Context/Context";

import { useNavigate } from "react-router-dom";
import { useBackendUrlContext, useUserContext, useUserDataContext } from "../../Context/Context";

const defaultVal = {
  email:"",
  password:"",
  full_name:"",
  bio:"",
  institution:"",
  role:"",
  country:"",
  contact_info:"",
  skills:"",
};
export default function SignUp({setAlertVal,setLoader}) {
  const { backendUrl } = useBackendUrlContext();

  const navigate = useNavigate(); 
  const {stat,setStat} = useUserContext();
  const {userData,setUserData} = useUserDataContext();

  const [signUp, setSignUp] = useState({
    email:"",
    password:"",
    full_name:"",
    bio:"",
    institution:"",
    role:"",
    country:"",
    contact_info:"",
    skills:"",
  });
  const formRef = useRef(null);
  const signUpUser = async () => {
    // setLoader(true);
    await axios
    .post(`${backendUrl}/siteUser/create_user/`, signUp)
    // .post("https://autobilling-gu29.onrender.com/addUser",signUp)
    .then((data) => {
      console.log(data);
      if(data.data[0] === false){
          setAlertVal(true);
        }
        localStorage.setItem("access_token", data.data.access_token);
        setUserData(data.data.user);
        // setLoader(false);
        setStat(true);
        navigate("/")
      })
      .catch((err) => {
        console.log(err);
        // setLoader(false);
      });
      
  };
  const handleClick = (e) => {
    e.preventDefault();
    if (!validator.isEmail(signUp.email)) {
      formRef.current.reportValidity();
      console.log("email not valid");
      setSignUp(defaultVal);
    } 
    else if (formRef.current.checkValidity()) {
      console.log("Form is valid");
      signUpUser();
      setSignUp(defaultVal);
    }
    else {
      console.log("form invalid");
      formRef.current.reportValidity();
      setSignUp(defaultVal);
    }
  };
  return (
    <>
      <label className="slider signup" htmlFor="chk">
        SignUp
      </label>
      <form className="signUpForm" ref={formRef}>
        <input
          value={signUp.full_name}
          onChange={(e) => {
            setSignUp({ ...signUp, full_name: e.target.value });
          }}
          className="form"
          type="text"
          name="shopname"
          placeholder="full_name"
          maxLength={15}
          minLength={3}
          required
        />
        <input
          value={signUp.email}
          onChange={(e) => {
            setSignUp({ ...signUp, email: e.target.value });
          }}
          className="form"
          type="email"
          name="email"
          placeholder="Email ID"
          required
        />
        <input
          value={signUp.institution}
          onChange={(e) => {
            setSignUp({ ...signUp, institution: e.target.value });
          }}
          className="form"
          type="text"
          name="institution"
          placeholder="institution"
          maxLength={100}
          required
        />
        <input
          value={signUp.role}
          onChange={(e) => {
            setSignUp({ ...signUp, role: e.target.value });
          }}
          className="form"
          type="text"
          name="role"
          placeholder="role"
          maxLength={100}
          required
        />
        <input
          value={signUp.country}
          onChange={(e) => {
            setSignUp({ ...signUp, country: e.target.value });
          }}
          className="form"
          type="text"
          name="country"
          placeholder="country"
          maxLength={100}
          required
        />
        <input
          value={signUp.contact_info}
          onChange={(e) => {
            setSignUp({ ...signUp, contact_info: e.target.value });
          }}
          className="form"
          type="integer"
          name="contact_info"
          placeholder="contact_info"
          required
        />
        <input
          value={signUp.password}
          onChange={(e) => {
            setSignUp({ ...signUp, password: e.target.value });
          }}
          className="form"
          type="password"
          name="password"
          placeholder="password"
          required
        />
        <button className="signUpButton" 
        onClick={handleClick}
        >
          Sign Up
        </button>
      </form>
    </>
  );
}
