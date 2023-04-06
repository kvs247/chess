import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import CardActionArea from '@mui/material/CardActionArea';

import magnus from '../../assets/carlsen.jpg'
import hikaru from '../../assets/hikaru.png'
import nepo from '../../assets/nepo.jpeg'
import fischer from '../../assets/fischer.jpg'

const users = [
    {
      username: 'Magnus Carlsen',
      photo: magnus
    },
    {
      username: 'Hikaru Nakamura',
      photo: hikaru
    },
    {
      username: 'Ian Nepomniachtchi',
      photo: nepo
    },
    {
      username: 'Bobby Fischer',
      photo: fischer
    }
]

function ActiveGames() {
    return (
        <Box bgcolor='secondary.main' align='center'>
          <Typography
            variant='h5'
            align='center'
            sx={{
              mt: 1,
              mb: 3,
            }}
          >
            Active Games
          </Typography>
          {users.map((user) => {
            return (
                <CardActionArea key={user.username}>
                  <Box
                    sx={{
                      bgcolor: 'primary.main',
                      color: '#e1e1e1',
                      width: '90%',
                      display: 'flex',
                      alignItems: 'center',
                      mb: 2,
                    }}
                  >
                    <Box
                      component='img'
                      alt=''
                      src={user.photo}
                      sx={{
                        width: 50,
                        mr: 2,
                      }}
                    />
                    {`${user.username}`}
                  </Box>
                </CardActionArea>
            );
          })}
        </Box>
    );
}

export default ActiveGames;