import React, { useState } from 'react'
import OverlayTrigger from "react-bootstrap/OverlayTrigger";
import Tooltip from "react-bootstrap/Tooltip";
import Alert from "react-bootstrap/Alert";
import "bootstrap/dist/css/bootstrap.min.css";
import "../SimulationPage.css"

export default function Share() {
  const [showAlert, setShowAlert] = useState(false);

  const handleShareClick = () => {
    const currentUrl = window.location.href;
    navigator.clipboard
      .writeText(currentUrl)
      .then(() => {
        setShowAlert(true);
        setTimeout(() => setShowAlert(false), 2000);
      })
      .catch((err) => {
        console.error("Failed to copy: ", err);
      });
  };

  const renderTooltip = (props) => (
    <Tooltip id="button-tooltip" {...props}>
      Share
    </Tooltip>
  );

  return (
    <>
      {showAlert && (
        <Alert
          variant="success"
          onClose={() => setShowAlert(false)}
          dismissible
        >
          Link copied to clipboard!
        </Alert>
      )}
      <OverlayTrigger
        placement="bottom"
        delay={{ show: 50, hide: 50 }}
        overlay={renderTooltip}
      >
        <div className="flexBox-element" onClick={handleShareClick}>
          <i className="fas fa-share"></i>{" "}
        </div>
      </OverlayTrigger>
    </>
  );
}
