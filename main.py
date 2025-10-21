import os
import threading
import time
import numpy as np
import sounddevice as sd
import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
import subprocess
import win32print
import win32com.client

# ======================
# 🔊 Text-to-Speech
# ======================
engine = pyttsx3.init()
engine.setProperty('rate', 165)

def speak(text):
    log(f"🤖 {text}")
    engine.say(text)
    engine.runAndWait()


# ======================
# 📂 File Management
# ======================
def get_first_file():
    folder = os.path.join(os.getcwd(), "files")
    if not os.path.exists(folder):
        os.makedirs(folder)
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    if not files:
        return None
    return os.path.join(folder, files[0])

def open_file(filepath):
    if os.path.exists(filepath):
        log(f"📂 Membuka file: {filepath}")
        try:
            os.startfile(filepath)
        except Exception as e:
            log(f"⚠️ Gagal membuka file: {e}")
            messagebox.showwarning("Gagal Membuka File", str(e))
    else:
        log("⚠️ File tidak ditemukan.")
        messagebox.showerror("File Tidak Ditemukan", "File tidak ditemukan di folder 'files'.")


# ======================
# 🖨️ Printer Management
# ======================
def print_file(filepath):
    if not os.path.exists(filepath):
        speak("File tidak ditemukan.")
        messagebox.showerror("Error", "File tidak ditemukan.")
        return

    try:
        printer_name = win32print.GetDefaultPrinter()
    except:
        printer_name = None

    if not printer_name:
        speak("Printer belum terhubung, membuka file saja.")
        messagebox.showinfo("Printer Tidak Ditemukan", "Printer belum terhubung. Membuka file saja.")
        open_file(filepath)
        return

    ext = os.path.splitext(filepath)[1].lower()
    log(f"🖨️ Printer terdeteksi: {printer_name}")
    speak("Mencetak dokumen...")

    try:
        if ext == ".pdf":
            acrobat_path = r"C:\Program Files (x86)\Adobe\Acrobat Reader\Reader\AcroRd32.exe"
            if not os.path.exists(acrobat_path):
                acrobat_path = r"C:\Program Files\Adobe\Acrobat Reader\Reader\AcroRd32.exe"
            if os.path.exists(acrobat_path):
                subprocess.run([acrobat_path, "/t", filepath, printer_name], shell=True)
            else:
                log("⚠️ Adobe Reader tidak ditemukan. File dibuka saja.")
                open_file(filepath)
        elif ext == ".docx":
            word = win32com.client.Dispatch("Word.Application")
            doc = word.Documents.Open(os.path.abspath(filepath))
            doc.PrintOut()
            doc.Close(False)
            word.Quit()
        else:
            speak("Format file belum didukung untuk print otomatis.")
            messagebox.showinfo("Format Tidak Didukung", f"Tidak dapat mencetak file dengan format {ext}.")
            open_file(filepath)
    except Exception as e:
        log(f"⚠️ Gagal mencetak: {e}")
        messagebox.showerror("Gagal Mencetak", str(e))


# ======================
# 🎧 Speech Recognition
# ======================
def listen_command(timeout=5):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            log("🎙️ Mendengarkan perintah suara...")
            audio = recognizer.listen(source, timeout=timeout)
            command = recognizer.recognize_google(audio, language="id-ID").lower()
            log(f"🗣️ Perintah terdeteksi: {command}")
            return command
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            log("⚠️ Gagal mengakses layanan pengenalan suara.")
            return None


# ======================
# 👏 Deteksi Tepukan
# ======================
def detect_claps(duration=3, threshold=0.25):
    fs = 44100
    log("👂 Mendeteksi tepukan tangan...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()

    data = np.abs(recording)
    peaks = np.where(data > threshold)[0]

    if len(peaks) == 0:
        return 0

    times = peaks / fs
    claps = []
    prev_time = times[0]
    for t in times:
        if t - prev_time > 0.25:
            claps.append(prev_time)
            prev_time = t
    claps.append(prev_time)

    log(f"👏 Jumlah tepukan terdeteksi: {len(claps)}")
    return len(claps)


# ======================
# 🧠 Log ke GUI
# ======================
def log(message):
    log_box.insert(tk.END, f"{message}\n")
    log_box.see(tk.END)


# ======================
# 🚀 Thread Utama
# ======================
is_running = False

def run_voice_system():
    global is_running
    speak("Sistem print otomatis diaktifkan.")
    while is_running:
        command = listen_command(timeout=5)
        file_path = get_first_file()

        if not file_path:
            speak("Folder files kosong. Tambahkan file terlebih dahulu.")
            time.sleep(3)
            continue

        if command:
            if "open file" in command or "buka file" in command:
                speak("Baik, sedang membuka file.")
                open_file(file_path)

            elif "print file" in command or "cetak file" in command:
                speak("Baik, mencetak dokumen.")
                print_file(file_path)

            elif "stop program" in command or "hentikan program" in command:
                speak("Program dihentikan.")
                stop_program()
                break

            else:
                log("Perintah tidak dikenali.")
        else:
            clap_count = detect_claps(duration=3, threshold=0.25)
            if clap_count == 2:
                speak("Dua tepukan tangan terdeteksi. Mencetak file otomatis.")
                print_file(file_path)
        time.sleep(1)


def start_program():
    global is_running
    if is_running:
        messagebox.showinfo("Info", "Program sudah berjalan.")
        return
    is_running = True
    threading.Thread(target=run_voice_system, daemon=True).start()
    log("🟢 Sistem dimulai.")


def stop_program():
    global is_running
    if not is_running:
        return
    is_running = False
    log("🔴 Sistem dihentikan.")


def exit_program():
    stop_program()
    root.destroy()


# ======================
# 🪟 GUI
# ======================
root = tk.Tk()
root.title("🎙️ Voice Print System")
root.geometry("720x520")
root.resizable(False, False)

title = tk.Label(root, text="🖨️ Sistem Print Otomatis Berbasis Suara", font=("Segoe UI", 14, "bold"))
title.pack(pady=10)

frame_btn = tk.Frame(root)
frame_btn.pack(pady=10)

btn_start = tk.Button(frame_btn, text="▶️ Start", command=start_program, width=12, bg="#4CAF50", fg="white")
btn_start.grid(row=0, column=0, padx=10)

btn_stop = tk.Button(frame_btn, text="⏹ Stop", command=stop_program, width=12, bg="#f44336", fg="white")
btn_stop.grid(row=0, column=1, padx=10)

btn_exit = tk.Button(frame_btn, text="❌ Exit", command=exit_program, width=12, bg="#555", fg="white")
btn_exit.grid(row=0, column=2, padx=10)

log_box = scrolledtext.ScrolledText(root, width=85, height=20, font=("Consolas", 10))
log_box.pack(padx=10, pady=10)

log("💻 Program siap dijalankan.")
log("Letakkan file di folder 'files' (nama bebas).")
log("Katakan: 'open file', 'print file', 'stop program', atau tepuk dua kali.")

root.mainloop()
