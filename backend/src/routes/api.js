import express from 'express';
import cors from 'cors';
import fs from 'fs';
import path from 'path';
import parquet from 'parquetjs-lite';
import { getCountries } from '../controllers/countryController.js';

const router = express.Router();
router.use(cors());

// Utility to read Parquet files
async function readParquetRows(parquetPath) {
  const reader = await parquet.ParquetReader.openFile(parquetPath);
  const cursor = reader.getCursor();
  let record = null;
  const rows = [];
  while (record = await cursor.next()) {
    rows.push(record);
  }
  await reader.close();
  return rows;
}

// Health check endpoint
router.get('/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// API: Countries
router.get('/countries', getCountries);

// 404 handler for unknown API routes
router.use((req, res) => {
  res.status(404).json({ error: 'API endpoint not found' });
});

// TODO: Add endpoints for GDP, population, CO2, electricity, etc.

export default router;
