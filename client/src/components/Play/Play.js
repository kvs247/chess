import BaseContainer from '../BaseContainer';
import NavBar from '../NavBar';
import GameArea from '../GameArea';

function Play({ user, onLogout, onClickPlay, playComputer }) {
    return (
        <BaseContainer>
            <NavBar 
              user={user}
              onLogout={onLogout}
              onClickPlay={onClickPlay}
            />
            <GameArea user={user} staticBoard={false}/>
        </BaseContainer>

    );
}

export default Play;