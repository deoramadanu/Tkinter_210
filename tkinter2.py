import tkinter as tk

# Membuat jendela utama
root = tk.Tk() # membuat jendela utama aplikasi.
root.title("Aplikasi Prediksi Prodi Pilihan") # memberi judul pada jendela.
root.geometry("400x600") # memberi ukuran layar
root.configure(bg="lightblue")  # warna latar belakang

# Label judul
label_judul = tk.Label(root, # untuk menampilkan di GUI
                       text="Aplikasi Prediksi Prodi Pilihan", # teks yang ingin ditampilkan
                       font=("Arial", 16, "bold"), # fontnya apa, ukurannya
                       bg="blue", fg="white", # untuk mengatur warna
                       pady=10) # memberikan jarak
label_judul.pack(fill="x", pady=(0, 20)) # membuat label memanjang secara horizontal di jendela.

# Frame untuk input nilai
frame_nilai = tk.Frame(root, bg="lightblue") # Wadah atau tempat untuk mengelompokkan
frame_nilai.pack(pady=10) # memberikan jarak

# Membuat label dan entry untuk 10 mata pelajaran
entries = []
for i in range(1, 11):
    label = tk.Label(frame_nilai, 
                     text=f"Nilai Mata Pelajaran {i}:", 
                     bg="lightblue", font=("Arial", 11))
    label.grid(row=i, column=0, sticky="w", padx=10, pady=5)
    
    entry = tk.Entry(frame_nilai, width=20)
    entry.grid(row=i, column=1, pady=5)
    entries.append(entry)

# Fungsi hasil prediksi
def hasil_prediksi():
    label_hasil.config(text="Hasil Prediksi: Teknologi Informasi", fg="green")

# Tombol untuk menampilkan hasil
btn_hasil = tk.Button(root, 
                      text="Hasil Prediksi", 
                      command=hasil_prediksi, 
                      bg="blue", fg="white", 
                      font=("Arial", 12, "bold"), 
                      padx=10, pady=5)
btn_hasil.pack(pady=20)

# Label hasil prediksi
label_hasil = tk.Label(root, 
                       text="Hasil Prediksi: -", 
                       font=("Arial", 12, "bold"), 
                       bg="lightblue", fg="darkblue")
label_hasil.pack(pady=10)

# Menjalankan GUI
root.mainloop()
