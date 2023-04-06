import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';

import moment from 'moment';

function CompletedGames({ games }) {

    //will need to filter for completed games

    const formattedGames = games.map(game => {

        const whiteUsernameRegex = /White "(.*)"/; 
        const whiteUsername = whiteUsernameRegex.exec(game.pgn)[1];
        const blackUsernameRegex = /Black "(.*)"/; 
        const blackUsername = blackUsernameRegex.exec(game.pgn)[1];

        const moves = game.pgn.split('\n').slice(-1)[0];
        
        const result = moves.split(' ').slice(-1)[0];

        const movesRegex = /\d+\./g;
        const moveInts = moves.match(movesRegex).map(str => parseInt(str.slice(0,-1)));
        const numMoves = Math.max(...moveInts);

        const dateRegex = /EndDate "(.*)"/;
        const dateRaw = dateRegex.exec(game.pgn)[1];
        const yyyymmdd = dateRaw.split('-');
        const date = new Date(yyyymmdd[0], yyyymmdd[1]-1, yyyymmdd[2]);
        const formattedDate = moment(date).format('MMMM D Y');

        return {
            whiteUsername: whiteUsername,
            blackUsername: blackUsername,
            result: result,
            moves: numMoves,
            date: formattedDate
        };
    });

    const testGames = [
        {
          id: 1,
          date: 'Mar 24, 2023',
          whiteUsername: 'John Doe',
          blackUsername: 'Jane Smith',
          result: '1-0',
          moves: 39,
        },
        {
          id: 2,
          date: 'Mar 22, 2023',
          whiteUsername: 'Bob Johnson',
          blackUsername: 'Alice Lee',
          result: '0-1',
          moves: 9,
        },
        // add more game entries
      ];


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
              <Box 
                sx={{ 
                  mx: 4,
                  bgcolor: 'primary.main',
                  display: 'flex',
                  flexDirection: 'row',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  padding: '16px',
                }}
              >
                <Box sx={{ flexBasis: '25%' }}>
                  <Typography variant="h6" gutterBottom>
                    {game.whiteUsername}
                  </Typography>
                  <Typography variant="h6" gutterBottom>
                    {game.blackUsername}
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
            </Grid>
          );
        })}
      </Grid>
    );
}

export default CompletedGames;