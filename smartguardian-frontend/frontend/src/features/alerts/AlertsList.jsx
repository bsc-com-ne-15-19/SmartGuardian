/* eslint-disable react/jsx-key */

import CrisisAlertIcon from '@mui/icons-material/CrisisAlert';
import { Box, Button, Stack } from '@mui/material';
import { DataGrid, GridActionsCellItem } from '@mui/x-data-grid';
import { useNavigate } from 'react-router-dom';
import Header from '../../components/Header';
const rows = [
  {
    id: 1,
    firstName: 'Aubrey',
    surname: 'Moyo',
    timeTriggerdAlert: '00:00:00',
    counts: '25',
    AlertLocation: 'Mwambo',
  },
  {
    id: 2,
    firstName: 'Aubrey',
    surname: 'Muwalo',
    timeTriggerdAlert: '00:00:00',
    counts: '25',
    AlertLocation: 'Mwambo',
  },
  {
    id: 3,
    firstName: 'Aubrey',
    surname: 'Muwalo',
    timeTriggerdAlert: '00:00:00',
    counts: '25',
    AlertLocation: 'Mwambo',
  },
];

const columns = [
  { field: 'id', headerName: '#', width: 10 },
  { field: 'firstName', headerName: 'FIRST NAME', width: 150 },
  { field: 'surname', headerName: 'SURNAME', width: 150 },
  { field: 'timeTriggerdAlert', headerName: 'TIME TRIGGERD ALERT', width: 200 },
  { field: 'counts', headerName: 'COUNTS', width: 200 },
  { field: 'AlertLocation', headerName: 'ALERT LOCATION', width: 200 },
  // { field: 'actions', headerName: 'ACTIONS', width: 150, },
  {
    field: 'actions',
    type: 'actions',
    headerName: 'STATUS',
    width: 200,
    cellClassName: 'actions',
    // eslint-disable-next-line no-unused-vars
    getActions: ({ id }) => {
      return [
        <GridActionsCellItem
          icon={<CrisisAlertIcon />}
          label='View'
          className='textPrimary'
          // onClick={handleEditClick(id)}
          color='inherit'
        />,
      ];
    },
  },
];
const AlertsList = () => {
  const navigate = useNavigate();
  return (
    <>
      <Header />
      <Box mt={10} px={6}>
        <Stack justifyContent='space-between' alignItems='center' direction='row'>
          <h3>Alerts</h3>
          <Button variant='contained' onClick={() => navigate('/home/users/create')}>
            Add New Student
          </Button>
        </Stack>
        <Box
          sx={{
            height: 500,
            width: '100%',

            '& .actions': {
              color: 'text.secondary',
            },
            '& .textPrimary': {
              color: 'text.primary',
            },
          }}
        >
          <DataGrid rows={rows} columns={columns} />
        </Box>
      </Box>
    </>
  );
};

export default AlertsList;
