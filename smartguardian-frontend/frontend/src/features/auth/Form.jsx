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
import { FlexBetween } from '@/components/FlexBetween';
import { Visibility, VisibilityOff } from '@mui/icons-material';
import AnimateButton from '../../components/AnimateButton';

const loginSchema = yup.object().shape({
  username: yup
    .string().required('Username is required'),
  password: yup.string().required('Password is required'),
});


const initialValuesLogin = {
  username: '',
  password: '',
};

/**
 * Form component for user login.
 *
 * @component
 * @example
 * return (
 *   <Form />
 * )
 */
const Form = () => {
  const [login] = useLoginMutation();
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const isNonMobile = useMediaQuery('(min-width:600px)');
  const [showPassword, setShowPassword] = useState(false);

  /**
   * Login user and handle form submission.
   *
   * @param {Object} values - Form values.
   * @param {Object} onSubmitProps - Formik submit props.
   * @returns {Promise<void>}
   */
  const loginUser = async (values, onSubmitProps) => {
    const response = await login({
      username: values.username,
      password: values.password,
    });
    // console.log(response);
    onSubmitProps.resetForm();

    if (response) {
      const access_token = response.data.access;
      dispatch(setLogin({ access_token }));
      // console.log('token here ----:', access_token);
      navigate('/home');
    }
  };

  /**
   * Handle form submission.
   *
   * @param {Object} values - Form values.
   * @param {Object} onSubmitProps - Formik submit props.
   * @returns {Promise<void>}
   */
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
              Login 🚨
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
                label='User Name'
                onBlur={handleBlur}
                onChange={handleChange}
                value={values.username}
                name='username'
                error={Boolean(touched.username) && Boolean(errors.username)}
                helperText={touched.username && errors.username}
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
