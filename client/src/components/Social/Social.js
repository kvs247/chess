import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import BaseContainer from '../BaseContainer';
import NavBar from '../NavBar';

import Profile from './Profile';
import UserList from './UserList';
import FriendList from './FriendList';

function Social({ user, users, games, onLogout, onClickPlay }) {

    const { id } = useParams();

    const [profileData, setProfileData] = useState({});
    const [friends, setFriends] = useState([]);
    const [showFriends, setShowFriends] = useState(true);

    const handleClickButton = () => {
        setShowFriends(!showFriends);
    };

    const updateStates = () => {
        const thisPageUser = users.filter(u => u.id == id)[0];
        setProfileData(thisPageUser);
        setFriends(users.filter(u => thisPageUser.friend_ids.includes(u.id)));
    };

    useEffect(() => {
        updateStates();
    }, [users]);   

    useEffect(() => {
      updateStates();
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