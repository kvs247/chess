import BaseContainer from '../BaseContainer.js';
import NavBar from '../NavBar.js';
import Attribution from './Attribution.js';

function About({ user, onLogout, onClickPlay }) {
    return (
        <BaseContainer>
          <NavBar 
            user={user}
            onLogout={onLogout} 
            onClickPlay={onClickPlay}
          />  
          <h1>About</h1>
          <Attribution />
        </BaseContainer>
    );
}

export default About;