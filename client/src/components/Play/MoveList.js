import { useState, useEffect } from 'react';
import Box from '@mui/material/Box';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';

function MoveList({ moves }) {

    const [groupedMoves, setGroupedMoves] = useState([]);

    useEffect(() => {
        console.log(moves)
        // const groupedMoves = [];
        if (moves.length > 0) {
              // console.log('moves', moves)
              const movesSplit = moves.split(' ').filter(move => move !== '')
              // console.log('moveSplit', movesSplit)
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
        // console.log('groupedMoves', groupedMoves)

    }, [moves]);


    return (
        <Box
        bgcolor='secondary.main'
        sx={{ overflow: 'auto'}}
        >
          <List>
            {groupedMoves.map((text, index) => {
              return (
                <ListItem key={index}>
                  <ListItemText primary={text} />
                </ListItem>
              );
            })}
          </List>
        </Box>
    );
}

export default MoveList;