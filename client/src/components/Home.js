import { useState } from 'react';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Box from '@mui/material/Box';
import CssBaseline from '@mui/material/CssBaseline';

import NavBar from './NavBar';
import ActiveGames from './ActiveGames';
import PlayArea from './PlayArea';

function Home() {
    return (
        <Container 
          disableGutters
          sx={{ 
            bgcolor: 'primary.main', 
            height: '100vh', 
            width: '100vw',
            minWidth: '100%',
            display: 'grid',
            gridTemplateColumns: '15% 70% 15%',
            padding: 0
          }}
          >
          <CssBaseline />
          <NavBar />
          <PlayArea />
          <ActiveGames />
        </Container>
    );
}

export default Home;