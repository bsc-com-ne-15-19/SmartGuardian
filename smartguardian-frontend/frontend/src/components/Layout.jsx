import { Stack } from '@mui/material';
import { MapProvider } from 'react-map-gl';
import { Outlet } from 'react-router-dom';
import Header from './Header';

export const Layout = () => {
  return (
    <MapProvider>
      <Stack mt={2} spacing={2}>
        <Header />
        <Outlet />
      </Stack>
    </MapProvider>
  );
};
