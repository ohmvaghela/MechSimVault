import React, { useState } from "react";
import axios from "axios";
import "./SimulationUpload.css"; // Import the CSS file
import { useNavigate } from "react-router-dom";
import Alert from "react-bootstrap/Alert";
import "bootstrap/dist/css/bootstrap.min.css";
import { useBackendUrlContext } from "../../Context/Context";

export default function SimulationUpload() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [softwares, setSoftwares] = useState("");
  const [simulationImage, setSimulationImage] = useState(null);
  const [zipFile, setZipFile] = useState(null);
  const [zipPhotos, setZipPhotos] = useState(null);
  const [showAlert, setShowAlert] = useState(false);
  const navigate = useNavigate();
  const { backendUrl } = useBackendUrlContext();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("title", title);
    formData.append("description", description);
    formData.append("Softwares", softwares);
    formData.append("simulation_image", simulationImage);
    formData.append("zip_file", zipFile);
    formData.append("zip_photos", zipPhotos);

    try {
      const token = localStorage.getItem("access_token");
      const response = await axios.post(
        `${backendUrl}/sim/add_sim/`,
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
            Authorization: `Bearer ${token}`,
          },
        }
      );
      console.log("Upload successful:", response.data);
      navigate("/");
    } catch (error) {
      if (error.response && error.response.status === 400) {
        console.error("Bad Request:", error.response.data);
      } else {
        console.error("Error uploading the simulation:", error);
      }
      setShowAlert(true);
      setTimeout(() => setShowAlert(false), 2000); // Hide alert after 2 seconds
    }
  };

  return (
    <div>
      {showAlert && (
        <Alert variant="danger" className="simupload-alert">
          Fail
        </Alert>
      )}
      <form onSubmit={handleSubmit} className="simupload-form">
        <div className="simupload-form-group">
          <label>Title:</label>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
        </div>
        <div className="simupload-form-group">
          <label>Description:</label>
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
          />
        </div>
        <div className="simupload-form-group">
          <label>Softwares:</label>
          <input
            type="text"
            value={softwares}
            onChange={(e) => setSoftwares(e.target.value)}
            required
          />
        </div>
        <div className="simupload-form-group">
          <label>Simulation Image:</label>
          <input
            type="file"
            onChange={(e) => setSimulationImage(e.target.files[0])}
            required
          />
        </div>
        <div className="simupload-form-group">
          <label>ZIP File:</label>
          <input
            type="file"
            onChange={(e) => setZipFile(e.target.files[0])}
            required
          />
        </div>
        <div className="simupload-form-group">
          <label>ZIP Photos:</label>
          <input
            type="file"
            onChange={(e) => setZipPhotos(e.target.files[0])}
            required
          />
        </div>
        <button type="submit" className="simupload-submit-button">
          Upload Simulation
        </button>
      </form>
    </div>
  );
}
