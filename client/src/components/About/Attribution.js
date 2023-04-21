import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';

function Attribution() {
  return (
    <Box 
      bgcolor='secondary.main' 
      align='center'
      sx={{
        display: 'flex',
        flexDirection: 'column',
        height: '100%',
      }}
    >
      <Typography variant='h5' align='center' sx={{ mt: 3, mb: 3 }}>
        Image Attribution
      </Typography>
      <Box
        sx={{
          mx: 1,
          height: '50%',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'space-evenly',
        }}
      >
        <Link href='https://www.flaticon.com/free-icons/chess' target='_blank' rel='noopener noreferrer' color='#e1e1e1'>
          Chess icons created by Flat Icons - Flaticon
        </Link>
        <br />
        <Link href='https://www.flaticon.com/free-icons/question-mark' target='_blank' rel='noopener noreferrer' color='#e1e1e1'>
          Question mark icons created by Freepik - Flaticon
        </Link>
        <br />
        <Link href='https://www.flaticon.com/free-icons/people' target='_blank' rel='noopener noreferrer' color='#e1e1e1'>
          People icons created by Freepik - Flaticon
        </Link>
        <br />
        <Link href='https://www.flaticon.com/free-icons/logout' target='_blank' rel='noopener noreferrer' color='#e1e1e1'>
          Logout icons created by Tempo_doloe - Flaticon
        </Link>
        <br />
        <Link href='https://www.flaticon.com/free-icons/user' target='_blank' rel='noopener noreferrer' color='#e1e1e1'>
          User icons created by Freepik - Flaticon
        </Link>
        <br />
        <Link href='https://www.flaticon.com/free-icons/sword' target='_blank' rel='noopener noreferrer' color='#e1e1e1'>
          Sword icons created by Freepik - Flaticon
        </Link>
      </Box>
    </Box>
  );
}

export default Attribution;
