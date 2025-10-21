
🖨️ Auto Clap & Voice Print System

Aplikasi desktop berbasis Python untuk mengotomatisasi pencetakan dokumen menggunakan perintah suara atau deteksi tepukan tangan. Didesain untuk kemudahan akses dan produktivitas pada sistem operasi Windows.

✨ Fitur Utama

-Kontrol Suara (Voice Control): Berikan perintah suara langsung dalam Bahasa Indonesia untuk mengendalikan sistem ("buka file", "print file", "hentikan program").
-Deteksi Tepukan Tangan (Clap Detection): Cukup tepuk tangan sebanyak dua kali untuk memicu perintah pencetakan otomatis.
-Dukungan Multi-Format
-Mampu mencetak file PDF secara otomatis menggunakan Adobe Acrobat Reader (memerlukan instalasi Adobe Reader).
-Mampu mencetak file DOCX secara otomatis menggunakan Microsoft Word COM automation (memerlukan instalasi MS Word).
-Text-to-Speech (TTS): Sistem memberikan umpan balik suara untuk setiap aksi yang dideteksi.
-Antarmuka Pengguna Grafis (GUI) Sederhana: Kontrol sistem melalui antarmuka tkinter yang minimalis dengan tombol Start, Stop, dan kotak log (log box).

🛠️ Teknologi yang Digunakan

Proyek ini dibangun dengan Python dan mengandalkan pustaka berikut:
-Python 3.x
-SpeechRecognition (untuk pengenalan suara, menggunakan layanan Google Speech Recognition)
-Sounddevice & NumPy (untuk memproses input audio dan mendeteksi pola tepukan tangan)
-Pyttsx3 (untuk fungsionalitas Text-to-Speech)
-PyWin32 (untuk interaksi dengan sistem Windows, seperti manajemen printer dan Microsoft Word COM)
-Tkinter (untuk antarmuka pengguna grafis)

⚙️ Prasyarat Instalasi

1. Sistem Operasi: Windows (Karena penggunaan pustaka pywin32 untuk fungsi printer dan COM).
2. Perangkat Keras: Mikrofon yang berfungsi dengan baik.
3. Perangkat Lunak Tambahan:
    -PortAudio: Diperlukan untuk PyAudio yang merupakan dependensi dari SpeechRecognition. Anda mungkin perlu menginstal binari PortAudio secara manual jika instalasi PyAudio melalui pip install PyAudio gagal.
    -Adobe Acrobat Reader (Untuk mencetak file PDF).
    -Microsoft Word (Untuk mencetak file DOCX).

Langkah-langkah Instalasi

1. Clone Repository
Bash
git clone <URL_REPO_ANDA>
cd auto-clap-print


2. Buat Virtual Environment (Opsional, tapi Direkomendasikan)
Bash
python -m venv venv
.\venv\Scripts\activate


3. Instal Dependensi
Bash
pip install -r requirements.txt


4. Buat Folder File
Pastikan folder files ada di direktori root proyek.
Bash
mkdir files



📂 Susunan Project

auto-clap-print/
├── files/
│   └── (tempat file dokumen diletakkan, contoh: test.pdf)
├── main.py             # Logika inti program dan Antarmuka GUI
└── requirements.txt    # Daftar dependensi Python



🚀 Contoh Penggunaan

1. Siapkan Dokumen: Tempatkan file yang ingin Anda cetak (misalnya, laporan.pdf atau surat.docx) di dalam folder files/. Program akan selalu memproses file pertama yang ditemukan di folder ini.
2. Jalankan Program
Bash
python main.py


3. Mulai Sistem
Klik tombol ▶️ Start pada GUI.
Kotak log akan menampilkan pesan: "Sistem print otomatis diaktifkan."
4. Perintah Otomatis
Metode Perintah
Aksi
Perintah Suara (Bahasa Indonesia)
Suara
Buka dokumen pertama di files/
"buka file" atau "open file"
Suara
Cetak dokumen pertama di files/
"cetak file" atau "print file"
Tepukan
Cetak dokumen pertama di files/
Tepuk Tangan Dua Kali 👏 👏
Suara/GUI
Hentikan sistem
"hentikan program" atau "stop program" / Klik tombol ⏹ Stop atau ❌ Exit


🤝 Kontribusi

Kontribusi disambut dengan baik! Jika Anda memiliki ide atau perbaikan, silakan:
1. Fork proyek ini.
2. Buat branch untuk fitur baru (git checkout -b feature/AmazingFeature).
3. Commit perubahan Anda (git commit -m 'Add some AmazingFeature').
4. Push ke branch (git push origin feature/AmazingFeature).
5. Buka Pull Request.
