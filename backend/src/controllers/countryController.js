import { getFirstParquetFile, readParquetRows, readAllParquetRows } from '../services/parquetService.js';
import path from 'path';

export async function getCountries(req, res, next) {
  try {
    const parquetDir = path.join(path.resolve(), '../data/bronze/utils/countries.parquet');
    // Pagination params
    const page = parseInt(req.query.page) || 1;
    const pageSize = parseInt(req.query.pageSize) || 100;
    const result = await readAllParquetRows(parquetDir, page, pageSize);
    res.json(result);
  } catch (err) {
    next(err);
  }
}

// You can add more controllers for GDP, population, etc. following this pattern.
