import { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import Box from '@mui/material/Box';
import CardActionArea from '@mui/material/CardActionArea';
import TextField from '@mui/material/TextField';

function BaseUserList({ children, users }) {

  
    const history = useHistory();
    
    const [filteredUsers, setFilteredUsers] = useState([]);

    useEffect(() => {
      setFilteredUsers(users);
    }, [users]);
    
    const handleClickUser = (user) => {
      history.push(`/users/${user.id}`);
    };
    
    // search functionality
    const handleChange = (event) => {
      const search = event.target.value.toLowerCase();
      setFilteredUsers(users.filter(user => {
        const usernameBoolean = user.username.toLowerCase().includes(search);
        const fullNameBoolean = user.full_name.toLowerCase().includes(search);
        const emailBoolean = user.email.toLowerCase().includes(search);
        return usernameBoolean || fullNameBoolean || emailBoolean;
      }));
    };
  
    users.sort((a, b) => a.username.localeCompare(b.username));

    return (
        <Box 
          bgcolor='secondary.main' 
          align='center'
          overflow='auto'
        >
          {children}
          <TextField
            onChange={(event) => handleChange(event)}
            margin='normal'
            id='search'
            label='Search'
            name='search'
            color='secondary'
          />
          {users ? filteredUsers.map((user) => {
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
          }) : null}
        </Box>
    );
}

export default BaseUserList;