import BaseContainer from '../BaseContainer';
import NavBar from '../NavBar';
import ActiveGames from '../ActiveGames';
import GameArea from './GameArea';

function Home({ user, onLogout, onClickPlay }) {
  return (
      <BaseContainer>
        <NavBar 
          user={user}
          onLogout={onLogout} 
          onClickPlay={onClickPlay}
        />
        <GameArea user={user} />
        <ActiveGames />
      </BaseContainer>
  );
}

export default Home;