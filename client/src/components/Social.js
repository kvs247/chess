import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import BaseContainer from './BaseContainer';
import NavBar from './NavBar';

import Profile from './Profile';
import ActiveGames from './ActiveGames';

function Social({ user, onLogout, onClickPlay }) {

    const [profileData, setProfileData] = useState({});

    const { id } = useParams();

    useEffect(() => {
      fetch(`/users/${id}`)
        .then(res => res.json())
        .then(data => setProfileData(data));
    }, []);    

    return (
        <BaseContainer>
          <NavBar 
            user={user}
            onLogout={onLogout} 
            onClickPlay={onClickPlay}
          />
          <Profile user={user} profileData={profileData}/>
          <ActiveGames />
        </BaseContainer>
    );
}

export default Social;