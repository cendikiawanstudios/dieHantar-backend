from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

# Konfigurasi Database (User ROOT)
db_config = {
    'user': 'root', 
    'password': '',
    'host': '127.0.0.1',
    'database': 'diehantar',
    'autocommit': True
}

def get_db():
    return mysql.connector.connect(**db_config)

@app.route('/')
def home():
    return jsonify({"status": "Online", "fitur": "Wallet & Voucher"})

# --- FITUR DOMPET / SALDO (Poin 5) ---
@app.route('/api/wallet', methods=['POST'])
def wallet():
    data = request.json
    user = data.get('user', 'User_App')
    action = data.get('action') # 'info' atau 'topup'
    
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    
    if action == 'info':
        # Cek Saldo
        cursor.execute("SELECT * FROM users WHERE username = %s", (user,))
        result = cursor.fetchone()
        if not result:
            # Auto register user jika belum ada
            cursor.execute("INSERT INTO users (username, saldo) VALUES (%s, 0)", (user,))
            saldo = 0
        else:
            saldo = result['saldo']
        conn.close()
        return jsonify({"user": user, "saldo": saldo})

    elif action == 'topup':
        # Isi Saldo
        jumlah = int(data.get('jumlah', 0))
        cursor.execute("UPDATE users SET saldo = saldo + %s WHERE username = %s", (jumlah, user))
        cursor.execute("INSERT INTO transaksi (user, tipe, jumlah, keterangan) VALUES (%s, 'TOPUP', %s, 'Topup via Termux')",(user, jumlah))
        conn.close()
        return jsonify({"status": "Sukses", "pesan": f"Berhasil Topup Rp {jumlah}"})

# --- FITUR VOUCHER / DISKON (Poin 8) ---
@app.route('/api/check-promo', methods=['POST'])
def check_promo():
    code = request.json.get('kode', '').upper()
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vouchers WHERE kode = %s", (code,))
    voucher = cursor.fetchone()
    conn.close()
    
    if voucher:
        if voucher['kuota'] > 0:
            return jsonify({"valid": True, "potongan": voucher['potongan'], "pesan": "Kode Valid!"})
        else:
            return jsonify({"valid": False, "potongan": 0, "pesan": "Kuota Habis"})
    return jsonify({"valid": False, "potongan": 0, "pesan": "Kode Tidak Ditemukan"})

# --- FITUR INTI (Order & Driver) ---
@app.route('/api/order', methods=['POST'])
def order():
    data = request.json
    user = data.get('user', 'Anonim')
    jenis = data.get('jenis', 'Umum')
    lokasi = data.get('lokasi', '-')
    potongan = data.get('potongan', 0) # Diskon dari frontend
    
    harga_dasar = 15000 if jenis == 'dieFood' else 12000
    total_bayar = max(0, harga_dasar - potongan)
    
    try:
        conn = get_db()
        cursor = conn.cursor()
        sql = "INSERT INTO pesanan (user, jenis, lokasi, status, harga) VALUES (%s, %s, %s, %s, %s)"
        val = (user, jenis, lokasi, "Mencari Driver", total_bayar)
        cursor.execute(sql, val)
        conn.close()
        return jsonify({"status": "Sukses", "info": "Menunggu Driver...", "harga_akhir": total_bayar})
    except Exception as e:
        return jsonify({"status": "Error", "info": str(e)})

@app.route('/api/list-orders', methods=['GET'])
def get_orders():
    try:
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pesanan ORDER BY id DESC LIMIT 20")
        rows = cursor.fetchall()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify([])

@app.route('/api/take-order', methods=['POST'])
def take_order():
    data = request.json
    order_id = data.get('id')
    driver = data.get('driver', 'Driver')
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE pesanan SET status = %s WHERE id = %s", (f"Diambil {driver}", order_id))
    conn.close()
    return jsonify({"status": "Sukses"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
