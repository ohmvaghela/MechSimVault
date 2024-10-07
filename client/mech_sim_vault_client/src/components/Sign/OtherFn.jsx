import React from "react";
import "./Sign.css"

export function AlertFn({ alertVal, setAlertVal }) {
  if (alertVal) {
    return (
      <div className="alert">
        <div>Email ID is already registered please try to login</div>
        <button className="closebutton" onClick={() => setAlertVal(false)}>
          X
        </button>
      </div>
    );
  } else return null;
}

export function Loader({ loader }) {
  if (loader) {
    return (
      <div className="loader-block">
        <div className="loader"></div>
      </div>
    );
  } else return null;
}
