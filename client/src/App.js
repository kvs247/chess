import { Route, Switch } from 'react-router-dom';

import Login from './components/Login';

function App() {
  return (
    <>
      <Switch>

        <Route exact path="/home">
          <h1>Chess Is Hard</h1>
        </Route>

        <Route exact path="/login">
          <Login />
        </Route>

      </Switch>
    </>
  );
}

export default App;
