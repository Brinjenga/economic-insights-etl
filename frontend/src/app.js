import React, { useEffect, useState } from 'react';
import axios from 'axios';
import CountryList from './components/CountryList';
import DashboardHeader from './components/DashboardHeader';

function App() {
  const [countries, setCountries] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:8080/api/countries')
      .then(res => {
        setCountries(res.data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  return (
    <div>
      <DashboardHeader />
      <main style={{ padding: '2rem' }}>
        {loading && <div>Loading...</div>}
        {error && <div>Error: {error}</div>}
        {!loading && !error && <CountryList countries={countries} />}
      </main>
    </div>
  );
}

export default App;