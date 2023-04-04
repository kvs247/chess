import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';

import guest from '../assets/profile-image.png';
import magnus from '../assets/carlsen.jpg'

const playerBox = (username, photo) => {
  return (
    <Box
      sx={{
        width: '85vh',
        display: 'flex',
        alignItems: 'center',
        my: 1
      }}
    >
      <Box 
        component='img'
        src={photo}
        alt=''
        sx={{
          width: 50,
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
          {playerBox('Opponent', guest)}
          <Box
            sx={{
              bgcolor: 'purple',
              height: '85vh',
              width: '85vh',
            }}
          />
          {playerBox('DrDrunkenstein', magnus)}
        </Box>
    );
}

export default PlayArea