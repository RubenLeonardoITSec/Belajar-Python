#!/usr/bin/python3
# pada 7 oktober 2021 hari kamis, pukul 23:00 WIB, saya belajar dasar bahasa pemrograman python3
# Tetap semangat belajar sampai bisa :)


# bersihkan tampilan layar
import os, sys
os.system("clear")



# Apa itu variabel?
# variabel adalah nama penyimpanan data di memori komputer, dan nilai data
# dari suatu variabel dapat berubah-ubah
# Variabel kita ibaratkan sebagai ember yang dapat menampung nilai atau data


# Variabel dapat menyimpan berbagai macam tipe data. Contoh:
# 1. Tipe data teks (string) maka harus diapit dengan tanda petik ("Ruben").
# 2. Angka (integer) = 20
# 3. Boolean tidak perlu diapit dengan tanda petik. = True 
# Atau 0 dan 1.
# True = Benar
# False =  salah
# 4. Tipe data float = bilangan koma. contoh: 1.5, 23.12, 15.8
# 5. Tipe data char. contoh: "R"


# Fungsi-fungsi untuk mengubah tipe data:
# int() untuk mengubah menjadi integer
# long() untuk mengubah menjadi integer panjang
# float() untuk mengubah menjadi float
# bool() untuk mengubah menjadi boolean
# chr() untuk mengubah menjadi karakter
# str() untuk mengubah menjadi string.
# bin() untuk mengubah menjadi bilangan Biner.
# hex() untuk mengubah menjadi bilangan Heksadesimal.
# oct() untuk mengubah menjadi bilangan okta.



# Contoh kita buat program dari hasil belajar diatas
# Membuat Variabel di Python:
nama = "RubenLeonardo"
kelas = 11
# Untuk melihat isi variabel, kita dapat menggunakan fungsi print.
print(nama)
print(kelas)



# Menghapus Variabel
# Ketika sebuah variabel tidak dibutuhkan lagi, maka kita bisa menghapusnya dengan fungsi del().
os = "ubuntu"
print(os)
del(os) # fungsi del untuk menghapus variabel
# print(os)
# Pada perintah terakhir, kita akan mandapatkan NameError. 
# Artinya variabel tidak ada di dalam memori alias sudah dihapus.


# contoh variabel dengan tipe data int
angka = 5
# contoh variabel dengan tipe data string
situs = "https://www.petanikode.com/python-variabel-dan-tipe-data/"
# contoh variabel dengan tipe data boolean
menikah = False
# contoh variabel dgn tipe data float
tinggi = 175.8
# mencetak semua isi variabel
print("")
print("Angka: ", angka)
print("Situs: ", situs)
print("Tinggi: ", tinggi)
if(menikah):
	print("Status: Menikah")
else:
	print("Status: Belum Menikah")



# Contoh lagi
print("")
print("Khusus untuk variabel dgn tipe data string dapat diubah isinya: ")
namaku = "Ruben Leonardo"
print("")
print(namaku)
print(namaku.lower()) # untuk menghasilkan huruf kecil semua
print(namaku.upper()) # untuk menghasilkan huruf kecil KAPITAL
print(namaku.title()) # untuk menghasilkan huruf Kapital pada awal kata
print(namaku.replace("Leonardo", "Elliot")) # mengganti kata/karakter dalam string dgn kata/karakter yg lain
print(namaku.find("Leo")) # mencari suatu posisi karakter
print(namaku.split("[]"))
# fungsinya untuk memotong string dgn suatu pemisah untuk dijadikan list
print(namaku.isnumeric())
# fungsinya untuk mengetahui apakah semua karakter dalam string angka atau bukan
print("")