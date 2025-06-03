import React from 'react';
import Container from 'react-bootstrap/Container';
import Alert from 'react-bootstrap/Alert';

function NotFound() {
  return (
    <Container className="py-5">
      <Alert variant="warning" className="text-center">
        <h2>404 - Page Not Found</h2>
        <p>The page you are looking for does not exist.</p>
      </Alert>
    </Container>
  );
}

export default NotFound;
