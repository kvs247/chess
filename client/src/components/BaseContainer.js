import Container from '@mui/material/Container';
import CssBaseline from '@mui/material/CssBaseline';

function BaseContainer({ children }) {
    return (
        <Container 
          disableGutters
          sx={{ 
            bgcolor: 'primary.main', 
            height: '100vh', 
            width: '100vw',
            minWidth: '100%',
            display: 'grid',
            gridTemplateColumns: '15% 70% 15%',
            padding: 0
          }}
        >
          <CssBaseline />
          {children}
      </Container>
    );
}

export default BaseContainer;