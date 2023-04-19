import BaseContainer from '../BaseContainer.js';
import NavBar from '../NavBar.js';
import Attribution from './Attribution.js';

function About({ user, movesToMake, numChallenges, onLogout, onClickPlay }) {
    return (
        <BaseContainer>
          <NavBar 
            user={user}
            movesToMake={movesToMake}
            numChallenges={numChallenges}
            onLogout={onLogout} 
            onClickPlay={onClickPlay}
          />  
          <h1>About</h1>
          <Attribution />
        </BaseContainer>
    );
}

export default About;