import { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import BaseContainer from '../BaseContainer';
import NavBar from '../NavBar';
import Challenges from './Challenges.js';
import GameArea from '../GameArea';

function Home({ user, users, movesToMake, numChallenges, onLogout, onClickPlay }) {

    const history = useHistory();

    const [receivedChallenges, setReceivedChallenges] = useState([]);
    const [sentChallenges, setSentChallenges] = useState([]);

    useEffect(() => {
        fetch('/challenges') 
          .then(res => res.json())
          .then(data => {
              const receivedUserChallenges = data.filter(challenge => challenge.challengee_id === user.id);
              setReceivedChallenges(receivedUserChallenges)

              const sentUserChallenges = data.filter(challenge => challenge.challenger_id === user.id);
              setSentChallenges(sentUserChallenges)
          }) 
    }, [user])

    const handleClickAccept = (id, username) => {
        fetch('/games', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify([
              { id: user.id, username: user.username}, 
              { id, username }
            ])
        })
          .then(res => res.json())
          .then(data => {
              history.push(`/play/${data.id}`)
          });
    };

    const handleClickDecline = (challengeId) => {
        fetch(`/challenges/${challengeId}`, {
            method: 'DELETE'
        })
        const newReceivedChallenges = receivedChallenges.filter(
            challenge => challenge.id !== challengeId
        )
        setReceivedChallenges(newReceivedChallenges)
    };

    const handleClickDelete = (challengeId) => {
      fetch(`/challenges/${challengeId}`, {
          method: 'DELETE'
      })
      const newSentChallenges = sentChallenges.filter(
          challenge => challenge.id !== challengeId
      )
      setSentChallenges(newSentChallenges)
    };


    const receivedChallengeUsers = receivedChallenges.map(c => {
        return {
            challenge: c,
            user: users.find(u => u.id === c.challenger_id)
        }
    });
    const sentChallengeUsers = sentChallenges.map(c => {
        return {
            challenge: c,
            user: users.find(u => u.id === c.challengee_id)
        }
    });

    return (
        <BaseContainer>
          <NavBar 
            user={user}
            movesToMake={movesToMake}
            numChallenges={numChallenges}
            onLogout={onLogout} 
            onClickPlay={onClickPlay}
          />
          <GameArea 
            user={user}   
            users={users}
            staticBoard={true} 
          />
          <Challenges 
            receivedChallengeUsers={receivedChallengeUsers}
            sentChallengeUsers={sentChallengeUsers}
            onClickAccept={handleClickAccept}
            onClickDecline={handleClickDecline}
            onClickDelete={handleClickDelete}
          />
        </BaseContainer>
    );
}

export default Home;