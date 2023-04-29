# Chess Is Hard

![alt](https://github.com/kschneider0/chess/blob/main/server/assets/screenshot1.png?raw=true)

This app is live at https://www.chess.kvschneider.com.

## Introduction

The purpose of this project is pretty simple - it's chess with Python! More than that, it is a Flask-React app which allows users to create an account, log in, and play games with other users. It includes the ability to add friends and send/cancel challenges to other players. Additionally, all in progress and completed games are saved, so you can review your games or view other player's games. Currently it includes some actual games between grandmaster chess players and some games between myself and some friends.

## Installation
If you would like to copy the repo and run it locally, here are the steps:

- After cloing the repo onto your machine, run `pipenv install; pipenv shell` at the root directory to setup a virtual environment with all of the Python dependencies installed. 
-  Run `npm install; npm run build` at the `/client` directory to install all of the JavaScript dependencies and build the app.
- Run `gunicorn --chdir server app:app` at the root directory to launch the app. By default it will be hosted on port 8000.

## Usage 

To start a new game, go to the Social page, where you can find a list of all the accounts on the app. Click on another account to view their stats and a scrollable list of their completed games. Select a game to view it on the chess board. You can add or remove other users from your friends list, and send them a challenge with the "SEND CHALLENGE" button. Challenges sent to you by other players will also appear on the Challenge screen.
            
Once a challenge is accepted, a new game will be automatically created and accessible on the Active Games page. For testing purposes, both players can move both sets of pieces. However, normal chess rules apply, such as castling, en passant capture, pawn promotion, and most win/draw scenarios. The game of chess is complex with many rules, so the logic is not 100% complete, but it will allow legal moves and disallow illegal ones for the majority of board positions. Pawn promotion is implemented (only to queen status), but may cause issues.

## Structure
### Front End
- App
  - About
    - NavBar
    - Content
    - Attribution
  - Social
    - NavBar
    - Profile
      - CompletedGames
    - UserList/FriendList
  - Play
    - NavBar
    - GameArea
      - Board
    - MoveList/Challenges/ActiveGames
    


## Dependencies

## Features

## 