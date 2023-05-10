import { useContext } from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Container from '@mui/material/Container';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';
import { useFormik } from 'formik';
import * as yup from 'yup';
import { useHistory } from 'react-router-dom';

import { AppContext } from '../../App.js';

const validationSchema = yup.object({
    email: yup
        .string('Enter your email')
        .email('Enter a valid email')
        .required('Email is required'),
    password: yup
        .string('Enter your password')
        .min(8, 'Password should be of minimum 8 characters length')
        .required('Password is required'),
});

function Login() {

    const history = useHistory();

    const { handleLoginSignUp } = useContext(AppContext);

    const formik = useFormik({
        initialValues: {
            email: '',
            password: '',
        },
        validationSchema: validationSchema,
        validateOnChange: false,
        onSubmit: (e) => {
            handleLoginSignUp(e, '/login')
              .catch(error => {
                  formik.setErrors({ login: error.error });
              });
        }
      });

    return (
        <Container
          sx={{ 
            bgcolor: 'primary.main', 
            height: '100vh', 
            width: '100vw', 
            minWidth: '100%',
          }}
        >
          <CssBaseline />  
          <Typography 
              variant='h1'
              sx={{ 
                textAlign: 'center',
                py: 10,
              }}
          >
            Chess Is Hard
          </Typography>
          <Typography 
              variant='h2'
              sx={{ 
                textAlign: 'center',
                pb: 4,
              }}
          >
            Login
          </Typography>
          <Box
            component='form'
            onSubmit={(e) => formik.handleSubmit(e, '/login')}
            textAlign='center'
            sx={{
              width: '25%',
              m: 'auto',
            }}
          >
            <TextField 
              required
              fullWidth
              color='secondary'
              id='email'
              label='Email Address'
              margin='normal'
              name='email'
              value={formik.values.email}
              onChange={formik.handleChange}
              InputLabelProps={{
                style: {
                  color: '#E1E1E1',
                }
              }}
              sx={{ input: {color: '#E1E1E1'}, border: {color: '#E1E1E1'} }}
            />
            <TextField 
              margin='normal'
              required
              fullWidth
              id='password'
              label='Password'
              name='password'
              type='password'
              color='secondary'
              value={formik.values.password}
              onChange={formik.handleChange}
              InputLabelProps={{
                style: {
                  color: '#E1E1E1',
                }
              }}
              sx={{ input: {color: '#E1E1E1'}, border: {color: '#E1E1E1'} }}
            />
            {/* Errors */}
            {Object.keys(formik.errors).length > 0 &&
              <Box sx={{ mb: 2 }}>
                {Object.keys(formik.errors).map((error, index) => (
                  <Typography key={index} sx={{ color: 'error.main' }}>
                    {formik.errors[error]}
                  </Typography>
                ))}    
              </Box>
            }
            <Button
              type='submit'
              fullWidth
              variant='contained'
              sx={{ mt: 3 }}
            >
                Log In
            </Button>
            <Box sx={{ mt: 2 }}>
              <Link 
                onClick={() => history.push('/signup')} 
                sx={{ 
                  color: '#ffffff', 
                  p: 2,
                  cursor: 'pointer',
                }}
                >
                Don't have an account? 
                Sign Up
              </Link>
            </Box>
            <Box sx={{ display: 'flex', mt: 2 }}>
              <br />
              <Link 
                onClick={() => {
                    history.push('/play');
                    const guestLogin = {
                        email: 'guest@fake.com',
                        password: 'password'
                    };
                    handleLoginSignUp(guestLogin, '/login');
                }} 
                sx={{ 
                  color: '#ffffff', 
                  mx: 'auto',
                  cursor: 'pointer',
                }}
              >
                Log In As Guest
              </Link>
            </Box>
          </Box>
        </Container>
    );
}

export default Login;