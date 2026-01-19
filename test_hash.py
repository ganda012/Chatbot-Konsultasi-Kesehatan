from werkzeug.security import check_password_hash

# Hash yang sama dengan yang ada di config.py
password_hash_from_config = 'pbkdf2:sha256:600000$8gAbZcB8$8b5f7c1f1a6e0c4d9e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c'

# Password yang akan kita coba
password_to_test = 'admin'

# Lakukan pengecekan
is_correct = check_password_hash(password_hash_from_config, password_to_test)

if is_correct:
    print("✅ Hash BENAR. Password 'admin' cocok dengan hash.")
else:
    print("❌ Hash SALAH. Password 'admin' TIDAK cocok.")