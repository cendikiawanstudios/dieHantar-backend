const express = require('express');
const app = express();
const port = 3000;

// Middleware agar bisa baca JSON
app.use(express.json());

// --- TAMBAHKAN BAGIAN INI ---
const restaurantRoutes = require('./routes/restaurantRoutes');
app.use('/api/restaurants', restaurantRoutes);
// ----------------------------

app.listen(port, () => {
  console.log(`🚀 Server Backend dieHantar berjalan di port ${port}`);
});
