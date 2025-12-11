const express = require('express');
const router = express.Router();
const db = require('../config/db');

// 1. GET: Ambil Semua Data Restoran (Untuk Tampilan User)
router.get('/', (req, res) => {
    const sql = 'SELECT * FROM restaurants WHERE is_open = 1';
    db.query(sql, (err, results) => {
        if (err) {
            return res.status(500).json({ error: err.message });
        }
        res.json({
            message: 'Data restoran berhasil diambil',
            data: results
        });
    });
});

// 2. POST: Tambah Restoran Baru (Untuk Mitra Daftar)
router.post('/', (req, res) => {
    const { owner_id, name, description, address, image_url } = req.body;
    
    // Validasi sederhana
    if (!name || !address) {
        return res.status(400).json({ message: 'Nama dan Alamat wajib diisi!' });
    }

    const sql = `INSERT INTO restaurants (owner_id, name, description, address, image_url) VALUES (?, ?, ?, ?, ?)`;
    
    db.query(sql, [owner_id, name, description, address, image_url], (err, result) => {
        if (err) {
            return res.status(500).json({ error: err.message });
        }
        res.status(201).json({
            message: 'Restoran berhasil didaftarkan!',
            restaurantId: result.insertId
        });
    });
});

module.exports = router;
