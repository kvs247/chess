import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';

import BaseUserList from '../BaseUserList';

function UserList({ users, onClickButton }) {
  
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
            Users
          </Typography>
          <Button
            variant='contained'
            onClick={onClickButton}
          >
            Show Friends
          </Button>
        </BaseUserList>
    );
}

export default UserList;


