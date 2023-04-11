import BaseContainer from '../BaseContainer';
import NavBar from '../NavBar';
import ActiveGames from './ActiveGames';
import GameArea from '../GameArea';

function Home({ user, users, onLogout, onClickPlay }) {
  return (
      <BaseContainer>
        <NavBar 
          user={user}
          onLogout={onLogout} 
          onClickPlay={onClickPlay}
        />
        <GameArea 
          user={user}   
          users={users}
          staticBoard={true} 
        />
        <ActiveGames />
      </BaseContainer>
  );
}

export default Home;