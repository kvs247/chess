# Chess Is Hard

This app is live at https://www.chess.kvschneider.com.

## Introduction

The purpose of this project is pretty simple - it's chess with Python! More than that, it is a Flask-React app which allows users to create an account, log in, and play games with other users. It includes the ability to add friends and send/cancel challenges to other players. Additionally, all in progress and completed games are saved, so you can review your games or view other player's games. Currently it includes some actual games between grandmaster chess players and some games between myself and some friends.

## Installation
If you would like to copy the repo and run it locally, here are the steps:

- After cloing the repo onto your machine, run `pipenv install; pipenv shell` at the root directory to setup a virtual environment with all of the Python dependencies installed. 
-  Run `npm install; npm run build` at the `/client` directory to install all of the JavaScript dependencies and build the app.
- Run `gunicorn --chdir server app:app` at the root directory to launch the app. By default it will be hosted on port 8000.