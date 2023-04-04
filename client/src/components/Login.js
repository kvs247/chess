import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Container from '@mui/material/Container';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';

const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    console.log({
        email: data.get('email'),
        password: data.get('password'),
    });
};

function Login() {
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
            onSubmit={handleSubmit}
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
              id='email'
              label='Email Address'
              name='email'
              color='secondary'
              sx={{ input: {color: 'white'} }}
            />
            <TextField 
              margin='normal'
              required
              fullWidth
              id='password'
              label='Password'
              name='password'
              color='secondary'
            />
            <Button
              type='submit'
              fullWidth
              variant='contained'
              sx={{ mt: 3 }}
            >
                Log In
            </Button>
            <Box sx={{ mt: 2 }}>
              <Link href='/signup' sx={{ color: '#ffffff', p: 2 }}>
                Don't have an account? Sign Up
              </Link>
            </Box>
            <Box sx={{ display: 'flex', mt: 2 }}>
              <br />
              <Link href='/home' sx={{ color: '#ffffff', mx: 'auto' }}>
                Log In As Guest
              </Link>
            </Box>
          </Box>
        </Container>
    );
}

export default Login;