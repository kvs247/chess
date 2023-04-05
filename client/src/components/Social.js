import BaseContainer from './BaseContainer';
import NavBar from './NavBar';

import Profile from './Profile';
import ActiveGames from './ActiveGames';

function Social({ user, onLogout, onClickPlay }) {
    return (
        <BaseContainer>
          <NavBar 
            onLogout={onLogout} 
            onClickPlay={onClickPlay}
          />
          <Profile user={user}/>
          <ActiveGames />
        </BaseContainer>
    );
}

export default Social;