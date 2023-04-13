import { useParams } from 'react-router-dom';

import { pgnToObj } from '../Util/pgnFenHandler.js';

import BaseContainer from '../BaseContainer.js';
import NavBar from '../NavBar.js';
import GameArea from '../GameArea.js';
import ActiveGames from './ActiveGames.js';

function Play({ user, users, games, onLogout, onClickPlay, playComputer }) {

    const { id } = useParams();

    const activeGames = games.filter(game => {
        const pgnObj = pgnToObj(game.pgn);
        const inProgress = pgnObj['result'] == '*'
        const isWhite = pgnObj['whiteUsername'] === user.username;
        const isBlack = pgnObj['blackUsername'] === user.username;
        return inProgress && (isWhite || isBlack);
    });
    const activeGamesUserIds = activeGames.map(game => {
        return [game['white_user_id'], game['black_user_id']]
    }).flat();
    const activeGamesUsers = users.filter(user => {
      return activeGamesUserIds.includes(user.id)
    });

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
            staticBoard={id ? false : true}
            gameId={id}
          />
          {id ? null :
            <ActiveGames
              games={activeGames}
              users={activeGamesUsers}
            >
            </ActiveGames>
          }
        </BaseContainer>

    );
}

export default Play;