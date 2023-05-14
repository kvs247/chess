import { useParams } from 'react-router-dom';
import { useState, useEffect } from 'react';
import ArrowBackIosIcon from '@mui/icons-material/ArrowBackIos';
import ArrowForwardIosIcon from '@mui/icons-material/ArrowForwardIos';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import FirstPageIcon from '@mui/icons-material/FirstPage';
import LastPageIcon from '@mui/icons-material/LastPage';

import { pgnToObj } from '../Util/pgnFenHandler.js';
import { useAppContext } from '../../AppContext.js';
import Board from './Board.js';
import guest from '../../assets/profile-image.png';

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

function GameArea({ staticBoard, flippedBoard, onClickFlip, gameId }) {
  const { user, users, getGames, resetHomeBoard } = useAppContext();
  const { id } = useParams();
  const [isLoaded, setIsLoaded] = useState(false);
  const [rerender, setRerender] = useState(false);
  const [resetBoard, setResetBoard] = useState(false);
  const [gameData, setGameData] = useState({});
  const [isUsersTurn, setIsUsersTurn] = useState(false);
  const [index, setIndex] = useState(-1);

  const handleSetIndex = (value) => {
    const startIndex = -gameData.fen_list.length;

    if (index === -1 && value === 1) return;
    if (index === startIndex && value === -1) return;

    if (value === -2) {
        setIndex(startIndex); 
        return;
    };
    if (value === 2) {
        setIndex(-1); 
        return;
    };

    setIndex(index => index + value);
  };

  const helper = (e) => {
    if (e.key === 'ArrowLeft') handleSetIndex(-1);
    if (e.key === 'ArrowRight') handleSetIndex(1);
  };

  const handleMove = async (
    fromIndex, 
    toIndex, 
    promotion=null, 
    resign=null, 
    draw=null
    ) => {
      if (!gameId) gameId = 0;
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
    
  let whiteUsername;
  let whiteProfileImage;
  let blackUsername;
  let blackProfileImage;
  if (gameData.pgn && users.length > 0) {
    const pgnObj = pgnToObj(gameData.pgn);

    whiteUsername = pgnObj['whiteUsername'];
    whiteProfileImage = users.find(user => user.username === whiteUsername).profile_image;
    
    blackUsername = pgnObj['blackUsername'];
    blackProfileImage = users.find(user => user.username === blackUsername).profile_image;
    
    if (gameData.id === 0) {
      whiteUsername = 'White';
        whiteProfileImage = guest;
        blackUsername = 'Black';
        blackProfileImage = guest;
      };
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
    };
  };
    
  useEffect(() => {
    document.removeEventListener('keydown', helper);
    if (isLoaded) {
      document.addEventListener('keydown', helper);
      return () => document.removeEventListener('keydown', helper);
    };
  // eslint-disable-next-line
  }, [gameData, index]);

  useEffect(() => {
    if (gameData.fen) {
      const whitesTurn = gameData.fen.split(' ')[1] === 'w' ? true : false;
      if (whitesTurn && user.id === gameData.white_user_id) setIsUsersTurn(true)
      else if (!whitesTurn && user.id === gameData.black_user_id) setIsUsersTurn(true)
      else setIsUsersTurn(false);
      };
  }, [user.id, gameData]);
        
  useEffect(() => {
    setRerender(false);
    setResetBoard(false);
    fetch(`/games/${gameId ? gameId : 0}`)
      .then(res => res.json())
      .then(data => {
        setGameData(data)
        setIsLoaded(true)
      });
  }, [gameId, rerender, resetBoard])

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
        index={index}
        resetBoard={resetBoard}
        staticBoard={staticBoard}
        flippedBoard={flippedBoard}
        isUsersTurn={isUsersTurn}
        gameData={gameData}
        onMove={handleMove}
      />
      {flippedBoard ? 
      playerBox(blackUsername, blackProfileImage) :
      playerBox(whiteUsername, whiteProfileImage)}
      {/* Bottom Menu */}
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
          onClick={() => handleSetIndex(-2)}
        >
          <FirstPageIcon sx={{ color: '#e1e1e1', fontSize: '3rem' }} />
        </Button>
        <Button
          onClick={() => handleSetIndex(-1)}
        >
          <ArrowBackIosIcon sx={{ color: '#e1e1e1', fontSize: '2rem' }} />
        </Button>
        <Button
          variant='contained'
          sx ={{ m: 1, }}
          onClick={() => onClickFlip()}
        >
          Flip Board
        </Button> 
        {id ? null : 
          <Button
            variant='contained'
            sx ={{ m: 1, }}
            onClick={() => {
              resetHomeBoard(0);
              setResetBoard(true);
            }}
          >
            Reset Board
          </Button>
        }
        {user.username === whiteUsername || user.username === blackUsername ? 
          <>
          <Button
            variant='contained'
            sx ={{ m: 1, }}
            onClick={() => handleMove(-1, -1, null, user.username, null)}
          >
            Resign
          </Button> 
          {/* <Button
            variant='contained'
            sx = {{ m: 1 }}
          >
            Draw
          </Button> */}
          </>
        : null
        }
        <Button
          onClick={() => handleSetIndex(1)}
        >
          <ArrowForwardIosIcon sx={{ color: '#e1e1e1', fontSize: '2rem' }} />
        </Button>
        <Button
          onClick={() => handleSetIndex(2)}
        >
          <LastPageIcon sx={{ color: '#e1e1e1', fontSize: '3rem' }} />
        </Button>            
      </Box>
    </Box>
  );
}

export default GameArea