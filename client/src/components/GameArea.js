import { useState, useEffect } from 'react';
import Box from '@mui/material/Box';

import Board from './Board.js';

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

function GameArea({ user, staticBoard, gameId }) {

    const handleMove = async (fromIndex, toIndex) => {
        const responseFen = await fetch(`/games/${gameId}`, {
            method: 'PATCH',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ fromIndex, toIndex })
          })
          .then(res => res.json())    
        
        setRerender(true)

        return responseFen;
    };

    const [rerender, setRerender] = useState(false);
    const [fen, setFen] = useState(null);

    const getGameData = () => {
        fetch(`/games/${gameId}`)
          .then(res => res.json())
          .then(data => setFen(data.fen));
    };

    useEffect(() => {
        getGameData();
        setRerender(false);
    }, [gameId, rerender])

    return (
        <Box 
          bgcolor='primary.main' 
          align='center' 
          my='auto'
        >
          {playerBox('Opponent', guest)}
          <Board 
            length={length} 
            staticBoard={staticBoard}
            fen={fen}
            onMove={handleMove}
          />
          {playerBox(user.username, user.profile_image)}
        </Box>
    );
}

export default GameArea