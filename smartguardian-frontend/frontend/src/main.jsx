import 'mapbox-gl/dist/mapbox-gl.css';
import React from 'react';
import ReactDOM from 'react-dom/client';
import { MapProvider } from 'react-map-gl';
import { Provider } from 'react-redux';
import App from './App.jsx';
import { store } from './app/store.js';
import './index.css';

ReactDOM.createRoot(document.getElementById('map')).render(
  <React.StrictMode>
    <MapProvider>
      <Provider store={store}>
        <App />
      </Provider>
    </MapProvider>
  </React.StrictMode>
);
