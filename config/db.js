const mysql = require('mysql2');

const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',      // Default user Termux
  password: '',      // Kosongkan jika tidak ada password
  database: 'diehantar_db'
});

db.connect((err) => {
  if (err) {
    console.error('❌ Gagal koneksi ke Database:', err);
  } else {
    console.log('✅ Terhubung ke Database MySQL dieHantar!');
  }
});

module.exports = db;
