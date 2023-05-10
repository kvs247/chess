import { useState, createContext, useContext } from "react";
import { useHistory } from "react-router-dom";

const AppContext = createContext();

export function useAppContext() {
  return useContext(AppContext);
}

const AppContextProvider = ({ children }) => {

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

  return (
    <AppContext.Provider
      value={{
        user,
        users,
        games,
        movesToMake,
        setMovesToMake,
        numChallenges,
        challenges,
        selectedColor,
        setSelectedColor,
        handleColorChange,
        handleColorChangeComplete,
        getUsers,
        getGames,
        authorize,
        resetHomeBoard,
        handleLoginSignUp,
        handleLogout,
        handleSwitchMode
      }}
    >
      {children}
    </AppContext.Provider>
  );
};

export default AppContextProvider;