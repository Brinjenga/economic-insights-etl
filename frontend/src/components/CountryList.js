import React from 'react';

function CountryList({ countries }) {
  return (
    <ul>
      {countries.map((c, i) => (
        <li key={i}>{c.name} ({c.id})</li>
      ))}
    </ul>
  );
}

export default CountryList;
