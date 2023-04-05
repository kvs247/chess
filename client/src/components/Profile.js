import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';

import moment from 'moment';

const length = '80%';


function Profile({ user }) {

    let formattedDate = '';
    if (user.date_joined) {
      const yyyymmdd = user.date_joined.split(' ')[0].split('-')
      const date = new Date(yyyymmdd[0], yyyymmdd[1]-1, yyyymmdd[2])
      formattedDate = moment(date).format('MMMM D Y')
    };

    return (
        <Box
          bgcolor='primary.main'
          align='center'
          my='auto'
        >
          <Box
            bgcolor='secondary.main'
            width={length}
            height='40vh'
            sx={{
              display:'flex'

            }}
          >
            <Box 
              component='img'
              alt=''
              src={user.profile_image}
              sx={{
                height: '80%',
                mx: 2,
                my: 'auto',
              }}
            />
            <Box
              sx={{
                m: 'auto',
              }}
            >
              <Typography variant='h3' sx={{ mb: 5 }}>{user.username}</Typography>
              <Typography variant='h4' sx={{ mb: 5 }}>{user.full_name}</Typography>
              <Grid container spacing={2}>
                <Grid item xs={4}>
                  <Typography variant='h5'>Games</Typography>
                </Grid>
                <Grid item xs={4}>
                  <Typography variant='h5'>Wins</Typography>
                </Grid>
                <Grid item xs={4}>
                  <Typography variant='h5'>Joined</Typography>
                </Grid>
                <Grid item xs={4}>
                  <Typography variant='h5'>3253</Typography>
                </Grid>
                <Grid item xs={4}>
                  <Typography variant='h5'>1378</Typography>
                </Grid>
                <Grid item xs={4}>
                  <Typography variant='h5'>{formattedDate}</Typography>
                </Grid>
              </Grid>
            </Box>
          </Box>

          <Box
            bgcolor='secondary.main'
            width={length}
            mt={5}
            height='40vh'
          >
            <Typography variant='h4'>Profile</Typography>
          </Box>
        </Box>
    );
}

export default Profile;