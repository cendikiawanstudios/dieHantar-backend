# ALGORITMA TARIF / PRICING
# File ini menghitung harga berdasarkan jarak

HARGA_PER_KM_MOTOR = 2500
HARGA_PER_KM_MOBIL = 6000
BIAYA_JASA_APLIKASI = 2000

def hitung_tarif(jarak_km, jenis_kendaraan):
    if jenis_kendaraan == 'MOTOR':
        total = (jarak_km * HARGA_PER_KM_MOTOR) + BIAYA_JASA_APLIKASI
    elif jenis_kendaraan == 'MOBIL':
        total = (jarak_km * HARGA_PER_KM_MOBIL) + BIAYA_JASA_APLIKASI
    else:
        return 0
    
    return int(total)

# Test sederhana
if __name__ == "__main__":
    print(f"Harga 5KM Motor: Rp {hitung_tarif(5, 'MOTOR')}")