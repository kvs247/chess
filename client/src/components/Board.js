import Box from '@mui/material/Box';
import Draggable from 'react-draggable';

const lightSquare = '#c4c4c4';
const darkSquare = '#005c28';

const fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1';

const fenToArray = (fen) => {
    const piecesString = fen.split(' ')[0].replace('/', '');
    console.log(piecesString)
};

console.log('yo', fenToArray(fen));

function Board({ length }) {

    const squares = [];

    for (let i = 0; i < 64; i++) {

        const row = Math.floor(i / 8);
        const color = (row % 2 === 0 && i % 2 === 0) || 
                      (row % 2 === 1 && i % 2 === 1) 
                      ? lightSquare : darkSquare;

        squares.push(
            <Box 
              key={i}
              bgcolor={color}
              width = '100%'
              height = '100%'
            >
            </Box>
          );
    };

    return (
        <Box
          sx={{
            backgroundColor: 'blue',
            height: length,
            width: length,
            display: 'grid',
            gridTemplateColumns: 'repeat(8, 1fr)',
            gridTemplateRows: 'repeat(8, 1fr)',
          }}
        >
          {squares}
        </Box>
    );
}

export default Board;