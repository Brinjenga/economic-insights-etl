import express from 'express';
import cors from 'cors';
import fs from 'fs';
import path from 'path';
import parquet from 'parquetjs-lite';

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

// API: Countries
router.get('/countries', async (req, res) => {
  try {
    const parquetPath = path.join(path.resolve(), 'data/bronze/utils/countries.parquet/part-00000-49f8c137-7db6-48f1-a403-a97441aab066-c000.snappy.parquet');
    const countries = await readParquetRows(parquetPath);
    res.json(countries);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// TODO: Add endpoints for GDP, population, CO2, electricity, etc.

export default router;
