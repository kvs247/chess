import { useState, useEffect } from 'react';
import { Route, Switch, Redirect, useHistory } from 'react-router-dom';

import Login from './components/Auth/Login.js';
import SignUp from './components/Auth/SignUp.js';
import Home from './components/Home/Home.js';
import Play from './components/Play/Play.js';
import Social from './components/Social/Social.js';
import About from './components/About/About.js';

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
    const [playComputer, setPlayComputer] = useState(true);

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

    const handleClickPlay = (playComputer) => {
        setPlayComputer(playComputer);
    };

    return (
        <>
          <Switch>

            <Route path="/home">
              <Home 
                user={user} 
                users={users}
                onLogout={handleLogout}
                onClickPlay={handleClickPlay}
              />
            </Route>

            <Route exact path='/play'>
              <Play 
                user={user}
                users={users}
                games={games}
                setGames={setGames}
                getGames={getGames}                
                onLogout={handleLogout}
                onClickPlay={handleClickPlay}
                playComputer={playComputer}
              />
            </Route>

            <Route path='/play/:id'>
              <Play 
                user={user}
                users={users}
                games={games}
                setGames={setGames}
                getGames={getGames}
                onLogout={handleLogout}
                onClickPlay={handleClickPlay}
                playComputer={playComputer}
              />
            </Route>

            <Route path='/users/:id'>
              <Social 
                user={user}
                users={users}
                games={games}
                onLogout={handleLogout}
                onClickPlay={handleClickPlay}
              />
            </Route>

            <Route path='/about'>
              <About 
                user={user} 
                onLogout={handleLogout}
                onClickPlay={handleClickPlay}
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
