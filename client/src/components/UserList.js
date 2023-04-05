import { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import CardActionArea from '@mui/material/CardActionArea';
import { TextField } from '@mui/material';
import Button from '@mui/material/Button';

function UserList({ onClickButton }) {

    const history = useHistory();

    const [users, setUsers] = useState([]);
    const [filteredUsers, setFilteredUsers] = useState([]);

    useEffect(() => {
      fetch('/users')
        .then(res => res.json())
        .then(data => {
          setUsers(data);
          setFilteredUsers(data);
        });
    }, [])

    const handleClickUser = (user) => {
        history.push(`/users/${user.id}`);
        window.location.reload();
    };

    const handleChange = (event) => {
        const search = event.target.value.toLowerCase();
        setFilteredUsers(users.filter(user => {
            const usernameBoolean = user.username.toLowerCase().includes(search);
            const fullNameBoolean = user.full_name.toLowerCase().includes(search);
            const emailBoolean = user.email.toLowerCase().includes(search);
            return usernameBoolean || fullNameBoolean || emailBoolean;
        }));
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
            Users
          </Typography>
          <Button
            variant='contained'
            onClick={onClickButton}
          >
            Show Friends
          </Button>
          <TextField
            onChange={(event) => handleChange(event)}
            margin='normal'
            id='search'
            label='Search'
            name='search'
            color='secondary'
          />
          {filteredUsers.map((user) => {
            return (
                <CardActionArea key={user.username}>
                  <Box
                    onClick={() => handleClickUser(user)}
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
                      src={user.profile_image}
                      sx={{
                        width: 50,
                        mr: 2,
                      }}
                    />
                    {`${user.username}`}
                  </Box>
                </CardActionArea>
            );
          })}
        </Box>
    );
}

export default UserList;