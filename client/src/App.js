import { useState, useEffect } from 'react';
import { Route, Switch, Redirect, useHistory } from 'react-router-dom';

import Login from './components/Auth/Login.js';
import SignUp from './components/Auth/SignUp.js';
import Home from './components/Home/Home.js';
import Play from './components/Play/Play.js';
import Social from './components/Social/Social.js';
import About from './components/About/About.js';

import { pgnToObj } from './components/Util/pgnFenHandler.js';

function App() {

    const history = useHistory();

    const initialUserState = {
        id: null,
        full_name: '',
        username: '',
        email: '',
        profile_image: '',
        date_joined: '',
        friend_ids: []
    };
    const [user, setUser] = useState(initialUserState);
    const [users, setUsers] = useState([]);
    const [games, setGames] = useState([]);
    const [movesToMake, setMovesToMake] = useState(0);
    const [numChallenges, setNumChallenges] = useState(0);
    const [challenges, setChallenges] = useState(true);

    const authorize = () => {
        fetch('/authorized-session')
        .then(res => {
          if (res.ok) {
            res.json().then(user => setUser(user));
          };
        });
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
    }, [user])

    // route is either '/login' or '/signup'
    const handleLoginSignUp = (event, route) => {
        const dataObj = event
        console.log(dataObj)
        return fetch(route, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(dataObj)
        })
          .then(res => {
              if (res.ok) {
                  history.push('/home');
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
    };

    const handleSwitchMode = (challenges) => {
        setChallenges(challenges);
    };

    return (
        <>
          <Switch>

            <Route path="/home">
              <Home 
                user={user} 
                users={users}
                movesToMake={movesToMake}
                numChallenges={numChallenges}
                onLogout={handleLogout}
                onClickPlay={handleSwitchMode}
              />
            </Route>

            <Route exact path='/play'>
              <Play 
                user={user}
                users={users}
                movesToMake={movesToMake}
                numChallenges={numChallenges}
                games={games}
                setGames={setGames}
                getGames={getGames}                
                onLogout={handleLogout}
                onClickPlay={handleSwitchMode}
                showChallenges={challenges}
              />
            </Route>

            <Route path='/play/:id'>
              <Play 
                user={user}
                users={users}
                movesToMake={movesToMake}
                numChallenges={numChallenges}
                games={games}
                setGames={setGames}
                getGames={getGames}
                onLogout={handleLogout}
                onClickPlay={handleSwitchMode}
                showChallenges={challenges}
              />
            </Route>

            <Route path='/users/:id'>
              <Social 
                user={user}
                users={users}
                games={games}
                movesToMake={movesToMake}
                numChallenges={numChallenges}
                onLogout={handleLogout}
                onClickPlay={handleSwitchMode}
              />
            </Route>

            <Route path='/about'>
              <About 
                user={user} 
                movesToMake={movesToMake}
                numChallenges={numChallenges}
                onLogout={handleLogout}
                onClickPlay={handleSwitchMode}
              />
            </Route>            

            <Route path="/login">
              <Login handleLogin={handleLoginSignUp} />
            </Route>

            <Route path="/signup">
              <SignUp handleSignUp={handleLoginSignUp} />
            </Route>

            <Redirect from='/' to='/login' />

          </Switch>
        </>
    );
}

export default App;
