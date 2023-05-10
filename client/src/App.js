import { useState, useEffect, createContext } from 'react';
import { Route, Switch, Redirect, useHistory } from 'react-router-dom';

import Login from './components/Auth/Login.js';
import SignUp from './components/Auth/SignUp.js';
import Play from './components/Play/Play.js';
import Social from './components/Social/Social.js';
import About from './components/About/About.js';

import { pgnToObj } from './components/Util/pgnFenHandler.js';

export const AppContext = createContext();

function App() {

  const history = useHistory();
  
  const initialUserState = {
      id: null,
      full_name: '',
      username: '',
      email: '',
      profile_image: '',
      date_joined: '',
      friend_ids: [],
      board_color: '#046920'
  };
  const [user, setUser] = useState(initialUserState);
  const [users, setUsers] = useState([]);
  const [games, setGames] = useState([]);
  const [movesToMake, setMovesToMake] = useState(0);
  const [numChallenges, setNumChallenges] = useState(0);
  const [challenges, setChallenges] = useState(false);
  const [selectedColor, setSelectedColor] = useState(() => {
      const storedColor = localStorage.getItem('boardColor');
      return storedColor ? storedColor : '#046920';
  });

  const handleColorChange = (color) => {
    setSelectedColor(color.hex);
  };            
  
  const handleColorChangeComplete = (color) => {
    fetch(`/users/${user.id}`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ boardColor: color.hex })
    })
  };
  
  const getUsers = () => {
      fetch('/users')
        .then(res => res.json())
        .then(data => setUsers(data));
  };

  const getGames = () => {
      fetch('/games')
        .then(res => res.json())
        .then(data => setGames(data));
  };

  const authorize = () => {
      fetch('/authorized-session')
      .then(res => {
        if (res.ok) {
          res.json().then(user => setUser(user));
        };
      });
  };

  const resetHomeBoard = (id) => {
      fetch('/games', {
          method: 'PATCH',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({ id, })
    })      
  };

  const handleLoginSignUp = (event, route) => {
      // route is either '/login' or '/signup'
      const dataObj = event
      return fetch(route, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(dataObj)
      })
        .then(res => {
            if (res.ok) {
                resetHomeBoard(0);
                console.log('yo', user.board_color)
                localStorage.setItem('boardColor', user.board_color);
                setSelectedColor(user.board_color);
                history.push('/play');
                if (route === '/signup') getUsers();
                return res.json().then(user => setUser(user));
            } else {
                return res.json().then(errors => Promise.reject(errors));
            };
        })
  };

  const handleLogout = () => {
      fetch('/logout', { method: 'DELETE' })
      .then(res => {
          if (res.ok) setUser(initialUserState);
      });
      resetHomeBoard(0);
  };

  const handleSwitchMode = (challenges) => {
      setChallenges(challenges);
  };

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
        <AppContext.Provider
          value={{
            user,
            users,
            games,
            movesToMake,
            challenges,
            numChallenges,
            selectedColor,
            getGames,
            resetHomeBoard,
            handleLogout,
            handleSwitchMode,
            handleColorChange,
            handleLoginSignUp,
            handleColorChangeComplete
          }}
        >
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
        </AppContext.Provider>

      </>
  );
}

export default App;
