# LAYANAN NOTIFIKASI
# Menggunakan Firebase Cloud Messaging (FCM) placeholder

def send_push_notification(user_token, title, message):
    print(f"[FCM SEND] To: {user_token} | {title}: {message}")
    # Disini nanti pasang library 'firebase-admin'
    return True

def notify_driver_new_order(driver_id, order_details):
    msg = f"Order Baru Masuk! Jarak: {order_details['jarak']}km"
    send_push_notification(driver_id, "Order Masuk", msg)