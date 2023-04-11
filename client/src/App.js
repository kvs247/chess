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

    const initialUserState = {};
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
      event.preventDefault();
      const data = new FormData(event.currentTarget);
      const dataObj = Object.fromEntries(data.entries());
      fetch(route, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(dataObj)
        })
        .then(res => {
          if (res.ok) {
            res.json().then(user => setUser(user));
            history.push('/home');
          } else {
            res.json().then(errors => console.log(errors));
          };
        });
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
                onLogout={handleLogout}
                onClickPlay={handleClickPlay}
                playComputer={playComputer}
              />
            </Route>

            <Route path='/play/:id'>
              <Play 
                user={user}
                users={users}
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
              <Login onSubmit={handleLoginSignUp} />
            </Route>

            <Route path="/signup">
              <SignUp onSubmit={handleLoginSignUp} />
            </Route>

            <Redirect from='/' to='/login' />

          </Switch>
        </>
    );
}

export default App;
