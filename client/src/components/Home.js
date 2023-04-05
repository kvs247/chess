import BaseContainer from './BaseContainer';
import NavBar from './NavBar';
import ActiveGames from './ActiveGames';
import PlayArea from './PlayArea';

function Home({ user, onLogout, onClickPlay }) {
  return (
      <BaseContainer>
        <NavBar 
          onLogout={onLogout} 
          onClickPlay={onClickPlay}
        />
        <PlayArea user={user} />
        <ActiveGames />
      </BaseContainer>
  );
}

export default Home;