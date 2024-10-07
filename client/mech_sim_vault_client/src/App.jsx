import "./App.css";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Navbar from "./components/Navbar/Navbar";
import Cards from "./components/Cards/Cards";
import SimulationPage from "./components/SimulationPage/SimulationPage";
import UserPage from "./components/UserPage/UserPage";
import Sign from "./components/Sign/Sign";
import SimulationUpload from "./components/SimulationUpload/SimulationUpload";
import { useState, useEffect } from "react";
import {
  UserStateContext,
  UserDataContext,
  BackendUrlContext
} from "./Context/Context";
import axios from "axios";
import { fetchAndSetImage } from "./OtherFn";

axios.defaults.withCredentials = true;

const browserRouter = createBrowserRouter([
  {
    path: "/",
    element: <Navbar />,
    children: [
      {
        path: "/",
        element: <Cards />,
      },
      {
        path: "/Simulation/:id",
        element: <SimulationPage />,
      },
      {
        path: "/UserPage/:id",
        element: <UserPage />,
      },
      {
        path: "/Sign",
        element: <Sign />,
      },
      {
        path: "/upload_sim",
        element: <SimulationUpload />,
      },
    ],
  },
]);

function App() {
  const [backendUrl, setBackendUrl] = useState("http://localhost:8000");
  const [stat, setStat] = useState(() => {
    const savedStat = localStorage.getItem("stat");
    return savedStat !== null ? JSON.parse(savedStat) : false;
  });
  const [userData, setUserData] = useState(() => {
    const savedUserData = localStorage.getItem("userData");
    return savedUserData !== null ? JSON.parse(savedUserData) : [];
  });

  useEffect(() => {
    localStorage.setItem("stat", JSON.stringify(stat));
  }, [stat]);

  useEffect(() => {
    localStorage.setItem("userData", JSON.stringify(userData));
    if (Object.keys(userData).length !== 0) {
      const imageUrl = `${backendUrl}${userData.profile_picture}`;
      fetchAndSetImage(imageUrl);
    }
  }, [userData, backendUrl]);

  return (
    <BackendUrlContext.Provider value={{ backendUrl, setBackendUrl }}>
      <UserStateContext.Provider value={{ stat, setStat }}>
        <UserDataContext.Provider value={{ userData, setUserData }}>
          <RouterProvider router={browserRouter} />
        </UserDataContext.Provider>
      </UserStateContext.Provider>
    </BackendUrlContext.Provider>
  );
}

export default App;
