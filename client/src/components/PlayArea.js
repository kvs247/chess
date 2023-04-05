import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';

import guest from '../assets/profile-image.png';

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

function PlayArea({ user }) {
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
              height: length,
              width: length,
            }}
          />
          {playerBox(user.username, user.profile_image)}
        </Box>
    );
}

export default PlayArea