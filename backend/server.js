
const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');

const app = express();
const PORT = 3000;

// Connect to the existing Capstone B database
const databasePath = path.join(
    __dirname,
    '..',
    'database',
    'capstone_b.db'
);

const db = new sqlite3.Database(databasePath, (error) => {
    if (error) {
        console.error('Database connection failed:', error.message);
    } else {
        console.log('Connected to Capstone B SQLite database');
    }
});

// Home endpoint
app.get('/', (req, res) => {
    res.send('Server Running');
});

// Health check endpoint
app.get('/api/health', (req, res) => {
    res.json({ status: 'healthy' });
});

// Get all products from the database
app.get('/api/products', (req, res) => {
    db.all('SELECT * FROM Product', [], (error, rows) => {
        if (error) {
            return res.status(500).json({
                error: 'Failed to retrieve products',
                details: error.message
            });
        }

        res.json({
            count: rows.length,
            products: rows
        });
    });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server Started at http://localhost:${PORT}`);
});
