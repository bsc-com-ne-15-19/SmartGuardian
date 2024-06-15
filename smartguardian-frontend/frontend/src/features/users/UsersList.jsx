import React, { useState, useEffect } from 'react';
import DeleteIcon from '@mui/icons-material/DeleteOutlined';
import EditIcon from '@mui/icons-material/Edit';
import VisibilityIcon from '@mui/icons-material/Visibility';
import { Box, Button, Stack } from '@mui/material';
import { DataGrid, GridActionsCellItem } from '@mui/x-data-grid';
import { useNavigate } from 'react-router-dom';
import Header from '../../components/Header';

const UsersList = () => {
  const navigate = useNavigate();
  const [rows, setRows] = useState([]);

  useEffect(() => {
    // Fetch data from API when the component mounts
    fetch('http://127.0.0.1:8001/ManageStudents/')
      .then(response => response.json())
      .then(data => {
        // Assuming your API response contains an array of students
        // Map the student objects to add an 'id' property using 'phone_number'
        const updatedRows = data.map((student, index) => ({
          ...student,
          id: student.phone_number.phone_number // Use 'phone_number' as the 'id' property
        }));
        setRows(updatedRows);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  const columns = [
    { field: 'id', headerName: 'DEVICE NUMBER', width: 200 },
    { field: 'first_name', headerName: 'FIRST NAME', width: 200 },
    { field: 'last_name', headerName: 'LAST NAME', width: 200 },
    { field: 'student_id', headerName: 'STUDENT ID', width: 200 },
    { field: 'primary_location', headerName: 'PRIMARY LOCATION', width: 200 },
    {
      field: 'actions',
      type: 'actions',
      headerName: 'Actions',
      width: 200,
      cellClassName: 'actions',
      getActions: ({ id }) => [
        <GridActionsCellItem
          key={`view_${id}`}
          icon={<VisibilityIcon />}
          label='View'
          className='textPrimary'
          // onClick={handleEditClick(id)}
          color='inherit'
        />,
        <GridActionsCellItem
          key={`edit_${id}`}
          icon={<EditIcon />}
          label='Edit'
          className='textPrimary'
          // onClick={handleEditClick(id)}
          color='inherit'
        />,
        <GridActionsCellItem
          key={`delete_${id}`}
          icon={<DeleteIcon />}
          label='Delete'
          // onClick={handleDeleteClick(id)}
          color='inherit'
        />,
      ],
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


/* eslint-disable react/jsx-key */
// import { Box, Typography } from '@mui/material';
// import React from 'react';
// import PulseLoader from 'react-spinners/PulseLoader';
// import { useGetUsersQuery } from './usersApiSlice';

// const UsersList = () => {
//   const { data: users, isLoading, isSuccess, isError, error } = useGetUsersQuery();

//   if (isLoading) {
//     return <PulseLoader color='#36d7b7' />;
//   }

//   if (isError) {
//     <Typography color='error' variant='subtitle2'>
//       {error?.data?.message}
//     </Typography>;
//   }

//   if (isSuccess) {
//     const { ids } = users;
//     console.log(ids);
//     return <Box>UsersList</Box>;
//   }
// };

// export default UsersList;
// import DeleteIcon from '@mui/icons-material/DeleteOutlined';
// import EditIcon from '@mui/icons-material/Edit';
// import VisibilityIcon from '@mui/icons-material/Visibility';
// import { Box, Button, Stack } from '@mui/material';
// import { DataGrid, GridActionsCellItem } from '@mui/x-data-grid';
// import { useNavigate } from 'react-router-dom';
// import Header from '../../components/Header';

// const rows = [
//   {
//     id: 1,
//     firstName: 'Aubrey',
//     surname: 'Muwalo',
//     registrationNumber: 'BSC/COM/NE/03/19',
//     device: '9847623',
//     location: 'Mwambo',
//     actions: '',
//   },
//   {
//     id: 2,
//     firstName: 'Aubrey',
//     surname: 'Muwalo',
//     registrationNumber: 'BSC/COM/NE/03/19',
//     device: '9847623',
//     location: 'Mwambo',
//     actions: '',
//   },
//   {
//     id: 3,
//     firstName: 'Aubrey',
//     surname: 'Muwalo',
//     registrationNumber: 'BSC/COM/NE/03/19',
//     device: '9847623',
//     location: 'Mwambo',
//     actions: '',
//   },
// ];

// const columns = [
//   { field: 'id', headerName: '#', width: 10 },
//   { field: 'firstName', headerName: 'FIRST NAME', width: 150 },
//   { field: 'surname', headerName: 'SURNAME', width: 150 },
//   { field: 'registrationNumber', headerName: 'REGISTRATION #', width: 200 },
//   { field: 'device', headerName: 'DEVICE', width: 200 },
//   { field: 'location', headerName: 'LOCATION', width: 200 },
//   // { field: 'actions', headerName: 'ACTIONS', width: 150, },
//   {
//     field: 'actions',
//     type: 'actions',
//     headerName: 'Actions',
//     width: 200,
//     cellClassName: 'actions',
//     // eslint-disable-next-line no-unused-vars
//     getActions: ({ id }) => {
//       return [
//         <GridActionsCellItem
//           icon={<VisibilityIcon />}
//           label='View'
//           className='textPrimary'
//           // onClick={handleEditClick(id)}
//           color='inherit'
//         />,
//         <GridActionsCellItem
//           icon={<EditIcon />}
//           label='Edit'
//           className='textPrimary'
//           // onClick={handleEditClick(id)}
//           color='inherit'
//         />,

//         <GridActionsCellItem
//           icon={<DeleteIcon />}
//           label='Delete'
//           // onClick={handleDeleteClick(id)}
//           color='inherit'
//         />,
//       ];
//     },
//   },
// ];
// const UsersList = () => {
//   const navigate = useNavigate();
//   return (
//     <>
//       <Header />
//       <Box mt={10} px={6}>
//         <Stack justifyContent='space-between' alignItems='center' direction='row'>
//           <h3>Students</h3>
//           <Button variant='contained' onClick={() => navigate('/home/users/create')}>
//             Add New Student
//           </Button>
//         </Stack>
//         <Box
//           sx={{
//             height: 500,
//             width: '100%',

//             '& .actions': {
//               color: 'text.secondary',
//             },
//             '& .textPrimary': {
//               color: 'text.primary',
//             },
//           }}
//         >
//           <DataGrid rows={rows} columns={columns} />
//         </Box>
//       </Box>
//     </>
//   );
// };

// export default UsersList;
