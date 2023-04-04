import { Container, Typography, Box } from '@mui/material';

function Home() {
    return (
        <Container sx={{ bgcolor: 'primary.main', height: '100vh', width: '100vw', p: 0, m: 0 }}>
            <Typography 
              variant='h1'
              sx={{ textAlign: 'center' }}
            >
              Chess Is Hard
            </Typography>
            <Box>
                <input type='text'></input>
            </Box>
        </Container>
    );
}

export default Home;