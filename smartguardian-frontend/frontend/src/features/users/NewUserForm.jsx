import { FlexBetween } from '@/components/FlexBetween';
import { Box, Button, TextField, Typography, useMediaQuery, Radio, RadioGroup, FormControlLabel, FormControl, FormLabel } from '@mui/material';
import { Formik } from 'formik';
import { useNavigate } from 'react-router-dom';
import * as yup from 'yup';
import AnimateButton from '../../components/AnimateButton';
import Header from '../../components/Header';
import axios from 'axios';

/**
 * Schema for validating the create student form fields
 */
const createStudentSchema = yup.object().shape({
  firstName: yup.string().required('First Name is required'),
  lastName: yup.string().required('Last Name is required'),
  student_id: yup.string().required('Student ID is required'),
  email_address: yup.string().required('Email Address is required'),
  phone_number: yup.string().required('Phone Number is required'),
  gender: yup.string().required('Gender is required'),
  primary_location: yup.string().required('Primary Location is required'),
});

/**
 * Initial values for the create student form fields
 */
const initialValuesCreateStudent = {
  firstName: '',
  lastName: '',
  student_id: '',
  phone_number: '',
  email_address: '',
  primary_location:'',
  gender: '',
};

/**
 * Component for the New User Form
 */
const NewUserForm = () => {
  const navigate = useNavigate();

  /**
   * Function to create a new student
   * @param {Object} values - The form values
   * @param {Object} onSubmitProps - The formik submit props
   */
  const createStudent = async (values, onSubmitProps) => {
    const data = {
      student_id: values.student_id,
      phone_number: {
        phone_number: values.phone_number,
        email_address: values.email_address,
      },
      primary_location: values.primary_location,
      first_name: values.firstName,
      last_name: values.lastName,
      gender: values.gender,
    };

    try {
      const response = await axios.post('http://127.0.0.1:8001/', data, {
        headers: {
          'Content-Type': 'application/json',
        },
      });

      console.log(response.data);

      if (response.status === 200 || response.status === 201) {
        onSubmitProps.resetForm();
        navigate('/home/users');
      } else {
        console.error('Failed to create student:', response.data);
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  /**
   * Function to handle form submission
   * @param {Object} values - The form values
   * @param {Object} onSubmitProps - The formik submit props
   */
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
            setFieldValue,
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
                <Box sx={{ gridColumn: 'span 2', height: 60 }}>
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
                <Box sx={{ gridColumn: 'span 2', height: 60 }}>
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
                <Box sx={{ gridColumn: 'span 2', height: 60 }}>
                  <TextField
                    size='small'
                    fullWidth
                    label='Student ID'
                    onBlur={handleBlur}
                    onChange={handleChange}
                    value={values.student_id}
                    name='student_id'
                    error={Boolean(touched.student_id) && Boolean(errors.student_id)}
                    helperText={touched.student_id && errors.student_id}
                  />
                </Box>
                <Box sx={{ gridColumn: 'span 2', height: 60 }}>
                  <TextField
                    size='small'
                    fullWidth
                    label='Phone Number'
                    onBlur={handleBlur}
                    onChange={handleChange}
                    value={values.phone_number}
                    name='phone_number'
                    error={Boolean(touched.phone_number) && Boolean(errors.phone_number)}
                    helperText={touched.phone_number && errors.phone_number}
                  />
                </Box>
                <Box sx={{ gridColumn: 'span 2', height: 60 }}>
                  <TextField
                    size='small'
                    fullWidth
                    label='Email Address'
                    onBlur={handleBlur}
                    onChange={handleChange}
                    value={values.email_address}
                    name='email_address'
                    error={Boolean(touched.email_address) && Boolean(errors.email_address)}
                    helperText={touched.email_address && errors.email_address}
                  />
                </Box>
                <Box sx={{ gridColumn: 'span 2', height: 60 }}>
                  <TextField
                    size='small'
                    fullWidth
                    label='Primary Location'
                    onBlur={handleBlur}
                    onChange={handleChange}
                    value={values.primary_location}
                    name='primary_location'
                    error={Boolean(touched.primary_location) && Boolean(errors.primary_location)}
                    helperText={touched.primary_location && errors.primary_location}
                  />
                </Box>
                <Box sx={{ gridColumn: 'span 2', height: 60 }}>
                  <FormControl component="fieldset">
                    <FormLabel component="legend">Gender</FormLabel>
                    <RadioGroup
                      row
                      aria-label="gender"
                      name="gender"
                      value={values.gender}
                      onChange={(event) => setFieldValue('gender', event.target.value)}
                    >
                      <FormControlLabel value="Female" control={<Radio />} label="Female" />
                      <FormControlLabel value="Male" control={<Radio />} label="Male" />
                      <FormControlLabel value="Other" control={<Radio />} label="Other" />
                    </RadioGroup>
                    {touched.gender && errors.gender && (
                      <Typography color="error" variant="body2">
                        {errors.gender}
                      </Typography>
                    )}
                  </FormControl>
                </Box>
                <Box sx={{ gridColumn: 'span 2', height: 60 }}>
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
              </Box>
            </form>
          )}
        </Formik>
      </Box>
    </>
  );
};

export default NewUserForm;