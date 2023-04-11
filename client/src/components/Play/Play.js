import { useParams } from 'react-router-dom';

import BaseContainer from '../BaseContainer';
import NavBar from '../NavBar';
import GameArea from '../GameArea';

function Play({ user, users, onLogout, onClickPlay, playComputer }) {

    const { id } = useParams();

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
              staticBoard={false}
              gameId={id}
            />
        </BaseContainer>

    );
}

export default Play;