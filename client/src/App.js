import { useState, useEffect, createContext, useContext } from 'react';
import { Route, Switch, Redirect, useHistory } from 'react-router-dom';

import Login from './components/Auth/Login.js';
import SignUp from './components/Auth/SignUp.js';
import Play from './components/Play/Play.js';
import Social from './components/Social/Social.js';
import About from './components/About/About.js';

import { pgnToObj } from './components/Util/pgnFenHandler.js';

import AppContextProvider, { useAppContext } from './AppContext.js';

function App() {

  const history = useHistory();

  const {
    selectedColor,
    authorize,
    getUsers,
    getGames,
    games,
    user,
    users,
    setMovesToMake,
    setNumChallenges,
    setSelectedColor
  } = useAppContext();

  useEffect(() => {
      localStorage.setItem('boardColor', selectedColor);
    }, [selectedColor]);
    
  useEffect(() => {
    authorize();
    getUsers();
    getGames();
  }, []);
  
  useEffect(() => {
      const activeGames = games.filter(game => {
          const pgnObj = pgnToObj(game.pgn);
          const inProgress = pgnObj['result'] === '*'
          const isWhite = pgnObj['whiteUsername'] === user.username;
          const isBlack = pgnObj['blackUsername'] === user.username;
          return inProgress && (isWhite || isBlack);
      });         
      const yourMoveGames = activeGames.filter(game => {
          const whitesTurn = game.fen.split(' ')[1] === 'w' ? true : false;
          let result = false
          if (whitesTurn && user.id === game.white_user_id) result = true;
          if (!whitesTurn && user.id === game.black_user_id) result = true;
          return result
      });
      setMovesToMake(yourMoveGames.length);
  // eslint-disable-next-line
  }, [games]);

  useEffect(() => {
    fetch('/challenges') 
      .then(res => res.json())
      .then(data => {
          const receivedChallenges = data.filter(challenge => challenge.challengee_id === user.id);
          const receivedChallengeUsers = receivedChallenges.map(c => {
            return {
                challenge: c,
                user: users.find(u => u.id === c.challenger_id)
            }
          });
          setNumChallenges(receivedChallengeUsers.length);
      }) 
    localStorage.setItem('boardColor', user.board_color);
    setSelectedColor(user.board_color);
  // eslint-disable-next-line
  }, [user])


  return (
      <>
        {/* <AppContextProvider> */}
          <Switch>
            <Route exact path='/play'>
              <Play />
            </Route>
            <Route path='/play/:id'>
              <Play />
            </Route>
            <Route path='/profile/:id'>
              <Social />
            </Route>
            <Route path='/about'>
              <About />
            </Route>            
            <Route path="/login">
              <Login />
            </Route>
            <Route path="/signup">
              <SignUp />
            </Route>
            <Redirect from='/' to='/login' />
          </Switch>
        {/* </AppContextProvider> */}

      </>
  );
}

export default App;
