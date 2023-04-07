import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';

import moment from 'moment';

import readPGN from '../Util/pngHandler.js'

import CompletedGames from './CompletedGames.js';

const length = '80%';

function Profile({ user, profileData, games }) {
  
  
  // only render if profileData is not empty
  if (profileData?.date_joined) {
    
      const numGames = games.length;
      const wonGames = games.filter(g => {
          const pgnObj = readPGN(g.pgn);
          const isWhite = pgnObj['whiteUsername'] === profileData.username;
          const isBlack = pgnObj['blackUsername'] === profileData.username;
          const whiteWon = pgnObj['result'] === '1-0';
          const blackWon = pgnObj['result'] === '0-1';
          return ((whiteWon && isWhite) || (blackWon && isBlack));
        });
        const numWon = wonGames.length;

      const yyyymmdd = profileData.date_joined.split(' ')[0].split('-')
      const date = new Date(yyyymmdd[0], yyyymmdd[1]-1, yyyymmdd[2])
      const formattedDate = moment(date).format('MMMM D Y')

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
                src={profileData.profile_image}
                sx={{
                  height: '80%',
                  mx: 2,
                  my: 'auto',
                }}
              />
              <Box sx={{ m: 'auto'}}>
                <Typography variant='h3' sx={{ mb: 5 }}>{profileData.username}</Typography>
                <Typography variant='h4' sx={{ mb: 5 }}>{profileData.full_name}</Typography>
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
                    <Typography variant='h5'>{numGames}</Typography>
                  </Grid>
                  <Grid item xs={4}>
                    <Typography variant='h5'>{numWon}</Typography>
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
              height='40vh'
              sx={{ mt: 3, p: 2}}
              overflow='auto'
            >
              <Typography variant='h4' sx={{ p: 2}}>Completed Games</Typography>
              <CompletedGames games={games} />
            </Box>
             
          </Box>
      );
    };
}

export default Profile;