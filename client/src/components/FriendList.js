import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';

import BaseUserList from './BaseUserList';

function FriendList({ users, onClickButton }) {
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
            Friends
          </Typography>
          <Button
            variant='contained'
            onClick={onClickButton}
          >
            Show Users
          </Button>
        </BaseUserList>
    );
}

export default FriendList;