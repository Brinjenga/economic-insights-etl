import React from 'react';
import Navbar from 'react-bootstrap/Navbar';
import Container from 'react-bootstrap/Container';

function DashboardHeader() {
  return (
    <Navbar bg="primary" variant="dark" expand="lg" className="mb-4">
      <Container>
        <Navbar.Brand href="#home">
          Economic Insights Dashboard
        </Navbar.Brand>
      </Container>
    </Navbar>
  );
}

export default DashboardHeader;
