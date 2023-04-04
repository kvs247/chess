import { Route, Switch } from 'react-router-dom';

import Login from './components/Login';
import SignUp from './components/SignUp';
import Home from './components/Home';

function App() {
  return (
    <>
      <Switch>

        <Route path="/home">
          <Home />
        </Route>

        <Route path="/login">
          <Login />
        </Route>

        <Route path="/signup">
          <SignUp />
        </Route>

      </Switch>
    </>
  );
}

export default App;
