import BaseContainer from '../BaseContainer.js';
import NavBar from '../NavBar.js';
import Attribution from './Attribution.js';

import Content from './Content.js';

function About({ user, movesToMake, numChallenges, onLogout, onClickPlay }) {
    return (
        <BaseContainer columns={'16rem 1fr 25rem'}>
          <NavBar 
            user={user}
            movesToMake={movesToMake}
            numChallenges={numChallenges}
            onLogout={onLogout} 
            onClickPlay={onClickPlay}
          />  
          <Content />
          <Attribution />
        </BaseContainer>
    );
}

export default About;