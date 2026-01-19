import os
from dotenv import load_dotenv

# Memuat variabel lingkungan dari file .env (jika ada)
load_dotenv()

class Config:
    # Secret key untuk keamanan session, CSRF token, dll.
    # Generate key baru dengan: python -c 'import secrets; print(secrets.token_hex())'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ini-adalah-secret-key-yang-sangat-rahasia'
    
    # Konfigurasi database SQLite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///chatbot.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --- KONFIGURASI LOGIN ADMIN ---
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME') or 'admin'
    # Hash ini dibuat untuk password: 'admin'
    ADMIN_PASSWORD_HASH = os.environ.get('ADMIN_PASSWORD_HASH') or 'scrypt:32768:8:1$4SnjStNtniADDcRM$faada47232f3fe9a0cfa39a5ebf217b693ded9313ea5511c6edb7b3ecedda284d3cd919f2893e52d02bb06072d206f7c2422a8473ccdd1d25042927d7a76dd41'