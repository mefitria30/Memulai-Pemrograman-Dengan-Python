# len() bertujuan untuk menghitung panjang atau banyaknya elemen dari list, set, dan string.

# List

contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]

print(contoh_list)
print(len(contoh_list))


print ('-----------------------------------')


# Set

contoh_list = set([1, 3, 3, 5, 5, 5, 7, 7, 9])

print(contoh_list)
print(len(contoh_list))

print ('-----------------------------------')


# String
contoh_list = "Fitria Melliyanni"

print(contoh_list)
print(len(contoh_list))

print ('-----------------------------------')

# min() dan max() -> mengetahui berapa nilai minimum dan maksimum dari suatu list menggunakan fungsi min() dan max().


angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))

print ('-----------------------------------')


# count() digunakan untuk mengetahui berapa kali suatu objek muncul dalam list.

genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))

print ('-----------------------------------')


string = "Fitria adalah orang yang sangat menyenangkan"
substring = "a"
print(string.count(substring))

print ('-----------------------------------')


# In dan not in merupakan operator yang diperuntukkan untuk mengetahui nilai atau objek yang ada dalam list.

kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)

print ('-----------------------------------')


# Memberikan Nilai untuk Multiple Variable

data = ['shirt', 'white', 'L']
apparel, color, size = data

print(data)
print(apparel)
print(color)
print(size)


# fungsi sort() untuk mengurutkan angka atau urutan huruf.

kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()

print(kendaraan)


#  membalikkan urutan fungsi sort()

kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True)

print(kendaraan)

print ('-----------------------------------')

# Metode sort menggunakan urutan ASCII sehingga nilai huruf kapital (uppercase) akan lebih dahulu dibandingkan huruf kecil (lowercase).

kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort()

print(kendaraan)