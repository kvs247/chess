import { useHistory } from 'react-router-dom';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import CardActionArea from '@mui/material/CardActionArea';

import { pgnToObj } from '../Util/pgnFenHandler.js'

import whiteKing from '../../assets/chess-pieces/white-king.png';
import blackKing from '../../assets/chess-pieces/black-king.png';

function CompletedGames({ games }) {
  
    //will need to filter for completed games
    const history = useHistory();
    const reversedGames = games.slice().reverse();
    const formattedGames = reversedGames.map(game => {
      
        const pgnObj = pgnToObj(game.pgn);

        const movesRegex = /\d+\./g;
        let moveInts = [];
        if (pgnObj['moveList'].match(movesRegex)) {
            moveInts = pgnObj['moveList'].match(movesRegex).map(str => parseInt(str.slice(0,-1)));
        }
        const numMoves = Math.max(...moveInts);

        return {
            id: game.id,
            whiteUsername: pgnObj['whiteUsername'],
            blackUsername: pgnObj['blackUsername'],
            result: pgnObj['result'],
            moves: numMoves,
            date: pgnObj['date']
        };
    });

    return (
      <Grid container spacing={3}>
        {/* Headers */}
        <Grid item xs={12}>
          <Box 
            sx={{ 
              mx: 4,
              bgcolor: 'primary.main',
              display: 'flex',
              flexDirection: 'row',
              alignItems: 'center',
              justifyContent: 'space-between',
              padding: '16px',
              fontWeight: 'bold',
              color: 'white',
            }}
          >
            <Box sx={{ flexBasis: '25%' }}>
              <Typography variant="h5" gutterBottom>
                Players
              </Typography>
            </Box>
            <Box sx={{ flexBasis: '25%' }}>
              <Typography variant="h5" gutterBottom>
                Result
              </Typography>
            </Box>
            <Box sx={{ flexBasis: '25%' }}>
              <Typography variant="h5" gutterBottom>
                Moves
              </Typography>
            </Box>            
            <Box sx={{ flexBasis: '25%' }}>
              <Typography variant="h5" gutterBottom>
                Date
              </Typography>
            </Box>
          </Box>
        </Grid>
        {/* Games */}
        {formattedGames.map((game, index) => {
          return (
            <Grid item xs={12} key={index}>
              <CardActionArea disableRipple>
                <Box 
                  onClick={() => history.push(`/play/${game.id}`)}
                  sx={{ 
                    mx: 4,
                    bgcolor: 'primary.main',
                    display: 'flex',
                    flexDirection: 'row',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    padding: '16px',
                    color: '#E1E1E1',
                  }}
                >
                  <Box sx={{ flexBasis: '25%' }}>
                    <Typography variant="h6" gutterBottom>
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
                        {game.whiteUsername} 
                      </Box>
                    </Typography>
                    <Typography variant="h6" gutterBottom>
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
                          {game.blackUsername} 
                        </Box>
                    </Typography>                                                      
                  </Box>
                  <Box sx={{ flexBasis: '25%' }}>
                    <Typography variant="h6" gutterBottom>
                      {game.result}
                    </Typography>
                  </Box>
                  <Box sx={{ flexBasis: '25%' }}>
                    <Typography variant="h6" gutterBottom>
                      {game.moves}
                    </Typography>
                  </Box>
                  <Box sx={{ flexBasis: '25%' }}>
                    <Typography variant="h6" gutterBottom>
                      {game.date}
                    </Typography>
                  </Box>
                </Box>

              </CardActionArea>
            </Grid>
          );
        })}
      </Grid>
    );
}

export default CompletedGames;