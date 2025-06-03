import React from 'react';
import ListGroup from 'react-bootstrap/ListGroup';

function CountryList({ countries }) {
  return (
    <ListGroup variant="flush">
      {countries.map((c, i) => (
        <ListGroup.Item key={i}>
          {c.name} ({c.id})
        </ListGroup.Item>
      ))}
    </ListGroup>
  );
}

export default CountryList;
