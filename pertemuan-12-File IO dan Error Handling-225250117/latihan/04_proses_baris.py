with open("data/nilai.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()

        if not baris:
            continue

        # Pisahkan NIM dan nilai berdasarkan koma
        nim, teks_nilai = baris.split(",")

        # Ubah teks_nilai (indeks ke-1 setelah split) menjadi float
        print(nim, float(teks_nilai))