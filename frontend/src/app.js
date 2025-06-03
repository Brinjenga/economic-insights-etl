import React, { useEffect, useState } from 'react';
import axios from 'axios';
import CountryList from './components/CountryList';
import DashboardHeader from './components/DashboardHeader';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Spinner from 'react-bootstrap/Spinner';
import Alert from 'react-bootstrap/Alert';
import Pagination from 'react-bootstrap/Pagination';
import Container from 'react-bootstrap/Container';

function App() {
  const [countries, setCountries] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [page, setPage] = useState(1);
  const [pageSize] = useState(10);
  const [totalPages, setTotalPages] = useState(1);

  useEffect(() => {
    setLoading(true);
    axios.get(`http://localhost:8080/api/countries?page=${page}&pageSize=${pageSize}`)
      .then(res => {
        setCountries(res.data.data);
        setTotalPages(res.data.totalPages);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, [page, pageSize]);

  const handlePageChange = (newPage) => {
    if (newPage >= 1 && newPage <= totalPages) {
      setPage(newPage);
    }
  };

  return (
    <div className="bg-light min-vh-100">
      <DashboardHeader />
      <Container className="py-4">
        {loading && (
          <div className="d-flex justify-content-center align-items-center" style={{ height: '200px' }}>
            <Spinner animation="border" variant="primary" role="status">
              <span className="visually-hidden">Loading...</span>
            </Spinner>
          </div>
        )}
        {error && <Alert variant="danger">Error: {error}</Alert>}
        {!loading && !error && <>
          <Card className="shadow-sm mb-4">
            <Card.Header className="bg-primary text-white">
              <h2 className="h5 mb-0">Country List</h2>
            </Card.Header>
            <Card.Body className="p-0">
              <CountryList countries={countries} />
            </Card.Body>
          </Card>
          <Pagination className="justify-content-center mt-4">
            <Pagination.Prev disabled={page === 1} onClick={() => handlePageChange(page - 1)} />
            {[...Array(totalPages)].map((_, idx) => (
              <Pagination.Item key={idx + 1} active={page === idx + 1} onClick={() => handlePageChange(idx + 1)}>
                {idx + 1}
              </Pagination.Item>
            ))}
            <Pagination.Next disabled={page === totalPages} onClick={() => handlePageChange(page + 1)} />
          </Pagination>
        </>}
      </Container>
    </div>
  );
}

export default App;