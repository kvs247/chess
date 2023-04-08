import { useState } from 'react';
import Draggable from 'react-draggable';
import Box from '@mui/material/Box';

import piecePngObj from './Util/piecePNGs';

const lightSquare = '#c4c4c4';
const darkSquare = '#005c28';

function fenToArray(fen) {
  const piecesString = fen.split(' ')[0].replace(/\//g, '');
  const piecesArrayNums = piecesString.split('');
  const piecesArray = piecesArrayNums.map(piece => {
    if (parseInt(piece)) {
      return [...Array(parseInt(piece)).fill(null)];
    };
    return piece;
  }).flat();
  return piecesArray;
}

const fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1';
const fenArray = fenToArray(fen);

function getInitialPositions() {
    const positions = {};
    for (let i = 0; i < 64; i++) {
        positions[i] = { x: 0, y: 0 };
    };
    return positions;
}
const initialPositions = getInitialPositions();

function Board({ length, staticBoard }) {

    const [positions, setPositions] = useState(initialPositions);

    const squareLength = (window.innerHeight * (length.replace('vh', '') / 100)) / 8;
    const squares = [];

    const onStart = () => {
        setPositions(initialPositions);
    };

    const onStop = (i) => {
        const deltaX = positions[i].x;
        const deltaY = positions[i].y;

        const fromIndex = i;
        const toIndex = i + Math.round(deltaX / squareLength) + Math.round(deltaY / squareLength) * 8;

        console.log(fromIndex, toIndex);
    };

    const handleDrag = (e, ui, id) => {
      const { x, y } = positions[id];
      setPositions((positions) => {
        const newPositions = { ...positions };
        newPositions[id] = { x: x + ui.deltaX, y: y + ui.deltaY };
        return newPositions
      });
    };


    for (let i = 0; i < 64; i++) {

        const row = Math.floor(i / 8);
        const color = (row % 2 === 0 && i % 2 === 0) || 
                      (row % 2 === 1 && i % 2 === 1) 
                      ? lightSquare : darkSquare;

        const pieceImg = (
            <Box 
              draggable='false'
              component='img'
              src={piecePngObj[`${fenArray[i]}`]}
              alt=''
              sx={{ maxWidth: "100%", maxHeight: "100%" }}
          />
        );

        squares.push(
            <Box 
              key={i}
              bgcolor={color}
              sx={{
                width: "100%",
                height: "100%",
                backgroundColor: color,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
              }}
            >
              {staticBoard ? pieceImg : 
                <Draggable
                  bounds='.board-container'
                  onStart={onStart}
                  onStop={() => onStop(i)}
                  onDrag={(e, ui) => handleDrag(e, ui, i)}
                >
                  {pieceImg}
                </Draggable>
              }
            </Box>
          );
    };

    return (
        <Box
          className='board-container'
          sx={{
            height: length,
            width: length,
            display: 'grid',
            gridTemplateColumns: 'repeat(8, 1fr)',
            gridTemplateRows: 'repeat(8, 1fr)',
            position: 'relative',
          }}
        >
          {squares}
        </Box>
    );
}

export default Board;