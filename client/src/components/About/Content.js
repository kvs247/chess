import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';

const textBlock = (name, descriptions) => {
    return (
        <Box
          textAlign='center'
          display='flex'
          flexDirection='column'
          alignItems='center'
          justifyContent='center'        
        >
            <Typography variant='h2'>{name}</Typography>
            {descriptions.map(description => {
                return <><Typography 
                         color='#e1e1e1' 
                         textAlign='left'
                         sx={{ mx: 12 }}
                       >{description}</Typography>
                       <br /></>
            })}
        </Box>
    );
};

function Content() {
    return (
        <Box
          sx={{
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              justifyContent: 'center',
              height: 'calc(100vh - 64px)',
              padding: '0 16px',
          }}        
        >
            <Typography variant='h1'>About</Typography>

            {textBlock('Description',
                ['Welcome to Chess Is Hard, a web application made by me, Kyle Schneider. This was my final project for a coding bootcamp I completed in April 2023, and I have continued making improvements and perfecting features since graduating. I chose this project because I thought it would be challenging, easy to appreciate, and because like many, I find chess extremely interesting.',
                
                'To start a new game, go to the Social page, where you can find a list of all the accounts on the app. Click on another account to view their stats and a scrollable list of their completed games. Select a game to view it on the chess board. You can add or remove other users from your friends list, and send them a challenge with the "SEND CHALLENGE" button. Challenges sent to you by other players will also appear on the Challenge screen.',
            
                'Once a challenge is accepted, a new game will be automatically created and accessible on the Active Games page. For testing purposes, both players can move both sets of pieces. However, normal chess rules apply, such as castling, en passant capture, pawn promotion, and most win/draw scenarios. The game of chess is complex with many rules, so the logic is not 100% complete, but it will allow legal moves and disallow illegal ones for the majority of board positions. Pawn promotion is implemented (only to queen status), but may cause issues.']
            )}

            {textBlock('Dependencies',
                ['This app does not use any chess related dependencies.',
            
                'React Router, Material UI, React Draggable, React Color, Formik/Yup, ', ]
            )}

            {textBlock('Chess Rules',
                [<Link target='_blank' href='https://www.chess.com/learn-how-to-play-chess' color='#e1e1e1'>Learn to play chess on Chess.com</Link>]
            )}     

            {textBlock('Source and Demo',
                [<Link target='_blank' href='https://github.com/kschneider0/chess' color='#e1e1e1'>Source Code</Link>]
            )}                   

        </Box>
    );
}

export default Content;