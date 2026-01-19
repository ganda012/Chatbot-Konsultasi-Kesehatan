# import_data.py
import json
from app import create_app, db
from app.models_db import QnA

def import_qna_from_json():
    """
    Mengimpor data Q&A dari file data.json ke dalam database.
    Jika pertanyaan sudah ada, jawabannya akan diperbarui.
    """
    app = create_app()
    
    # Path ke file data.json Anda
    json_file_path = 'data.json'

    with app.app_context():
        # --- 1. Cek dan Baca File JSON ---
        try:
            with open(json_file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"✅ File '{json_file_path}' berhasil dibaca.")
        except FileNotFoundError:
            print(f"❌ Error: File '{json_file_path}' tidak ditemukan.")
            print("   Pastikan file ini ada di folder yang sama dengan 'run.py'.")
            return
        except json.JSONDecodeError:
            print(f"❌ Error: File '{json_file_path}' tidak berformat JSON yang valid.")
            return

        # --- 2. Proses Setiap Data ---
        added_count = 0
        updated_count = 0
        skipped_count = 0

        for item in data:
            question = item.get('question')
            answer = item.get('answer')

            # Lewati jika data tidak lengkap
            if not question or not answer:
                print(f"⚠️  Melewati item tidak valid: {item}")
                skipped_count += 1
                continue

            # Cek apakah pertanyaan sudah ada di database
            existing_qna = QnA.query.filter_by(question=question).first()
            
            if existing_qna:
                # Jika sudah ada, update jawabannya
                existing_qna.answer = answer
                updated_count += 1
            else:
                # Jika belum ada, buat entri baru
                new_qna = QnA(question=question, answer=answer)
                db.session.add(new_qna)
                added_count += 1
        
        # --- 3. Simpan Perubahan ke Database ---
        try:
            db.session.commit()
            print("\n-------------------------------------------------")
            print("         ✅ Impor data dari JSON SELESAI!         ")
            print("-------------------------------------------------")
            print(f"📝 Data baru yang ditambahkan: {added_count}")
            print(f"🔄 Data yang diperbarui     : {updated_count}")
            print(f"⚠️  Data yang dilewati       : {skipped_count}")
            print("-------------------------------------------------")
        except Exception as e:
            # Jika terjadi error, batalkan semua perubahan
            db.session.rollback()
            print(f"\n❌ Terjadi kesalahan saat menyimpan ke database: {e}")

if __name__ == '__main__':
    import_qna_from_json()