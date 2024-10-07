import React from "react";
import Dropdown from "react-bootstrap/Dropdown";
import "bootstrap/dist/css/bootstrap.min.css";
import "./Navbar.css"
export function SortDrop() {
  return (
    <>
      <Dropdown className="SortDrop">
        <Dropdown.Toggle  id="SortDrop-toggle">Sort By</Dropdown.Toggle>
        <Dropdown.Menu className="SortDrop-Menu">
          <Dropdown.Item className="SortDrop-Item" to="/" >
            Recent
          </Dropdown.Item>
          <Dropdown.Item className="SortDrop-Item" to="/Dashboard" >
            Likes 
          </Dropdown.Item>
        </Dropdown.Menu>
      </Dropdown>
    </>
  );
}

export function SoftwareDrop() {
  return (
    <>
      <Dropdown className="SoftwareDrop">
        <Dropdown.Toggle id="SoftwareDrop-toggle">Software</Dropdown.Toggle>
        <Dropdown.Menu className="SoftwareDrop-Menu">
          <Dropdown.Item className="SoftwareDrop-Item" to="/" >
            Ansys
          </Dropdown.Item>
          <Dropdown.Item className="SoftwareDrop-Item" to="/Dashboard" >
            Abaqus 
          </Dropdown.Item>
          <Dropdown.Item className="SoftwareDrop-Item" to="/" >
            Comsol
          </Dropdown.Item>
        </Dropdown.Menu>
      </Dropdown>
    </>
  );
}