/**
 * Renders the dashboard component.
 * @component
 * @returns {JSX.Element} The rendered dashboard component.
 */
import 'mapbox-gl/dist/mapbox-gl.css';
import { MapProvider } from 'react-map-gl';
import Header from '../../components/Header';
import MapCard from '../../components/MapCard';

export const Dashboard = () => {
  return (
    <>
      <MapProvider>
        <Header sx={{ position: 'absolute' }} />
        <MapCard />
      </MapProvider>
    </>
  );
};
