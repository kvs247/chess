import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import CssBaseline from '@mui/material/CssBaseline';

import guest from '../assets/profile-image.png';
import magnus from '../assets/carlsen.jpg'

const length = '80vh';

const playerBox = (username, photo) => {
  return (
    <Box
      sx={{
        width: length,
        display: 'flex',
        alignItems: 'center',
        my: 1,
        color: '#e1e1e1',
      }}
    >
      <Box 
        component='img'
        src={photo}
        alt=''
        sx={{
          width: 50,
          mr: 1,
          borderRadius: '5px',
        }}
      />
      {`${username}`}
  </Box>
  );
};

function PlayArea() {
    return (
        <Box 
          bgcolor='primary.main' 
          align='center' 
          my='auto'
        >
          <CssBaseline />
          {playerBox('Opponent', guest)}
          <Box
            sx={{
              bgcolor: 'purple',
              height: length,
              width: length,
            }}
          />
          {playerBox('DrDrunkenstein', magnus)}
        </Box>
    );
}

export default PlayArea