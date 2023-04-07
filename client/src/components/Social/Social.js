import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import BaseContainer from '../BaseContainer';
import NavBar from '../NavBar';

import Profile from './Profile';
import UserList from './UserList';
import FriendList from './FriendList';

function Social({ user, onLogout, onClickPlay }) {

    const { id } = useParams();

    const [profileData, setProfileData] = useState({});
    const [users, setUsers] = useState([]);
    const [friends, setFriends] = useState([]);
    const [games, setGames] = useState([]);
    const [showFriends, setShowFriends] = useState(true);

    const handleClickButton = () => {
        setShowFriends(!showFriends);
    };
    
    const getUsers = () => {
      fetch('/users')
        .then(res => res.json())
        .then(data => {
          const thisPageUser = data.filter(u => u.id == id)[0];
          setUsers(data);
          setProfileData(thisPageUser);
          setFriends(data.filter(u => thisPageUser.friend_ids.includes(u.id)));
      });
    };

    const getGames = () => {
      fetch('/games')
        .then(res => res.json())
        .then(data => setGames(data));
    };

    useEffect(() => {

      getUsers();

      getGames();

    }, []);   

    useEffect(() => {
      // fetch(`/users/${id}`)
      //   .then(res => res.json())
      //   .then(data => setProfileData(data));
      const thisPageUser = users.filter(u => u.id == id)[0];
      setProfileData(thisPageUser);
      setFriends(users.filter(u => thisPageUser.friend_ids.includes(u.id)));
    }, [id]);    

    const filteredGames = games.filter(u => {
      return u.white_user_id == id || u.black_user_id == id;
    });

    return (
        <BaseContainer>
          <NavBar 
            user={user}
            onLogout={onLogout} 
            onClickPlay={onClickPlay}
          />
          <Profile 
            user={user}   
            profileData={profileData}
            games={filteredGames}
          />
          {showFriends ? 
          <UserList users={users} onClickButton={handleClickButton}/>
          :
          <FriendList users={friends} onClickButton={handleClickButton}/>
          }
        </BaseContainer>
    );
}

export default Social;