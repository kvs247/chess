import BaseContainer from '../BaseContainer';
import NavBar from '../NavBar';
import ActiveGames from '../ActiveGames';

function Play({ playComputer }) {
    return (
        <h1>{playComputer ? 'play computer' : 'play friend'}</h1>

    );
}

export default Play;