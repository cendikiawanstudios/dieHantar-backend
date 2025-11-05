from flask import Flask, jsonify
import pymysql.cursors
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Fungsi untuk membuat koneksi database
def get_db_connection():
    return pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB'],
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "success",
        "message": "Backend DieHantar berjalan dengan Flask di Termux!"
    })

@app.route('/api/v1/makanan', methods=['GET'])
def get_makanan_list():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # Contoh query. Pastikan tabel menu_makanan sudah ada di database Anda!
            sql = "SELECT id, nama, harga FROM menu_makanan" 
            cursor.execute(sql)
            result = cursor.fetchall()
            return jsonify({"status": "success", "data": result})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Gagal mengambil data: {e}"}), 500
    finally:
        connection.close()


if __name__ == '__main__':
    # Pastikan MariaDB (MySQL) server sudah berjalan!
    app.run(host='0.0.0.0', port=8000, debug=True)
