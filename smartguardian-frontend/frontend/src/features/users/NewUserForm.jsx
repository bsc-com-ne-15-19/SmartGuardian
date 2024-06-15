import { FlexBetween } from '@/components/FlexBetween';
import { Login } from '@mui/icons-material';
import { Box, Button, TextField, Typography, useMediaQuery } from '@mui/material';
import { Formik } from 'formik';
import { useNavigate } from 'react-router-dom';
import * as yup from 'yup';
import AnimateButton from '../../components/AnimateButton';
import Header from '../../components/Header';

const createStudentSchema = yup.object().shape({
  firstName: yup.string().required('First Name is required'),
  lastName: yup.string().required('Last Name is required'),
  age: yup.number().required('Age is required'),
  address: yup.string().required('Address is required'),
  phoneNumber: yup.string().required('Phone Number is required'),
  guardianName: yup.string().required('Guardian Name is required'),
  guardianAddress: yup.string().required('Guardian Address is required'),
  guardianPhoneNumber: yup.string().required('Guardian Phonenumber is required'),
  relationship: yup.string().required('Relationship is required'),
});

const initialValuesCreateStudent = {
  firstName: '',
  lastName: '',
  address: '',
  phoneNumber: '',
  guardianName: '',
  guardianAddress: '',
  guardianPhoneNumber: '',
  relationship: '',
};

const NewUserForm = () => {
  const navigate = useNavigate();
  const createStudent = async (values, onSubmitProps) => {
    const response = await Login({
      firstName: values.firstName,
      lastName: values.lastName,
      address: values.address,
      phoneNumber: values.phoneNumber,
      guardianName: values.guardianName,
      guardianAddress: values.guardianAddress,
      guardianPhoneNumber: values.guardianPhoneNumber,
      relationship: values.relationship,
    });
    console.log(response);
    onSubmitProps.resetForm();

    if (response) {
      navigate('/home/users');
    }
  };
  const handleFormSubmit = async (values, onSubmitProps) => {
    await createStudent(values, onSubmitProps);
  };
  const isNonMobile = useMediaQuery('(min-width:600px)');

  return (
    <>
      <Header />

      <Box mt={10} px={6}>
        <Formik
          onSubmit={handleFormSubmit}
          initialValues={initialValuesCreateStudent}
          validationSchema={createStudentSchema}
        >
          {({
            values,
            errors,
            touched,
            handleBlur,
            handleChange,
            handleSubmit,
            isSubmitting,
          }) => (
            <form onSubmit={handleSubmit}>
              <FlexBetween mb={4}>
                <Typography sx={{ color: '#262626' }} fontSize={22} fontWeight={500}>
                  Add New Student
                </Typography>
              </FlexBetween>
              <Box
                display='grid'
                gap={2}
                gridTemplateColumns='repeat(4, minmax(0, 1fr))'
                sx={{
                  '& > div': { gridColumn: isNonMobile ? undefined : 'span 4' },
                }}
              >
                <Box
                  sx={{
                    gridColumn: 'span 2',
                    height: 60,
                  }}
                >
                  <TextField
                    size='small'
                    fullWidth
                    label='First Name'
                    onBlur={handleBlur}
                    onChange={handleChange}
                    value={values.firstName}
                    name='firstName'
                    error={Boolean(touched.firstName) && Boolean(errors.firstName)}
                    helperText={touched.firstName && errors.firstName}
                  />
                </Box>
                <Box
                  sx={{
                    gridColumn: 'span 2',
                    height: 60,
                  }}
                >
                  <TextField
                    size='small'
                    fullWidth
                    label='Last Name'
                    onBlur={handleBlur}
                    onChange={handleChange}
                    value={values.lastName}
                    name='lastName'
                    error={Boolean(touched.lastName) && Boolean(errors.lastName)}
                    helperText={touched.lastName && errors.lastName}
                  />
                </Box>
                <Box
                  sx={{
                    gridColumn: 'span 2',
                    height: 60,
                  }}
                >
                  <TextField
                    size='small'
                    fullWidth
                    label='Age'
                    onBlur={handleBlur}
                    onChange={handleChange}
                    value={values.age}
                    name='age'
                    error={Boolean(touched.age) && Boolean(errors.age)}
                    helperText={touched.age && errors.age}
                  />
                </Box>
                <Box
                  sx={{
                    gridColumn: 'span 2',
                    height: 60,
                  }}
                >
                  <TextField
                    size='small'
                    fullWidth
                    label='Phone Number'
                    onBlur={handleBlur}
                    onChange={handleChange}
                    value={values.phoneNumber}
                    name='phoneNumber'
                    error={
                      Boolean(touched.phoneNumber) && Boolean(errors.phoneNumber)
                    }
                    helperText={touched.phoneNumber && errors.phoneNumber}
                  />
                </Box>
                <Box
                  sx={{
                    gridColumn: 'span 2',
                    height: 60,
                  }}
                >
                  <TextField
                    size='small'
                    fullWidth
                    label='Address'
                    onBlur={handleBlur}
                    onChange={handleChange}
                    value={values.address}
                    name='address'
                    error={Boolean(touched.address) && Boolean(errors.address)}
                    helperText={touched.address && errors.address}
                  />
                </Box>
                <Box
                  sx={{
                    gridColumn: 'span 2',
                    height: 60,
                  }}
                >
                  <TextField
                    size='small'
                    fullWidth
                    label='Guardian Name'
                    onBlur={handleBlur}
                    onChange={handleChange}
                    value={values.guardianName}
                    name='guardianName'
                    error={
                      Boolean(touched.guardianName) && Boolean(errors.guardianName)
                    }
                    helperText={touched.guardianName && errors.guardianName}
                  />
                </Box>
                <Box
                  sx={{
                    gridColumn: 'span 2',
                    height: 60,
                  }}
                >
                  <TextField
                    size='small'
                    fullWidth
                    label='Guardian Phone Number'
                    onBlur={handleBlur}
                    onChange={handleChange}
                    value={values.guardianPhoneNumber}
                    name='guardianPhoneNumber'
                    error={
                      Boolean(touched.guardianPhoneNumber) &&
                      Boolean(errors.guardianPhoneNumber)
                    }
                    helperText={
                      touched.guardianPhoneNumber && errors.guardianPhoneNumber
                    }
                  />
                </Box>
                <Box
                  sx={{
                    gridColumn: 'span 2',
                    height: 60,
                  }}
                >
                  <TextField
                    size='small'
                    fullWidth
                    label='Guardian Address'
                    onBlur={handleBlur}
                    onChange={handleChange}
                    value={values.guardianAddress}
                    name='guardianAddress'
                    error={
                      Boolean(touched.guardianAddress) &&
                      Boolean(errors.guardianAddress)
                    }
                    helperText={touched.guardianAddress && errors.guardianAddress}
                  />
                </Box>
                <Box
                  sx={{
                    gridColumn: 'span 2',
                    height: 60,
                  }}
                >
                  <TextField
                    size='small'
                    fullWidth
                    label='Relationship'
                    onBlur={handleBlur}
                    onChange={handleChange}
                    value={values.relationship}
                    name='relationship'
                    error={
                      Boolean(touched.relationship) && Boolean(errors.relationship)
                    }
                    helperText={touched.relationship && errors.relationship}
                  />
                </Box>
              </Box>

              <Box mt={1} display='flex' justifyContent='flex-end'>
                <AnimateButton>
                  <Button
                    disableElevation
                    disabled={isSubmitting}
                    fullWidth
                    size='medium'
                    type='submit'
                    variant='contained'
                    color='primary'
                  >
                    Create Student
                  </Button>
                </AnimateButton>
              </Box>
            </form>
          )}
        </Formik>
      </Box>
    </>
  );
};

export default NewUserForm;
