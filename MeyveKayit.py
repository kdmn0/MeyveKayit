import tkinter as tk

dosya_adi = "kayitlar.txt"
kayitlar = {}

# Dosyadan oku
try:
    with open(dosya_adi, "r", encoding="utf-8") as f:
        for satir in f:
            isim, kg = satir.strip().split(",")
            kayitlar[isim] = float(kg)
except FileNotFoundError:
    pass

# Dosyaya yaz
def dosyaya_yaz():
    with open(dosya_adi, "w", encoding="utf-8") as f:
        for isim, kg in kayitlar.items():
            f.write(f"{isim},{kg}\n")

# Ekle fonksiyonu
def ekle():
    isim = entry_isim.get()
    kg = entry_kg.get()

    if not isim or not kg:
        return

    kg = float(kg)

    if isim in kayitlar:
        kayitlar[isim] += kg
    else:
        kayitlar[isim] = kg

    listeyi_guncelle()
    dosyaya_yaz()

    entry_isim.delete(0, tk.END)
    entry_kg.delete(0, tk.END)

# Listeyi güncelle
def listeyi_guncelle():
    liste.delete(0, tk.END)
    for isim, kg in kayitlar.items():
        liste.insert(tk.END, f"{isim} → {kg} kg")

# Pencere
pencere = tk.Tk()
pencere.title("MeyveKayıt")

tk.Label(pencere, text="Müşteri Adı").pack()
entry_isim = tk.Entry(pencere)
entry_isim.pack()

tk.Label(pencere, text="Kg").pack()
entry_kg = tk.Entry(pencere)
entry_kg.pack()

tk.Button(pencere, text="Ekle", command=ekle).pack(pady=5)

liste = tk.Listbox(pencere, width=40)
liste.pack()

listeyi_guncelle()
pencere.mainloop()
