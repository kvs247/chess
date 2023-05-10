import { useState, useEffect } from 'react';
import Box from '@mui/material/Box';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import Typography from '@mui/material/Typography';

function MoveList({ moves }) {
  const [groupedMoves, setGroupedMoves] = useState([]);

  useEffect(() => {
    if (moves.length > 0) {
      const movesSplit = moves.split(' ').filter(move => move !== '')
      const mainArr = [];
      let tempArr = [];
      for (let i = 0; i < movesSplit.length + 1; i += 1) {
        const text = movesSplit[i];
        tempArr.push(text);
        if (tempArr.length === 3) {
          mainArr.push(tempArr.join(' '));
          tempArr = [];
        };
      };
      setGroupedMoves(mainArr);
    };
  }, [moves]);

  return (
    <Box
    bgcolor='secondary.main'
    sx={{ overflow: 'auto'}}
    >
      <Typography
        variant='h5'
        align='center'
        sx={{
          mt: 1,
          mb: 3
        }}
      >
        Moves
      </Typography>
      <List>
        {groupedMoves.map((text, index) => {
          return (
            <ListItem key={index}>
              <ListItemText primary={text} sx={{ textAlign: 'center', color: '#e1e1e1' }} />
            </ListItem>
          );
        })}
      </List>
    </Box>
  );
}

export default MoveList;