import { Box, Container, Paper } from '@mui/material';
import Form from './Form';

const Login = () => {
  return (
    <Box
      sx={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        minHeight: '100vh',
        background: '#fafafb', // Set minimum height to fill the viewport
      }}
    >
      <Container sx={{ maxWidth: { xs: 400, lg: 475 } }}>
        <Paper sx={{ borderRadius: 2 }}>
          <Box p='2rem' m='2rem auto'>
            <Form />
          </Box>
        </Paper>
      </Container>
    </Box>
  );
};

export default Login;
