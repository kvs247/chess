import Attribution from './Attribution.js';
import BaseContainer from '../BaseContainer.js';
import Content from './Content.js';
import NavBar from '../NavBar.js';

function About() {
    return (
        <BaseContainer columns={'16rem 1fr 25rem'}>
          <NavBar />  
          <Content />
          <Attribution />
        </BaseContainer>
    );
}

export default About;