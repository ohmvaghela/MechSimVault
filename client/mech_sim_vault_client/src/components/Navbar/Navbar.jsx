import React, { useEffect, useState } from "react";
import { Link, Outlet, useLocation, useNavigate } from "react-router-dom";
import "./Navbar.css";
import { SoftwareDrop, SortDrop } from "./OtherFn";
import { useUserContext, useUserDataContext } from "../../Context/Context";
import Dropdown from "react-bootstrap/Dropdown";
import "bootstrap/dist/css/bootstrap.min.css";

export default function Navbar() {
  const location = useLocation();

  return (
    <>
      <div className="Navbar">
        <Link to='/' className="HomeButtonLink">
        <div className="HomeButton">
          
          {/* <img className="Logo" src='logo.png'/> */}
          <span className="col1">Mech</span>
          <span className="col2">Sim</span>
          <span className="col1">Vault</span>
        </div>
        </Link>

        {location.pathname === "/" && <SearchBar />}
        {/* {location.pathname !== "/sign" && (
          <Link to="/sign" className="SiteUserLink">
          <div className="SiteUser">
            Login/SignUp
          </div>
          </Link>
        )} */}
        <SignToggle/>
      </div>

      <Outlet />
    </>
  );
}

function SearchBar() {
  return (
    <>
      <div className="Nav-seach-holder">
        <input className="Nav-search" type="text" placeholder="Search.." />
        <div className="Nav-search">
          <i className="fa fa-search"></i>
        </div>
        <SortDrop />
        <SoftwareDrop />
      </div>
    </>
  );
}

function SignToggle(){
  const {stat,setStat} = useUserContext();
  const [userLoggedIn,setUserLoggedIn] = useState(false);
  const location = useLocation();
  if(stat){
    return (

      <ProfileIcon/>
    )
  }
  else{
    return (
    <>
      {location.pathname !== "/sign" && (
        <Link to="/sign" className="SiteUserLink">
        <div className="SiteUser">
          Login/SignUp
        </div>
        </Link>
      )}
    </>
    )
  }
}

function ProfileIcon(){
  const {stat,setStat} = useUserContext();
  const {userData,setUserData} = useUserDataContext()
  const navigate = useNavigate();
  const [profileImage, setProfileImage] = useState("");

  useEffect(() => {
    // Retrieve the profile image from localStorage
    const storedImage = localStorage.getItem("profile_picture");
    if (storedImage) {
      setProfileImage(storedImage);
    }
  }, []);

  return(
    <>
      <Dropdown className="ProfileButton">
        <Dropdown.Toggle id="ProfileButton-Toggle">
          <img src={profileImage||'/default_profile_photo.jpg'} className="Profile-logo-image"/>
        </Dropdown.Toggle>
        <Dropdown.Menu className="ProfileButton-Dropdown">
          <Dropdown.Item as={Link} to="/" className="goHomepage">
            HomePage
          </Dropdown.Item>
          {/* change the link over here */}
          <Dropdown.Item as={Link} to={`/UserPage/${userData.id}`} className="goDashboard">
            DashBoard
          </Dropdown.Item>
          <Dropdown.Item>
            <button className="Logout-button"
              onClick={() => {
                setStat(false);
                localStorage.removeItem("access_token");
                localStorage.removeItem("profile_picture");
                setUserData([]);

                navigate("/");
              }}
            >
              Logout
            </button>
          </Dropdown.Item>
        </Dropdown.Menu>
      </Dropdown>
    
    </>
  );
}