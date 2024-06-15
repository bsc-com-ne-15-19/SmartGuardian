import {
  Box,
  Button,
  Checkbox,
  FormControlLabel,
  IconButton,
  InputAdornment,
  TextField,
  Typography,
  useMediaQuery,
} from '@mui/material';
import { Formik } from 'formik';
import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import * as yup from 'yup';
import { useLoginMutation } from './authApiSlice';
import { setLogin } from './authSlice';

const loginSchema = yup.object().shape({
  email: yup
    .string()
    .email('Please provide valid email')
    .required('Email is required'),
  password: yup.string().required('Password is required'),
});

const initialValuesLogin = {
  email: '',
  password: '',
};

const Form = () => {
  const [login] = useLoginMutation();
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const isNonMobile = useMediaQuery('(min-width:600px)');
  const [showPassword, setShowPassword] = useState(false);

  const loginUser = async (values, onSubmitProps) => {
    const response = await login({
      email: values.email,
      password: values.password,
    });
    console.log(response);
    onSubmitProps.resetForm();

    if (response) {
      const access_token = response.data.access_token;
      dispatch(setLogin({ access_token }));
      navigate('/home');
    }
  };

  const handleFormSubmit = async (values, onSubmitProps) => {
    await loginUser(values, onSubmitProps);
  };

  return (
    <Formik
      onSubmit={handleFormSubmit}
      initialValues={initialValuesLogin}
      validationSchema={loginSchema}
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
              Login
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
                gridColumn: 'span 4',
                height: 60,
              }}
            >
              <TextField
                size='small'
                fullWidth
                label='Email'
                onBlur={handleBlur}
                onChange={handleChange}
                value={values.email}
                name='email'
                error={Boolean(touched.email) && Boolean(errors.email)}
                helperText={touched.email && errors.email}
              />
            </Box>

            <Box sx={{ gridColumn: 'span 4', height: 40 }}>
              <TextField
                fullWidth
                size='small'
                label='Password'
                type={showPassword ? 'text' : 'password'}
                onBlur={handleBlur}
                onChange={handleChange}
                value={values.password}
                name='password'
                error={Boolean(touched.password) && Boolean(errors.password)}
                helperText={touched.password && errors.password}
                InputProps={{
                  endAdornment: (
                    <InputAdornment position='end'>
                      <IconButton
                        aria-label='toggle password visibility'
                        onClick={() => setShowPassword(!showPassword)}
                        edge='end'
                      >
                        {showPassword ? <VisibilityOff /> : <Visibility />}
                      </IconButton>
                    </InputAdornment>
                  ),
                }}
              />
            </Box>
            <Box width={170}>
              <FormControlLabel
                label='Keep me sign in'
                control={
                  <Checkbox
                  //   checked={persist}
                  //   onChange={() => setPersist((prev) => !prev)}
                  />
                }
              />
            </Box>
          </Box>

          <Box mt={1}>
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
                Login
              </Button>
            </AnimateButton>
          </Box>
        </form>
      )}
    </Formik>
  );
};

export default Form;

// import { useLoginMutation } from '@/features/auth/authApiSlice';
// import { setLogin } from '@/features/auth/authSlice';
// import Visibility from '@mui/icons-material/Visibility';
// import VisibilityOff from '@mui/icons-material/VisibilityOff';
// import {
//   Box,
//   Button,
//   Checkbox,
//   FormControlLabel,
//   IconButton,
//   InputAdornment,
//   TextField,
//   Typography,
//   useMediaQuery,
// } from '@mui/material';
// import { Formik } from 'formik';
// import { useState } from 'react';
// import { useDispatch } from 'react-redux';
// import { useNavigate } from 'react-router-dom';
// import PulseLoader from 'react-spinners/PulseLoader';
// import * as yup from 'yup';
// import { FlexBetween } from '../../components/FlexBetween';
// import usePersist from '../../hooks/usePersist';
import { FlexBetween } from '@/components/FlexBetween';
import { Visibility, VisibilityOff } from '@mui/icons-material';
import AnimateButton from '../../components/AnimateButton';

// // const registerSchema = yup.object().shape({
// //   firstName: yup.string().required('First name is required'),
// //   lastName: yup.string().required('Last name is required'),
// //   email: yup
// //     .string()
// //     .email('Please provide valid email')
// //     .required('Email is required'),
// //   password: yup.string().required('Password is required'),
// // });

// const loginSchema = yup.object().shape({
//   email: yup
//     .string()
//     .email('Please provide valid email')
//     .required('Email is required'),
//   password: yup.string().required('Password is required'),
// });

// const initialValuesLogin = {
//   email: '',
//   password: '',
// };

// // const initialValuesRegister = {
// //   firstName: '',
// //   lastName: '',
// //   email: '',
// //   password: '',
// // };
// const Form = () => {
//   const [pageType, setPageType] = useState('login');
//   const dispatch = useDispatch();
//   const navigate = useNavigate();
//   const isNonMobile = useMediaQuery('(min-width:600px)');
//   const [login, { isLoading: isLoginLoading }] = useLoginMutation();
//   const [showPassword, setShowPassword] = useState(false);
//   const [persist, setPersist] = usePersist();

//   const loginUser = async (values, onSubmitProps) => {
//     const response = await login({
//       email: values.email,
//       password: values.password,
//     });
//     onSubmitProps.resetForm();

//     if (response) {
//       const access_token = response.data.access_token;
//       dispatch(setLogin({ access_token }));
//       navigate('/dashboard');
//     }
//   };

//   const handleFormSubmit = async (values, onSubmitProps) => {
//     await loginUser(values, onSubmitProps);
//   };

//   if (isLoginLoading) {
//     return <PulseLoader color={'#258cff'} />;
//   }

//   return (
// <Formik
//   onSubmit={handleFormSubmit}
//   initialValues={initialValuesLogin}
//   validationSchema={loginSchema}
// >
//   {({
//     values,
//     errors,
//     touched,
//     handleBlur,
//     handleChange,
//     handleSubmit,
//     resetForm,
//   }) => (
//     <form onSubmit={handleSubmit}>
//       <FlexBetween mb={4}>
//         <Typography sx={{ color: '#262626' }} fontSize={22} fontWeight={500}>
//           Login
//         </Typography>
//       </FlexBetween>
//       <Box
//         display='grid'
//         gap={2}
//         gridTemplateColumns='repeat(4, minmax(0, 1fr))'
//         sx={{
//           '& > div': { gridColumn: isNonMobile ? undefined : 'span 4' },
//         }}
//       >
//         <Box
//           sx={{
//             gridColumn: 'span 4',
//             height: 80,
//           }}
//         >
//           <TextField
//             fullWidth
//             label='Email'
//             onBlur={handleBlur}
//             onChange={handleChange}
//             value={values.email}
//             name='email'
//             error={Boolean(touched.email) && Boolean(errors.email)}
//             helperText={touched.email && errors.email}
//           />
//         </Box>

//         <Box sx={{ gridColumn: 'span 4', height: 60 }}>
//           <TextField
//             fullWidth
//             label='Password'
//             type={showPassword ? 'text' : 'password'}
//             onBlur={handleBlur}
//             onChange={handleChange}
//             value={values.password}
//             name='password'
//             error={Boolean(touched.password) && Boolean(errors.password)}
//             helperText={touched.password && errors.password}
//             InputProps={{
//               endAdornment: (
//                 <InputAdornment position='end'>
//                   <IconButton
//                     aria-label='toggle password visibility'
//                     onClick={() => setShowPassword(!showPassword)}
//                     edge='end'
//                   >
//                     {showPassword ? <VisibilityOff /> : <Visibility />}
//                   </IconButton>
//                 </InputAdornment>
//               ),
//             }}
//           />
//         </Box>
//         <Box width={170}>
//           <FormControlLabel
//             label='Keep me sign in'
//             control={
//               <Checkbox
//               // checked={persist}
//               // onChange={() => setPersist((prev) => !prev)}
//               />
//             }
//           />
//         </Box>
//       </Box>

//       <Box mt={2}>
//         <Button
//           fullWidth
//           type='submit'
//           variant='contained'
//           sx={{
//             textTransform: 'capitalize',
//             fontSize: '1rem',
//             p: '0.8rem',
//           }}
//         >
//           login
//         </Button>
//       </Box>
//     </form>
//   )}
// </Formik>
//   );
// };

// export default Form;
