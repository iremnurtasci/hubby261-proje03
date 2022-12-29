import tkinter as tk
from tkinter import scrolledtext
import string
from gensim.models import KeyedVectors

pencere = tk.Tk()
pencere.title("Benzer Kelime Bulma Optimizasyonu")

arayuz = tk.Label(pencere, text="Kelime Bulma Optimizasyonuna Hoş Geldiniz!" "\n" 
"Arama kutucuğuna bir veya birden fazla kelime girebilirsiniz. Girdiğiniz anahtar kelimeye benzer kelimelere ulaşabilirsiniz." "\n" )
arayuz.grid(column=0, row=0)
arayuz.pack()

def gensimUygula():
    kelimeVektoru = KeyedVectors.load_word2vec_format('trModel100', binary=True)
    print("Model Yükleniyor...")
    anahtarKelimeler = input("Anahtar Kelime: ").lower()
    print("Girilen Kelime : " + str(anahtarKelimeler))
    kelimeler = anahtarKelimeler.split()
    for i in kelimeler:
        if i in string.punctuation:
            print("Lütfen noktalama işareti kullanmayınız!")
    oneriler = []
    for kelime in kelimeler:
        oneriler.extend(kelimeVektoru.most_similar(positive=kelime))
    print(oneriler)
    # Önerilerin Rafine olduğu kısım
    for index, oneri in enumerate(oneriler):
        if anahtarKelimeler not in oneri[0]:
            print(index + 1, "https://www.google.com.tr/search?q=" + oneri[0])
        if anahtarKelimeler in oneri[0]:
            print(index + 1, i + " kelimesiyle aynı köke sahip olduğu için temizlenmiştir.")


    kelimeler = anahtarKelimeler.split()
    temizlenenKelimeler = []
    for kelime in kelimeler:
        temizlenenKelime = ""
        for i in kelime:
            if i not in string.punctuation:
                temizlenenKelime += i
        temizlenenKelimeler.append(temizlenenKelime)

    print("Temizlenen Kelimeler Listesi ")
    print(temizlenenKelimeler)

kelimeGir = tk.StringVar()
kelimeGir = tk.Entry(pencere, width=20, textvariable=kelimeGir)
kelimeGir.pack()
button = tk.Button(pencere, text="Kelime Gir", command=gensimUygula)
button.pack()
sonuc = scrolledtext.ScrolledText(pencere, width=100, height=10)

gensimUygula()

pencere.mainloop()
