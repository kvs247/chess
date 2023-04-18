import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

import { pgnToObj } from '../Util/pgnFenHandler.js';

import BaseContainer from '../BaseContainer.js';
import NavBar from '../NavBar.js';
import GameArea from '../GameArea.js';
import ActiveGames from './ActiveGames.js';
import MoveList from './MoveList.js';

function Play({ user, users, games, setGames, getGames, onLogout, onClickPlay, playComputer }) {

    console.log('Play.js: users', users)

    const { id } = useParams();

    const [moves, setMoves] = useState('');
    const [yourMoveGames, setYourMoveGames] = useState([]);
    const [theirMoveGames, setTheirMoveGames] = useState([]);
    const [activeGamesUsers, setActiveGamesUsers] = useState([]);
    
    useEffect(() => {
      getGames();
    // eslint-disable-next-line
    }, []);

    useEffect(() => {


        const game = games.find(game => game.id === parseInt(id));
        if (game && game.pgn) setMoves(pgnToObj(game.pgn)['moveList']);
        const activeGames = games.filter(game => {
            const pgnObj = pgnToObj(game.pgn);
            const inProgress = pgnObj['result'] === '*'
            const isWhite = pgnObj['whiteUsername'] === user.username;
            const isBlack = pgnObj['blackUsername'] === user.username;
            return inProgress && (isWhite || isBlack);
          });
        const activeGamesUserIds = activeGames.map(game => {
          return [game['white_user_id'], game['black_user_id']]
        }).flat();

        console.log('activeGames', activeGames)
        
        
        setActiveGamesUsers(users.filter(user => {
          return activeGamesUserIds.includes(user.id)
        }));
        
        setYourMoveGames(activeGames.filter(game => {
          const whitesTurn = game.fen.split(' ')[1] === 'w' ? true : false;
          let result = false
          if (whitesTurn && user.id === game.white_user_id) result = true;
          if (!whitesTurn && user.id === game.black_user_id) result = true;
          return result
        }));

        setTheirMoveGames(activeGames.filter(game => {
          const whitesTurn = game.fen.split(' ')[1] === 'w' ? true : false;
          let result = false
          if (!whitesTurn && user.id === game.white_user_id) result = true;
          if (whitesTurn && user.id === game.black_user_id) result = true;
          return result
        }));
        
        // setTheirMoveGames(activeGames.filter(game => {
        //   return !yourMoveGames.includes(game)
        //   }));
    // eslint-disable-next-line
    }, [games, users, id]);
          
          
          console.log('games', games.sort((a, b) => a.id - b.id))
          console.log('yourMoveGames', yourMoveGames)
          console.log('theirMoveGames', theirMoveGames)
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