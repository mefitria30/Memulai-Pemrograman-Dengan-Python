# For termasuk sintaks dalam Python yang bersifat definite iteration. Definite iteration adalah sebuah proses iterasi atau perulangan ketika jumlah pengulangannya ditentukan secara eksplisit sebelumnya.


# menampilkan angka dari 1 hingga 10 berdasarkan variable list yang sudah diinisialisasikan sebelumnya. 
var_list = [1,2,3,4,5,6,7,8,9,10]
for i in var_list:
    print(i)

print('--------------------------------')

# melakukan perulangan berdasarkan panjang suatu nilai dengan menggunakan fungsi "range()".

for i in range(30):
    print(i)


print('--------------------------------')

for i in range(1,10,2):
    print(i)

print('--------------------------------')

# While termasuk sintaks dalam Python yang bersifat indefinite iteration. Indefinite iteration adalah sebuah proses iterasi yang akan berhenti ketika memenuhi kondisi tertentu.

counter = 1
while counter <= 5:
    print(counter)
    counter += 1    # Increment

print('--------------------------------')

# For Bersarang 
for i in range(1, 3):
    for j in range(1, 3):
        print(i,j)

print('--------------------------------')

# Kontrol Perulangan

# Break statement adalah pernyataan untuk menghentikan perulangan dan kemudian program akan otomatis keluar dari perulangan tersebut, lalu dilanjutkan dengan mengeksekusi blok perulangan selanjutnya.

for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 1:
            break  # Menghentikan perulangan dalam jika j = 1

print('--------------------------------')

for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))

print('--------------------------------')


# Continue statement adalah pernyataan untuk membuat iterasi berhenti, kemudian melanjutkan ke iterasi berikutnya.

for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))

print('--------------------------------')


# else setelah for yang berfungsi untuk perulangan bersifat pencarian. 

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan.")

print('--------------------------------')


#  else setelah while, blok statement else akan selalu dieksekusi saat kondisi pada while menjadi salah. 

count = 0

while count < 3:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")

print('--------------------------------')

n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")

print('--------------------------------')


# Pass statement adalah pernyataan yang digunakan jika Anda menginginkan sebuah pernyataan atau blok pernyataan (statement), tetapi tidak ada tindakan atau program tidak melakukan apa pun.

x = 10

if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")

print('--------------------------------')


# List Comprehension -> sebuah cara untuk menghasilkan list baru berdasarkan list atau iterables yang telah ada sebelumnya.

angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
  pangkat.append(n**2)
print(pangkat)

print('--------------------------------')

# atau dengan bentuk seperti ini

angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)