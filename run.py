# run.py
from app import create_app, db # Impor create_app, bukan app langsung

# Buat instance aplikasi
app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # Ini akan membuat tabel database jika belum ada
        db.create_all()
        print("Database tables created successfully.") # Tambahkan pesan konfirmasi (opsional)
    
    app.run(debug=True)
