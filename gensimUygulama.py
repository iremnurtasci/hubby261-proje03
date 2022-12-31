import tkinter as tk
from gensim.models import KeyedVectors
print("Model Yükleniyor...")
kelimeVektoru = KeyedVectors.load_word2vec_format('trModel100', binary=True)
print(kelimeVektoru)

pencere = tk.Tk()
pencere.title("Benzer Kelimeler Bulma Optimizasyonu")


etiket = tk.Label(pencere, text="Kelime Bulma Optimizasyonuna Hoş Geldiniz!" "\n" 
"Arama kutucuğuna bir veya birden fazla kelime girebilirsiniz. Girdiğiniz anahtar kelimeye benzer kelimelere ulaşabilirsiniz." "\n" )
etiket.pack()

kelimeGir = tk.Entry(pencere)
kelimeGir.pack()


def benzerKelimeler():
    anahtarKelimeler = kelimeGir.get().lower()
    benzerKelimelerListesi = anahtarKelimeler.split()
    oneriler = []
    for anahtarKelime in benzerKelimelerListesi:
        print("Girilen Kelime: " + "".join(anahtarKelime))
        oneriler = (kelimeVektoru.most_similar(positive=anahtarKelime))
        sonuc = '\n'.join(f"{oneri[0]}: {oneri[1]:.4f}" for oneri in oneriler)

        #Önerileri rafine eden kısım
        for oneri in oneriler:
            if anahtarKelime not in oneri[0]:
                print("https://www.google.com.tr/search?q=" + oneri[0])
        arayuzeYazdir = tk.Text(pencere)
        arayuzeYazdir.insert(tk.END, sonuc)
        arayuzeYazdir.pack()

def cikis():
    pencere.destroy()

button1 = tk.Button(pencere, text="Kelime Gir", command=benzerKelimeler)
button1.pack()

button2 = tk.Button(pencere, text="Çıkış Yap", command=quit)
button2.pack()

pencere.mainloop()