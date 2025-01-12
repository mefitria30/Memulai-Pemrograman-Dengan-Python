print("Selamat datang dalam program Python!\n")
print("Silakan masukkan data diri Anda.")
nama = input("Masukkan nama Anda: ")
tahun_lahir = input("Masukkan tahun lahir Anda: ")
umur = 2025 - int(tahun_lahir)
 
print(f"Selamat datang {nama} dalam program Python, per 2023 umur Anda adalah {umur} tahun.\n")
print("Terima kasih telah menggunakan program Python!")


print('---------------------------------')

# program yang hasilnya TIDAK akan berubah jika urutan baris instruksinya diubah.

a = 6
b = 9
 
result = a + b
print(result)


print('-----------------------')


#  urutan instruksi yang mengubah hasil
a = 6
b = 9
 
print(a**2)
print(b//3)