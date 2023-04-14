import { useState, useEffect } from 'react';
import Box from '@mui/material/Box';

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

function GameArea({ user, users, staticBoard, gameId }) {

    const initialGameData = {
        id: 0,
        white_user_id: 0,
        black_user_id: 0,
        pgn: '',
        fen: ''
    };
    const [rerender, setRerender] = useState(false);
    const [gameData, setGameData] = useState({});

    useEffect(() => {
        getGameData();
        setRerender(false);
    }, [gameId, rerender])

    const handleMove = async (fromIndex, toIndex) => {
        const response = await fetch(`/games/${gameId}`, {
            method: 'PATCH',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ fromIndex, toIndex })
          }) 
          .then(res => res.json())
        
        setRerender(true)

        return response;
    };

    const getGameData = () => {
        if (!gameId) gameId = 1;
        fetch(`/games/${gameId}`)
          .then(res => res.json())
          .then(data => setGameData(data));
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
      
      if (gameData.id == 1) {
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
            }}          
          >
            {gameData.fen ? message : null}
          </Box>
          {playerBox(blackUsername, blackProfileImage)}
          <Board 
            length={length} 
            staticBoard={staticBoard}
            gameData={gameData}
            onMove={handleMove}
          />
          {playerBox(whiteUsername, whiteProfileImage)}
        </Box>
    );
}

export default GameArea