import { useState } from 'react';
import { Route, Switch } from 'react-router-dom';

import Login from './components/Login';
import SignUp from './components/SignUp';
import Home from './components/Home';

function App() {

    const [user, setUser] = useState({});

    return (
        <>
          <Switch>

            <Route path="/home">
              <Home />
            </Route>

            <Route path="/login">
              <Login setUser={setUser}/>
            </Route>

            <Route path="/signup">
              <SignUp />
            </Route>

          </Switch>
        </>
    );
}

export default App;
