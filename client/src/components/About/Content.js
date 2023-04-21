import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';

const textBlock = (name, description) => {
    return (
        <Box
          textAlign='center'
          display='flex'
          flexDirection='column'
          alignItems='center'
          justifyContent='center'        
        >
            <Typography variant='h2'>{name}</Typography>
            <Typography color='#e1e1e1'>{description}</Typography>
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
                'This is a cool app made by me'
            )}

            {textBlock('Dependencies',
                'None for chess baby'
            )}

            {textBlock('Chess Rules',
                'This is a cool app made by me'
            )}     

            {textBlock('Source and Demo',
                'This is a cool app made by me'
            )}                   

        </Box>
    );
}

export default Content;