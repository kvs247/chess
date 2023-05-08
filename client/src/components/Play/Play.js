import { useState, useEffect, useContext } from 'react';
import { useParams, useHistory } from 'react-router-dom';

import { pgnToObj } from '../Util/pgnFenHandler.js';

import { AppContext } from '../../App.js';
import BaseContainer from '../BaseContainer.js';
import NavBar from '../NavBar.js';
import GameArea from './GameArea.js';
import ActiveGames from './ActiveGames.js';
import MoveList from './MoveList.js';
import Challenges from './Challenges.js';

function Play({ 
    getGames, 
    onLogout, 
    onClickPlay, 
    onClickReset,
    showChallenges,
    selectedColor,
    onChangeColor, 
    onChangeColorComplete 
}) {

    const { user, users, games } = useContext(AppContext);

    const { id } = useParams();
    const history = useHistory();    

    const [moves, setMoves] = useState('');
    const [yourMoveGames, setYourMoveGames] = useState([]);
    const [theirMoveGames, setTheirMoveGames] = useState([]);
    const [activeGamesUsers, setActiveGamesUsers] = useState([]);
    const [receivedChallenges, setReceivedChallenges] = useState([]);
    const [sentChallenges, setSentChallenges] = useState([]);
    const [flippedBoard, setFlippedBoard] = useState(() => {
      const storedFlippedBoard = localStorage.getItem('flippedBoard');
      return storedFlippedBoard ? storedFlippedBoard === 'true' : false;
    });

    useEffect(() => {
        localStorage.setItem('flippedBoard', flippedBoard);
    // eslint-disable-next-line
    }, [flippedBoard]);

    const handleClickFlip = () => {
        setFlippedBoard(!flippedBoard);
        localStorage.setItem('flippedBoard', flippedBoard); 
    };

    useEffect(() => {
      getGames();
    // eslint-disable-next-line
    }, []);

    useEffect(() => {
        fetch('/challenges') 
          .then(res => res.json())
          .then(data => {
              const receivedUserChallenges = data.filter(challenge => challenge.challengee_id === user.id);
              setReceivedChallenges(receivedUserChallenges)

              const sentUserChallenges = data.filter(challenge => challenge.challenger_id === user.id);
              setSentChallenges(sentUserChallenges)
          }) 
    }, [user])

    const handleClickAccept = (id, username) => {
        fetch('/games', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify([
              { id: user.id, username: user.username}, 
              { id, username }
            ])
        })
          .then(res => res.json())
          .then(data => {
              if (user.id === data.black_user_id) {
                  setFlippedBoard(true)
                  localStorage.setItem('flippedBoard', true);
              } else {
                  setFlippedBoard(false)
                  localStorage.setItem('flippedBoard', false);
              };
              history.push(`/play/${data.id}`)
          });
    };

    const handleClickDecline = (challengeId) => {
        fetch(`/challenges/${challengeId}`, {
            method: 'DELETE'
        })
        const newReceivedChallenges = receivedChallenges.filter(
            challenge => challenge.id !== challengeId
        )
        setReceivedChallenges(newReceivedChallenges)
    };

    const handleClickDelete = (challengeId) => {
      fetch(`/challenges/${challengeId}`, {
          method: 'DELETE'
      })
      const newSentChallenges = sentChallenges.filter(
        challenge => challenge.id !== challengeId
        )
        setSentChallenges(newSentChallenges)
      };
      
      
    const receivedChallengeUsers = receivedChallenges.map(c => {
        return {
            challenge: c,
            user: users.find(u => u.id === c.challenger_id)
        }
    });
    const sentChallengeUsers = sentChallenges.map(c => {
        return {
            challenge: c,
            user: users.find(u => u.id === c.challengee_id)
        }
    });
    

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
        

    // eslint-disable-next-line
    }, [games, users, id]);
          
    return (
      <BaseContainer>
        <NavBar 
          selectedColor={selectedColor}
          onChangeColor={onChangeColor}
          onChangeColorComplete={onChangeColorComplete}
        />
        <GameArea 
          user={user} 
          users={users}
          getGames={getGames}
          flippedBoard={flippedBoard}
          onClickFlip={handleClickFlip}
          onClickReset={onClickReset}
          gameId={id}
          selectedColor={selectedColor}
        />
        {id ? 
          <MoveList moves={moves}/> :
          showChallenges ? 
          <Challenges 
            receivedChallengeUsers={receivedChallengeUsers}
            sentChallengeUsers={sentChallengeUsers}
            onClickAccept={handleClickAccept}
            onClickDecline={handleClickDecline}
            onClickDelete={handleClickDelete}            
          /> :
          <ActiveGames
            yourMoveGames={yourMoveGames}
            theirMoveGames={theirMoveGames}
            user={user}
            users={activeGamesUsers}
            setFlippedBoard={setFlippedBoard}
          />
        }
      </BaseContainer>
    );
}

export default Play;