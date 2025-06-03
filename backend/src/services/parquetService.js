import parquet from 'parquetjs-lite';
import fs from 'fs';
import path from 'path';

export async function readParquetRows(parquetPath) {
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

export function getFirstParquetFile(dir) {
  const files = fs.readdirSync(dir).filter(f => f.endsWith('.parquet'));
  if (files.length === 0) throw new Error('No parquet files found in directory: ' + dir);
  return path.join(dir, files[0]);
}

export async function readAllParquetRows(dir, page = 1, pageSize = 100) {
  // Get all .parquet files in the directory
  const files = fs.readdirSync(dir).filter(f => f.endsWith('.parquet'));
  if (files.length === 0) throw new Error('No parquet files found in directory: ' + dir);
  let allRows = [];
  for (const file of files) {
    const parquetPath = path.join(dir, file);
    const rows = await readParquetRows(parquetPath);
    allRows = allRows.concat(rows);
  }
  // Pagination
  const total = allRows.length;
  const start = (page - 1) * pageSize;
  const end = start + pageSize;
  const paginatedRows = allRows.slice(start, end);
  return {
    data: paginatedRows,
    page,
    pageSize,
    total,
    totalPages: Math.ceil(total / pageSize)
  };
}
