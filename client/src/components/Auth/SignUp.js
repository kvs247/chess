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

function SignUp({ handleSignUp }) {

    const history = useHistory();  

    const formik = useFormik({
        initialValues: {
            fullName: '',
            username: '',
            email: '',
            password: '',
            friend_ids: [],
        },
        validationSchema: validationSchema,
        validateOnChange: false,
        onSubmit: (e) => {
            handleSignUp(e, '/signup')
              .catch(error => {

                  if (error.error.includes('UNIQUE constraint failed: users.email')) {
                    formik.setErrors({ login: 'email already in use' });
                  }
                  if (error.error.includes('UNIQUE constraint failed: users.username')) {
                    formik.setErrors({ login: 'username is taken' });
                  }                  
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
            Sign Up
          </Typography>
          <Box
            component='form'
            onSubmit={(e) => formik.handleSubmit(e, '/signup')}
            textAlign='center'
            sx={{
              width: '25%',
              m: 'auto',
            }}
          >
            <TextField 
              margin='normal'
              required
              fullWidth
              id='fullName'
              label='Full Name'
              name='fullName'
              color='secondary'
              value={formik.values.fullName}
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
              id='username'
              label='Username'
              name='username'
              color='secondary'
              value={formik.values.username}
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
              id='email'
              label='Email Address'
              name='email'
              color='secondary'
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
              Sign Up
            </Button>
            <Box sx={{ mt: 2 }}>
              <Link 
                onClick={() => history.push('/login')} 
                sx={{ 
                  color: '#ffffff', 
                  p: 2,
                  cursor: 'pointer', 
                }}            
              >
                Already have an account? Log in
              </Link>
            </Box>
          </Box>
        </Container>
    );
}

export default SignUp;