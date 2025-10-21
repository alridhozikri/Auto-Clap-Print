# 🖨️ Auto Clap & Voice Print System

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Aplikasi desktop berbasis Python untuk **mengotomatisasi pencetakan dokumen** menggunakan perintah suara atau deteksi tepukan tangan. Didesain untuk kemudahan akses dan produktivitas pada sistem operasi Windows.

## ✨ Fitur Utama

* **Kontrol Suara (Voice Control)**: Berikan perintah suara langsung dalam Bahasa Indonesia untuk mengendalikan sistem ("buka file", "print file", "hentikan program").
* **Deteksi Tepukan Tangan (Clap Detection)**: Cukup tepuk tangan sebanyak **dua kali** untuk memicu perintah pencetakan otomatis.
* **Dukungan Multi-Format Print Otomatis**:
    * Mencetak file **PDF** secara otomatis menggunakan Adobe Acrobat Reader (memerlukan instalasi Adobe Reader).
    * Mencetak file **DOCX** secara otomatis menggunakan Microsoft Word COM automation (memerlukan instalasi MS Word).
* **Antarmuka GUI Desktop**: Kontrol yang mudah digunakan dengan tombol **Start**, **Stop**, dan kotak log *real-time* menggunakan `tkinter`.
* **Umpan Balik Suara (Text-to-Speech)**: Memberikan konfirmasi suara untuk setiap tindakan sistem.

***

## ⚙️ Teknologi yang Digunakan

Proyek ini dibangun menggunakan **Python** dan memanfaatkan pustaka-pustaka khusus untuk integrasi dengan sistem operasi Windows dan pemrosesan audio.

* **Inti**: Python 3.x
* **GUI**: `tkinter`
* **Audio I/O & Pemrosesan**: `sounddevice`, `numpy`
* **Pengenalan Suara**: `SpeechRecognition` (menggunakan Google Speech Recognition API)
* **Text-to-Speech**: `pyttsx3`
* **Integrasi Windows**: `pywin32` (untuk manajemen printer, COM Automation)

***

## 📋 Prasyarat Instalasi

1.  **Sistem Operasi**: Windows (Diperlukan karena penggunaan `pywin32` untuk fungsi printer).
2.  **Perangkat Keras**: Mikrofon yang terhubung dan berfungsi.
3.  **Aplikasi Tambahan**:
    * **Adobe Acrobat Reader** (untuk mencetak file PDF)
    * **Microsoft Word** (untuk mencetak file DOCX)

### Langkah-langkah

1.  **Clone Repositori:**

    ```bash
    git clone <URL_REPO_ANDA>
    cd auto-clap-print
    ```

2.  **Instal Dependensi:**

    ```bash
    pip install -r requirements.txt
    ```

    *Catatan*: Instalasi pustaka `PyAudio` (dependensi dari `SpeechRecognition`) mungkin memerlukan [PortAudio](http://www.portaudio.com/download.html) pada beberapa sistem.

3.  **Siapkan Folder Dokumen:**

    Pastikan Anda membuat folder bernama `files` di direktori root proyek.

    ```bash
    mkdir files
    ```

***

## 🖥️ Contoh Penggunaan

1.  **Tempatkan File**: Letakkan dokumen yang ingin Anda cetak (misalnya, `dokumen_penting.pdf` atau `proposal.docx`) di dalam folder **`files/`**. Aplikasi akan selalu mengambil **file pertama** di dalam folder tersebut.
2.  **Jalankan Aplikasi**:
    ```bash
    python main.py
    ```
3.  **Mulai Sistem**: Klik tombol **▶️ Start**.
4.  **Berikan Perintah**:

| Perintah | Pemicu | Aksi |
| :--- | :--- | :--- |
| **Suara** | "buka file" | Membuka file pertama di folder `files`. |
| **Suara** | "print file" | Mencetak file pertama di folder `files` ke printer default. |
| **Tepukan** | Tepuk Tangan 2x 👏 👏 | Mencetak file pertama di folder `files` secara otomatis. |
| **Suara** | "hentikan program" | Menghentikan sistem deteksi suara/tepukan. |

***

## 🛠️ Kontribusi

Kontribusi dalam bentuk *pull request* sangat kami hargai. Untuk berkontribusi, silakan ikuti langkah-langkah berikut:

1.  *Fork* proyek ini.
2.  Buat *Branch* Fitur baru (`git checkout -b feature/nama-fitur-keren`).
3.  *Commit* perubahan Anda (`git commit -m 'feat: Menambahkan fitur keren'`).
4.  *Push* ke *Branch* (`git push origin feature/nama-fitur-keren`).
5.  Buka **Pull Request**.

## ⚖️ Lisensi

Proyek ini dilisensikan di bawah **Lisensi MIT** - lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.

## 👤 Author

* **Github :** [**@alridhozikri**](https://github.com/alridhozikri)

***
