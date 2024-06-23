import React, { useEffect, useState } from 'react';
import axios from 'axios';
import CrisisAlertIcon from '@mui/icons-material/CrisisAlert';
import { Box, Button, Stack } from '@mui/material';
import { DataGrid, GridActionsCellItem } from '@mui/x-data-grid';
import { useNavigate } from 'react-router-dom';
import Header from '../../components/Header';

/**
 * Component that displays a list of alerts.
 */
const AlertsList = () => {
  const [rows, setRows] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    /**
     * Fetches the alerts from the server.
     */
    /**
     * Fetches alerts from the server and updates the state with the fetched data.
     * @returns {Promise<void>} A Promise that resolves when the alerts are fetched and the state is updated.
     */
    const fetchAlerts = async () => {
      try {
        // const response = await axios.get('http://127.0.0.1:8001/alert_api/alert-summary/');
        const response = await axios.get('http://127.0.0.1:8001/alert_api/alert-summary/');
        // Set the fetched alert data to the state variable 'rows'
        setRows(response.data);
        const alertData = response.data.map((alert, index) => ({
          id: index + 1,
          firstName: alert.student_name.split(' ')[0] || 'Unknown',
          surname: alert.student_name.split(' ')[1] || 'Unknown',
          timeTriggerdAlert: alert.timestamp,
          // timeTriggerdAlert: new Date(alert.timestamp).toLocaleTimeString(),
          counts: alert.alert_count,
          location: alert.location || 'Unknown',
          status: alert.alert_status
        }));
        setRows(alertData);
      } catch (error) {
        console.error('Error fetching alert data:', error);
      }
    };

    fetchAlerts();
  }, []);

  const columns = [
    { field: 'id', headerName: '#', width: 50 },
    { field: 'firstName', headerName: 'FIRST NAME', width: 150 },
    { field: 'surname', headerName: 'SURNAME', width: 150 },
    { field: 'timeTriggerdAlert', headerName: 'TIME TRIGGERD ALERT', width: 300 },
    { field: 'counts', headerName: 'COUNTS', width: 150 },
    { field: 'location', headerName: 'LAST ALERT LOCATION', width: 400 },
    // { field: 'status', headerName: 'STATUS', width: 150 },
    {
      // field: 'actions',
      // type: 'actions',
      // headerName: 'Actions',
      // width: 150,
      // cellClassName: 'ACTIONS',
      // getActions: ({ id }) => {
      //   return [
      //     <GridActionsCellItem
      //       icon={<CrisisAlertIcon />}
      //       label='View'
      //       className='textPrimary'
      //       color='inherit'
      //       onClick={() => handleViewClick(id)}
      //     />
      //   ];
      // }
    }
  ];

  // const handleViewClick = (id) => {
  //   console.log('View alert with id:', id);
  //   // Handle the view action here
  // };

  return (
    <>
      <Header />
      <Box mt={10} px={6}>
        <Stack justifyContent='space-between' alignItems='center' direction='row'>
          <h3>Alerts</h3>
          {/* <Button variant='contained' onClick={() => navigate('/home/users/create')}>
            Track Device
          </Button> */}
        </Stack>
        <Box
          sx={{
            height: 500,
            width: '100%',
            '& .actions': {
              color: 'text.secondary'
            },
            '& .textPrimary': {
              color: 'text.primary'
            }
          }}
        >
          <DataGrid rows={rows} columns={columns} />
        </Box>
      </Box>
    </>
  );
};

export default AlertsList;