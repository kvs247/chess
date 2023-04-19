import { useHistory } from 'react-router-dom';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import CardActionArea from '@mui/material/CardActionArea';

import playFriends from '../assets/play-friends.png';
import playComputer from '../assets/play-computer.png';
import social from '../assets/social.png';
import about from '../assets/about.png';
import logout from '../assets/logout.png';
import sword from '../assets/sword.png';


function NavBar({ user, movesToMake, numChallenges, onLogout, onClickPlay }) {
  
    const history = useHistory();

    const MenuItem = (text, icon, route) => {
      
        return (
            <CardActionArea>
              <Box 
                onClick={() => {
                  switch (text) {
                    case 'Active Games':
                      onClickPlay(false);
                      break;
                    case 'Challenges':
                      onClickPlay(true);
                      break;
                    case 'Logout':
                      onLogout();
                      break;
                    default:
                      break;
                  };
                  history.push(route);
                }}
                sx={{ 
                color: '#e1e1e1', 
                display: 'flex', 
                alignItems: 'center',
                pointer: 'cursor', 
              }}
              >
              <Box
                component='img'
                alt=''
                src={icon}
                sx={{
                  width: 50,
                  m: 2,
                }}
              />
                {`${text}`}
                {/* your move */}
                {text === 'Active Games' && movesToMake > 0 ? 
                <Box
                  sx={{ 
                    ml: 2, 
                    bgcolor: 'red',
                    borderRadius: '25%',
                    width: 15,
                    height: 15,
                    display: 'flex',
                    justifyContent: 'center',                
                  }}
                >
                  {movesToMake}
                </Box> : null}
                {/* challenges */}
                {text === 'Challenges' && numChallenges > 0 ? 
                <Box
                  sx={{ 
                    ml: 2, 
                    bgcolor: 'red',
                    borderRadius: '25%',
                    width: 15,
                    height: 15,
                    display: 'flex',
                    justifyContent: 'center',                
                  }}
                >
                  {numChallenges}
                </Box> : null}    
              </Box>
            </CardActionArea>
        );
    };

    return (
        <Box 
        bgcolor='secondary.main'
        >
          <CardActionArea disableRipple>
            <Typography 
              variant='h5' 
              align='center'
              sx={{
                mt: 1,
                mb: 3
              }}
              onClick={() => history.push('/home')}
            >
              Chess Is Hard
            </Typography>
          </CardActionArea>
          {MenuItem('Active Games', playFriends, '/play')}
          {MenuItem('Challenges', sword, '/play')}
          {MenuItem('Social', social, `/users/${user.id}`)}
          {MenuItem('About', about, '/about')}
          {MenuItem('Logout', logout, '/login')}
        </Box>
    );
}

export default NavBar;