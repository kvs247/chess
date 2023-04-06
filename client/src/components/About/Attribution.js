
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';

function Attribution() {
    return (
        <Box
          bgcolor='secondary.main'
          align='center'
        >
          <Typography
            variant='h5'
            align='center'
            sx={{
              mt: 1,
              mb: 3,
            }}
          >
            Attribution
            </Typography>
            <Box
              sx={{
                mx: 1,
              }}
            >      
              <a href="https://www.flaticon.com/free-icons/chess" title="chess icons">Chess icons created by Flat Icons - Flaticon</a>
              <br />
              <a href="https://www.flaticon.com/free-icons/question-mark" title="question mark icons">Question mark icons created by Freepik - Flaticon</a>
              <br />
              <a href="https://www.flaticon.com/free-icons/people" title="people icons">People icons created by Freepik - Flaticon</a>
              <br />
              <a href="https://www.flaticon.com/free-icons/logout" title="logout icons">Logout icons created by Tempo_doloe - Flaticon</a>
              <br />
              <a href="https://www.flaticon.com/free-icons/user" title="user icons">User icons created by Freepik - Flaticon</a>
            </Box>

        </Box>
    );
}

export default Attribution;