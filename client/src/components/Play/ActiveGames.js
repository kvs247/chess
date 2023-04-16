import { useHistory } from 'react-router-dom';
import Box from '@mui/material/Box';
import CardActionArea from '@mui/material/CardActionArea';
import Typography from '@mui/material/Typography';

import whiteKing from '../../assets/chess-pieces/white-king.png';
import blackKing from '../../assets/chess-pieces/black-king.png';

function ActiveGames({ games, users }) {

    const history = useHistory();
    const handleClick = (gameId) => {
        history.push(`/play/${gameId}`);
    };

    return (
      <Box
        bgcolor='secondary.main'
        align='center'
        overflow='auto'
      >
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
        {games && users[0] ? games.map((game) => {
          const whiteUser = users.find(user => user.id === game.white_user_id);
          const blackUser = users.find(user => user.id === game.black_user_id);
          console.log(game)
          return (
            <CardActionArea key={game.id}>
              <Box
                onClick={() => handleClick(game.id)}
                sx={{
                  bgcolor: 'primary.main',
                  color: '#e1e1e1',
                  width: '90%',
                  display: 'flex',
                  alignItems: 'center',
                  mb: 2,
                }}
              >
                <Typography variant='h6' sx={{ m: 'auto'}}>
                  <Box sx={{ display: 'flex', alignItems: 'center' }}>
                    <Box 
                      component='img'
                      src={whiteKing}
                      alt=''
                      sx={{ 
                        height: '2rem', 
                        width: '2rem', 
                        marginRight: '0.5rem', 
                        marginBottom: '0.2rem' 
                      }}
                    />
                    {whiteUser.username} 
                  </Box>
                    vs 
                  <Box sx={{ display: 'flex', alignItems: 'center' }}>
                    <Box 
                      component='img'
                      src={blackKing}
                      alt=''
                      sx={{ 
                        height: '2rem', 
                        width: '2rem', 
                        marginRight: '0.5rem', 
                        marginBottom: '0.2rem' 
                      }}
                    />
                    {blackUser.username} 
                  </Box>
                  Move {game.fen.split(' ')[5]}
                </Typography>
              </Box>
            </CardActionArea>
          );
        }) : 
        <Typography variant='h7'>
          No active games
        </Typography>
      }
      </Box>
    );

};

export default ActiveGames;