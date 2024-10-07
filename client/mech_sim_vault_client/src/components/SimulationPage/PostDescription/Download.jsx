import React from 'react'
import OverlayTrigger from "react-bootstrap/OverlayTrigger";
import Tooltip from "react-bootstrap/Tooltip";
import "bootstrap/dist/css/bootstrap.min.css";
import { saveAs } from "file-saver";
import "../SimulationPage.css"
import { useBackendUrlContext } from '../../../Context/Context';

export default function Download(props) {
  const { backendUrl } = useBackendUrlContext();

  const handleDownload = async ()=>{
    try{
      // console.log(props.sim);
      const url = `${backendUrl}${props.sim.zip_file}`
      const resposne = await fetch(url);
      const blob = await resposne.blob();
      saveAs(blob,url.substring(url.lastIndexOf('/')+1));
    }
    catch(e){
      console.error(e);
    }
  }
  const renderTooltip = (props) => (
    <Tooltip id="button-tooltip" {...props}>
      Download
    </Tooltip>
  );

  return (
    <OverlayTrigger
      placement="bottom"
      delay={{ show: 50, hide: 50 }}
      overlay={renderTooltip}
    >
      <div className="flexBox-element" onClick={handleDownload}>
        <i className="fas fa-download"></i>{" "}
      </div>
    </OverlayTrigger>
  );
}
