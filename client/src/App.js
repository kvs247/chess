import { useState, useEffect } from 'react';
import { Route, Switch, Redirect, useHistory } from 'react-router-dom';

import Login from './components/Login';
import SignUp from './components/SignUp';
import Home from './components/Home';

function App() {

    const history = useHistory();

    const initialUserState = {
        
    };
    const [user, setUser] = useState({});

    
    useEffect(() => {
      fetch('/authorized-session')
      .then(res => {
        if (res.ok) {
          res.json().then(user => setUser(user));
        };
      });
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
            if (res.ok) setUser({});
        });
    };

    return (
        <>
          <Switch>

            <Route path="/home">
              <Home 
                user={user} 
                onLogout={handleLogout}
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
