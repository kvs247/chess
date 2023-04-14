import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import CardActionArea from '@mui/material/CardActionArea';
import CheckIcon from '@mui/icons-material/Check';
import CloseIcon from '@mui/icons-material/Close';

function Challenges({ 
    receivedChallengeUsers, 
    sentChallengeUsers, 
    onClickDelete, 
    onClickDecline, 
    onClickAccept 
}) {

    return (
        <Box 
          bgcolor='secondary.main' 
          align='center' 
          overflow='auto'
        >
          <Typography
            variant='h5'
            align='center'
            sx={{ mt: 1, mb: 3 }}
          >
            Challenges
          </Typography>

          {/* Recieved */}
          <Typography
            variant='h6'
            align='center'
            sx={{ mt: 1, mb: 3 }}
          >
            Received
          </Typography>
          {receivedChallengeUsers ? receivedChallengeUsers.map((challengeUser, index) => {
            return (
                <Box
                  key={challengeUser.challenge.id}
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
                    src={challengeUser.user ? challengeUser.user.profile_image : ''}
                    sx={{
                      width: 50,
                      mr: 2,
                    }}
                  />
                  <Typography textAlign='center' mx='auto'>
                    {challengeUser.user ? `${challengeUser.user.username}` : null}
                    <br />
                    {`${challengeUser.challenge.date_created.split(' ')[0]}`}
                  </Typography>
                  <Box sx={{ ml: 'auto' }}>
                    <CardActionArea
                      onClick={() => {
                        onClickDecline(challengeUser.challenge.id);
                        onClickAccept(challengeUser.user.id, challengeUser.user.username);
                      }}
                    >
                      <CheckIcon sx={{ mr: 1 }} />
                    </CardActionArea>
                    <CardActionArea
                      onClick={() => onClickDecline(challengeUser.challenge.id)}
                    >
                      <CloseIcon sx={{ mr: 1 }} />
                    </CardActionArea>
                  </Box>
                </Box>
            );
          }) : null}

          {/* Sent */}
          <Typography
            variant='h6'
            align='center'
            sx={{ mt: 1, mb: 3 }}
          >
            Sent
          </Typography>
          {sentChallengeUsers ? sentChallengeUsers.map((challengeUser, index) => {
            return (
                <Box
                  key={challengeUser.challenge.id}
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
                    src={challengeUser.user ? challengeUser.user.profile_image : ''}
                    sx={{
                      width: 50,
                      mr: 2,
                    }}
                  />
                  <Typography textAlign='center' mx='auto'>
                    {`${challengeUser.user ? challengeUser.user.username : ''}`}
                    <br />
                    {`${challengeUser.challenge.date_created.split(' ')[0]}`}
                  </Typography>
                  <Box sx={{ ml: 'auto' }}>
                    <CardActionArea
                      onClick={() => onClickDelete(challengeUser.challenge.id)}
                    >
                      <CloseIcon sx={{ mr: 1 }} />
                    </CardActionArea>
                  </Box>
                </Box>
            );
          }) : null}
        </Box>
    );
}

export default Challenges;