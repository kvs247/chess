import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

import { pgnToObj } from '../Util/pgnFenHandler.js';

import BaseContainer from '../BaseContainer.js';
import NavBar from '../NavBar.js';
import GameArea from '../GameArea.js';
import ActiveGames from './ActiveGames.js';
import MoveList from './MoveList.js';

function Play({ user, users, games, setGames, getGames, onLogout, onClickPlay, playComputer }) {

    const { id } = useParams();

    const [moves, setMoves] = useState('');
    const [yourMoveGames, setYourMoveGames] = useState([]);
    const [theirMoveGames, setTheirMoveGames] = useState([]);

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

    
    useEffect(() => {
        const game = games.find(game => game.id === parseInt(id));
        if (game && game.pgn) setMoves(pgnToObj(game.pgn)['moveList']);

        setYourMoveGames(activeGames.filter(game => {
            // console.log(game);
            const whitesTurn = game.fen.split(' ')[1] === 'w' ? true : false;
            if (whitesTurn && user.id === game.white_user_id) return true;
        }));
        setTheirMoveGames(activeGames.filter(game => {
            if (!yourMoveGames.includes(game)) return true;
        }));
    }, [games, id]);

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
            getGames={getGames}
            staticBoard={id ? false : true}
            gameId={id}
          />
          {id ? 
            <MoveList moves={moves}/> :
            <ActiveGames
              games={activeGames}
              yourMoveGames={yourMoveGames}
              theirMoveGames={theirMoveGames}
              users={activeGamesUsers}
            >
            </ActiveGames>
          }
        </BaseContainer>

    );
}

export default Play;