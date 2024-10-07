import React, { useRef, useState } from "react";
import "./Sign.css";
import axios from "axios";
import validator from "validator";
// import { useUserDataContext, useUserStatContext } from "../../Context/Context";
import { useNavigate } from "react-router-dom";
import { useBackendUrlContext, useUserContext,useUserDataContext } from "../../Context/Context";

export default function LogIn({ setLoader }) {
  const { backendUrl } = useBackendUrlContext();

  const navigate = useNavigate();
  const { stat, setStat } = useUserContext();
  const {userData,setUserData} = useUserDataContext();
  const [login, setLogin] = useState({
    email: "",
    password: "",
  });
  const formRef = useRef(null);
  const loginFn = async () => {
    // console.log(login);
    // setLoader(true);
    await axios
      // .post("https://autobilling-gu29.onrender.com/loginUser",login)
      .post(`${backendUrl}/siteUser/login_user/`, login)
      .then((response) => {
        // console.log(response);
        setLoader(false);
        if (response.data === "Incorrect password") {
          console.log("incorrect password");
        } else {
          localStorage.setItem("access_token", response.data.access_token);
          
          setUserData(response.data.user);
          
          setStat(true);
          navigate("/");
        }
      })
      .catch((err) => {
        setLoader(false);
        // alert(err.response.data);
        console.log(["login error :", err]);
      });
  };
  const onClickHandle = async (e) => {
    e.preventDefault();
    if (formRef.current.checkValidity()) {
      // Form is valid, proceed with your logic
      console.log("Form is valid");
      loginFn();
    } else if (!validator.isEmail(login.email)) {
      formRef.current.reportValidity();
    } else {
      // Form is invalid, show validation errors
      formRef.current.reportValidity();
    }
  };
  return (
    <>
      <div className="loginBox">
        <label className="slider login" htmlFor="chk">
          Log In
        </label>
        <form className="loginForm" ref={formRef}>
          <input
            value={login.email}
            onChange={(e) => {
              setLogin({ ...login, email: e.target.value });
            }}
            className="form"
            type="email"
            name="email"
            placeholder="Email ID"
            required
          />
          <input
            value={login.password}
            onChange={(e) => {
              setLogin({ ...login, password: e.target.value });
            }}
            className="form"
            type="password"
            name="password"
            placeholder="password"
            required
          />
          <button className="loginButton" onClick={onClickHandle}>
            Login
          </button>
        </form>
      </div>
    </>
  );
}
