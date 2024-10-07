import React, { useEffect,useState } from 'react'
import "../SimulationPage.css"
import { Navigation, Pagination, Scrollbar, A11y } from "swiper/modules";
import { Swiper, SwiperSlide } from "swiper/react";
// Import Swiper styles
import "swiper/css";
import "swiper/css/navigation";
import "swiper/css/pagination";
import "swiper/css/scrollbar";
import JSZip from 'jszip';
import "../SimulationPage.css"
import { useBackendUrlContext } from '../../../Context/Context';

export default function SlideShow(props) {
  const [images, setImages] = useState([]);
  const { backendUrl } = useBackendUrlContext();

  const fetchZipFile = async (url) => {
    try {

      const response = await fetch(url);
      const blob = await response.blob();
      const zip = await JSZip.loadAsync(blob);

      const imageFiles = [];
      zip.forEach((relativePath, file) => {
        if (/\.(png|jpe?g)$/i.test(file.name)) {
          imageFiles.push(file.async('blob').then(blob => URL.createObjectURL(blob)));
        }
      });

      const urls = await Promise.all(imageFiles)
      setImages(urls);
      
    } catch (error) {
      console.error('Error fetching or extracting ZIP file:', error);
    }
  };
  useEffect(() => {
    if (props.sim && props.sim.zip_photos) {
      const zip_photos_url = `${backendUrl}${props.sim.zip_photos}/`;
      fetchZipFile(zip_photos_url);
    }
  }, [props.sim]);

  return (
    <Swiper
      className="swiper"
      modules={[Navigation, Pagination, Scrollbar, A11y]}
      spaceBetween={50}
      slidesPerView={3}
      centeredSlides={true}
      navigation
      pagination={{ clickable: false }}
      scrollbar={{ draggable: false }}
      slideActiveClass="active-slide"
      slideNextClass="next-slide"
      slidePrevClass="prev-slide"
      onSwiper={(swiper) => console.log(swiper)}
      onSlideChange={() => console.log("slide change")}
    >
      {images.map((image, index) => (
        <SwiperSlide className="slide" key={index}>
          <img
            src={image}
            alt={`Slide ${index + 1}`}
            className="slide-image"
          />
        </SwiperSlide>
      ))}
    </Swiper>
  )
}
