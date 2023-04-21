import Container from '@mui/material/Container';
import CssBaseline from '@mui/material/CssBaseline';

function BaseContainer({ children, columns='16rem 1fr 20rem' }) {
    return (
        <Container 
          disableGutters
          sx={{ 
            bgcolor: 'primary.main', 
            height: '100vh', 
            width: '100vw',
            minWidth: '100%',
            display: 'grid',
            gridTemplateColumns: columns,
            padding: 0
          }}
        >
          <CssBaseline />
          {children}
      </Container>
    );
}

export default BaseContainer;