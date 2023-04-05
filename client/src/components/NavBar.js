import { useHistory } from 'react-router-dom';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import CardActionArea from '@mui/material/CardActionArea';

import playFriends from '../assets/play-friends.png';
import playComputer from '../assets/play-computer.png';
import social from '../assets/social.png';
import about from '../assets/about.png';
import logout from '../assets/logout.png';


function NavBar({ onLogout, onClickPlay }) {

    const MenuItem = (text, icon, route) => {
      
        const history = useHistory();
        
        return (
            <CardActionArea>
              <Box 
                onClick={() => {
                  switch (text) {
                    case 'Play Friends':
                      onClickPlay(false);
                      break;
                    case 'Play Computer':
                      onClickPlay(true);
                      break;
                    case 'Logout':
                      onLogout();
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
              </Box>
            </CardActionArea>
        );
    };

    return (
        <Box 
        bgcolor='secondary.main'
        >
          <Typography 
            variant='h5' 
            align='center'
            sx={{
              mt: 1,
              mb: 3
            }}
          >
            Chess Is Hard
          </Typography>
          {MenuItem('Play Friends', playFriends, '/play')}
          {MenuItem('Play Computer', playComputer, '/play')}
          {MenuItem('Social', social, '/social')}
          {MenuItem('About', about, '/about')}
          {MenuItem('Logout', logout, '/login')}
        </Box>
    );
}

export default NavBar;