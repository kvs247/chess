import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import CardActionArea from '@mui/material/CardActionArea';

import BaseUserList from '../BaseUserList';

function ActiveGames({ users }) {
    return (
        <BaseUserList users={users}>
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
        </BaseUserList>
    );

};

export default ActiveGames;