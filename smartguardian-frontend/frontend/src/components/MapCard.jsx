import { CrisisAlert } from '@mui/icons-material';
import { Stack, Typography } from '@mui/material';
import React, { useEffect, useRef } from 'react';
import ReactDOMServer from 'react-dom/server';
import mapboxgl from 'mapbox-gl';
// import MapboxGeocoder from '@mapbox/mapbox-gl-geocoder/lib/index';
import 'mapbox-gl/dist/mapbox-gl.css';
import '@mapbox/mapbox-gl-geocoder/lib/mapbox-gl-geocoder.css';
import './MapCard.css';

mapboxgl.accessToken = 'pk.eyJ1IjoiYXVicmV5bXV3YWxvIiwiYSI6ImNsdGIxZjVvcTFtdmUybW1zcG9jeHFmYmIifQ.hAa-71IJ_PvPa3S981-syw'; // Replace with your actual Mapbox access token

const MapComponent = () => {
  const mapContainer = useRef(null);
  const map = useRef(null);
  const markers = useRef({});

  const PopupContent = ({ student_name, alert }) => (
    <Stack pr={1} alignItems="center" spacing={1.5} direction="row">
      <Typography variant="body2">{student_name}</Typography>
      {/* <CrisisAlert sx={{ color: alert === "True" ? 'red' : '#1677ff' }} /> */}
        {/* <CrisisAlert sx={{ color: alert === "True" ? 'red' : '#1677ff' }} /> */}
    </Stack>
  );

  useEffect(() => {
    if (map.current) return; // Initialize map only once

    map.current = new mapboxgl.Map({
      container: mapContainer.current,
      style: 'mapbox://styles/mapbox/streets-v12',
      // style: 'mapbox://styles/aubreymuwalo/clx8l7q6n007c01pj2vea2sfo',

      // style: 'mapbox://styles/aubreymuwalo/clx7yizm701x701pn6dnrhhdd',

      center: [35.33802, -15.38853],
      zoom: 16
    });

    // map.current.addControl(new MapboxGeocoder({ accessToken: mapboxgl.accessToken, mapboxgl }));

    // Add controls to the map
    map.current.addControl(new mapboxgl.ScaleControl(), 'bottom-left');
    map.current.addControl(new mapboxgl.NavigationControl(), 'bottom-right');
    map.current.addControl(new mapboxgl.FullscreenControl(), 'bottom-right');
    map.current.addControl(new mapboxgl.GeolocateControl({ trackUserLocation: true }), 'bottom-right');

    const socket = new WebSocket('wss://eb5f-105-234-164-2.ngrok-free.app/ws/location_updates/');

    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      updateMarker(data);
    };

    socket.onopen = () => {
      console.log('WebSocket connection established');
    };

    socket.onclose = () => {
      console.log('WebSocket connection closed');
    };

    socket.onerror = (error) => {
      console.error('WebSocket error: ' + error);
    };

    const updateMarker = (data) => {
      const { phone_number, latitude, longitude, alert, student_name } = data;
      const lat = parseFloat(latitude);
      const lng = parseFloat(longitude);
      const isAlert = alert === "True";

      if (markers.current[phone_number]) {
        markers.current[phone_number].setLngLat([lng, lat]);

        const markerElement = markers.current[phone_number].getElement();
        if (isAlert) {
          markerElement.classList.add('alert');
        } else {
          markerElement.classList.remove('alert');
        }
      } else {
        const el = createMarkerElement(isAlert);
        const marker = new mapboxgl.Marker(el)
          .setLngLat([lng, lat])
          .setPopup(new mapboxgl.Popup().setHTML(
            ReactDOMServer.renderToString(<PopupContent student_name={student_name} alert={alert} />)
          ))
          .addTo(map.current);

        markers.current[phone_number] = marker;
      }

      markers.current[phone_number].lastUpdateTime = Date.now();
    };

    const createMarkerElement = (isAlert) => {
      const el = document.createElement('div');
      el.className = 'marker';
      if (isAlert) {
        el.classList.add('alert');
      }
      return el;
    };

    const checkMarkers = () => {
      const currentTime = Date.now();
      Object.keys(markers.current).forEach((phoneNumber) => {
        const marker = markers.current[phoneNumber];
        const lastUpdateTime = marker.lastUpdateTime;
        const markerElement = marker.getElement();
        if (lastUpdateTime && (currentTime - lastUpdateTime) > 600000) {
          markerElement.className = 'marker';
          markerElement.style.backgroundColor = 'blue';
          markerElement.style.border = 'none';
        }
      });
    };

    const intervalId = setInterval(checkMarkers, 60000);
    return () => clearInterval(intervalId);
  }, []);

  return <div ref={mapContainer} style={{ width: '100%', height: '100%' }} />;
};

export default MapComponent;