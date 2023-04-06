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
    const [showFriends, setShowFriends] = useState(true);

    const handleClickButton = () => {
        setShowFriends(!showFriends);
    };

    useEffect(() => {
      fetch('/users')
        .then(res => res.json())
        .then(data => {
          setUsers(data);
      });
    }, []);   

    useEffect(() => {
      fetch(`/users/${id}`)
        .then(res => res.json())
        .then(data => setProfileData(data));
      setFriends(users.filter(u => profileData.friend_ids.includes(u.id)));
    }, [id]);    

    return (
        <BaseContainer>
          <NavBar 
            user={user}
            onLogout={onLogout} 
            onClickPlay={onClickPlay}
          />
          <Profile user={user} profileData={profileData}/>
          {showFriends ? 
          <UserList users={users} onClickButton={handleClickButton}/>
          :
          <FriendList users={friends} onClickButton={handleClickButton}/>
          }
        </BaseContainer>
    );
}

export default Social;