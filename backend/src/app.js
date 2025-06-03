import express from 'express';
import cors from 'cors';
import fs from 'fs';
import path from 'path';
import parquet from 'parquetjs-lite';
import apiRoutes from './routes/api.js';

const app = express();
app.use(cors());
app.use('/api', apiRoutes);

// Example: Serve country list from bronze layer
app.get('/api/countries', async (req, res) => {
  try {
    const parquetPath = path.join(path.resolve(), 'data/bronze/utils/countries.parquet/part-00000-49f8c137-7db6-48f1-a403-a97441aab066-c000.snappy.parquet');
    const reader = await parquet.ParquetReader.openFile(parquetPath);
    const cursor = reader.getCursor();
    let record = null;
    const countries = [];
    while (record = await cursor.next()) {
      countries.push(record);
    }
    await reader.close();
    res.json(countries);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// TODO: Add endpoints for GDP, population, CO2, electricity, etc.

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Backend API running on port ${PORT}`);
});