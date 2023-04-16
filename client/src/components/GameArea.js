import { useState, useEffect } from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';

import Board from './Board.js';
import { pgnToObj } from './Util/pgnFenHandler.js';

import guest from '../assets/profile-image.png';

const length = '75vh';

const playerBox = (username, photo) => {
  return (
    <Box
      sx={{
        width: length,
        display: 'flex',
        alignItems: 'center',
        my: 1,
        color: '#e1e1e1',
      }}
    >
      <Box 
        component='img'
        src={photo}
        alt=''
        sx={{
          width: 50,
          mr: 1,
          borderRadius: '5px',
        }}
      />
      {`${username}`}
  </Box>
  );
};

function GameArea({ user, users, getGames, staticBoard, gameId }) {

    // const initialGameData = {
    //     id: 0,
    //     white_user_id: 0,
    //     black_user_id: 0,
    //     pgn: '',
    //     fen: ''
    // };
    const [rerender, setRerender] = useState(false);
    const [gameData, setGameData] = useState({});
    const [flippedBoard, setFlippedBoard] = useState(false);
    const [isUsersTurn, setIsUsersTurn] = useState(false);

    useEffect(() => {
        setFlippedBoard(user.id === gameData.black_user_id);
        if (gameData.fen) {
            const whitesTurn = gameData.fen.split(' ')[1] === 'w' ? true : false;
            console.log('whitesTurn', whitesTurn);
            if (whitesTurn && user.id === gameData.white_user_id) setIsUsersTurn(true)
            else if (!whitesTurn && user.id === gameData.black_user_id) setIsUsersTurn(true)
            else setIsUsersTurn(false);
        };
    }, [gameData]);
    
    useEffect(() => {
      setRerender(false);
      fetch(`/games/${gameId ? gameId : 1}`)
        .then(res => res.json())
        .then(data => setGameData(data));
    }, [gameId, rerender])

    const handleMove = async (
      fromIndex, 
      toIndex, 
      promotion=null, 
      resign=null, 
      draw=null
    ) => {
        const response = await fetch(`/games/${gameId}`, {
            method: 'PATCH',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 
              fromIndex, 
              toIndex ,
              promotion,
              resign,
              draw              
            })
          }) 
          .then(res => res.json())
        getGames();
        setRerender(true)

        return response;
    };

    let whiteUsername = 'White';
    let whiteProfileImage = guest;
    let blackUsername = 'Black';
    let blackProfileImage = guest;
    if (gameData.pgn && users.length > 0) {
      const pgnObj = pgnToObj(gameData.pgn);

      whiteUsername = pgnObj['whiteUsername'];
      whiteProfileImage = users.find(user => user.username === whiteUsername).profile_image;
      
      blackUsername = pgnObj['blackUsername'];
      blackProfileImage = users.find(user => user.username === blackUsername).profile_image;
      
      if (gameData.id === 1) {
          whiteUsername = 'White';
          whiteProfileImage = guest;
          blackUsername = 'Black';
          blackProfileImage = guest;
      }
          
    };

    const pgnObj = pgnToObj(gameData.pgn);
    if (pgnObj['result'] !== '*') staticBoard = true;

    let message = '';
    if (gameData.fen) {
        message = gameData.fen.split(' ')[1] === 'w' ? 'White\'s Turn' : 'Black\'s Turn';
        if (pgnObj['result'] !== '*') {
              if (pgnObj['result'] === '1/2-1/2') message = 'Draw';
              if (pgnObj['result'] === '1-0') message = 'White Wins';
              if (pgnObj['result'] === '0-1') message = 'Black Wins';
        }
    };

    return (
        <Box 
          bgcolor='primary.main' 
          align='center' 
          my='auto'
        >
          <Box
            sx={{
              width: length,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              my: 1,
              color: '#e1e1e1',
              bgcolor: 'secondary.main',
            }}          
          >
            {gameData.fen ? message : null}
          </Box>
          {flippedBoard ? 
          playerBox(whiteUsername, whiteProfileImage) :
          playerBox(blackUsername, blackProfileImage)} 
          <Board 
            length={length} 
            staticBoard={staticBoard}
            flippedBoard={flippedBoard}
            isUsersTurn={isUsersTurn}
            gameData={gameData}
            onMove={handleMove}
          />
          {flippedBoard ? 
          playerBox(blackUsername, blackProfileImage) :
          playerBox(whiteUsername, whiteProfileImage)}
          <Box
            sx={{
              width: length,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              my: 1,
              color: '#e1e1e1',
              bgcolor: 'secondary.main',
            }}               
          >
            <Button
              variant='contained'
              sx ={{ m: 1, }}
              onClick={() => setFlippedBoard(!flippedBoard)}
            >
              Flip Board
            </Button> 
            {user.username === whiteUsername || user.username === blackUsername ? 
              <>
              <Button
                variant='contained'
                sx ={{ m: 1, }}
                onClick={() => handleMove(-1, -1, null, user.username, null)}
              >
                Resign
              </Button> 
              <Button
                variant='contained'
                sx = {{ m: 1 }}
              >
                Draw
              </Button>
              </>
            : null
            }
          </Box>
        </Box>
    );
}

export default GameArea