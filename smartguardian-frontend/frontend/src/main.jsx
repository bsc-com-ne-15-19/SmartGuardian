import 'mapbox-gl/dist/mapbox-gl.css';
import React from 'react';
import ReactDOM from 'react-dom/client';
import { MapProvider } from 'react-map-gl';
import { Provider } from 'react-redux';
import App from './App.jsx';
import { store } from './app/store.js';
import './index.css';

/**
 * Renders the main application.
 */
ReactDOM.createRoot(document.getElementById('map')).render(
  /**
   * Wraps the application with React's StrictMode.
   * 
   * @returns {JSX.Element} The wrapped application.
   */
  <React.StrictMode>
    <MapProvider>
      <Provider store={store}>
        <App />
      </Provider>
    </MapProvider>
  </React.StrictMode>
);
