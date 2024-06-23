import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Box, Button, Stack } from '@mui/material';
import { DataGrid } from '@mui/x-data-grid';
import WatchRoundedIcon from '@mui/icons-material/WatchRounded'; // Ensure this import is added
import Header from '../../components/Header';

/**
 * Component for displaying a list of users.
 *
 * @component
 * @param {string} apiUrl - The API URL for fetching user data.
 * @returns {JSX.Element} - The rendered component.
 */
const UsersList = ({ apiUrl = 'http://127.0.0.1:8001/ManageStudents/' }) => {
  const navigate = useNavigate();
  const [rows, setRows] = useState([]);

  useEffect(() => {
    /**
     * Fetches user data from the API and updates the rows state.
     *
     * @function
     * @param {string} apiUrl - The API URL for fetching user data.
     */
    const fetchData = (apiUrl) => {
      fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
          const updatedRows = data.map((student, index) => ({
            ...student,
            id: student.phone_number.phone_number, // Use 'phone_number' as the 'id' property
            index: index + 1 // Add an index property to each row
          }));
          setRows(updatedRows);
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    };

    fetchData(apiUrl);
  }, [apiUrl]);

  const columns = [
    { field: 'index', headerName: '#', width: 50},
    { field: 'id', headerName: 'DEVICE NUMBER', width: 200 },
    { field: 'first_name', headerName: 'FIRST NAME', width: 200 },
    { field: 'last_name', headerName: 'LAST NAME', width: 200 },
    { field: 'student_id', headerName: 'STUDENT ID', width: 200 },
    { field: 'primary_location', headerName: 'PRIMARY LOCATION', width: 200 },
    {
      field: 'device_status',
      headerName: 'DEVICE STATUS',
      width: 200,
      renderCell: (params) => (
        <WatchRoundedIcon
          style={{ color: params.value ? 'lime' : 'gray' }}
        />
      ),
    },
  ];

  return (
    <>
      <Header />
      <Box mt={10} px={6}>
        <Stack justifyContent='space-between' alignItems='center' direction='row'>
          <h3>Students</h3>
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

export default UsersList;