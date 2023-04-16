import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Container from '@mui/material/Container';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';

function SignUp({ onSubmit }) {
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
            onSubmit={(e) => onSubmit(e, '/signup')}
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
              InputLabelProps={{
                style: {
                  color: '#E1E1E1',
                }
              }}
              sx={{ input: {color: '#E1E1E1'}, border: {color: '#E1E1E1'} }}
            />
            <Button
              type='submit'
              fullWidth
              variant='contained'
              sx={{ mt: 3 }}
            >
              Sign Up
            </Button>
            <Box sx={{ mt: 2 }}>
              <Link href='/login' sx={{ color: '#ffffff', p: 2 }}>
                Already have an account? Log in
              </Link>
            </Box>
          </Box>
        </Container>
    );
}

export default SignUp;