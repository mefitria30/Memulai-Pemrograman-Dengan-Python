## Tipe Data Primitif

# Berikut adalah implementasi tipe data numbers ke dalam Python.
x = 6
print(type(x))

x = 6.0
print(type(x))

x = 1+2j
print(type(x))

# Tipe data numbers bersifat immutable yang artinya nilai di dalamnya tidak dapat diubah.

var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))

# Tipe data primitif kedua adalah boolean, yakni tipe data yang hanya bernilai TRUE atau FALSE. 

x = True
print(type(x))

x = False
print(type(x))

#  Ketika Anda membuat variabel bernilai string tentu diawali dengan single quote (‘’) atau double quote (“”). 

x = 'Fitria Melliyanni'
print(type(x))

# tiga single quote atau double quote untuk menyimpan string yang lebih dari satu baris (multi-line).

multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""

print(multi_line)

# String merupakan urutan karakter yang setiap karakternya memiliki indeks. 

x = 'Fitria Melliyanni'
print(x[0])
print(x[8])

# mengakses beberapa substring dengan menggunakan metode indexing dan slicing.

x = 'Fitria'
print(x[2:])

# menampilkan teks/string berdasarkan input dari pengguna
# 1. Formatted String -> Metode ini diperuntukkan untuk menampilkan variabel bertipe string dengan menggunakan huruf “f” 

name = "Fitria Melliyanni"
print(f"Hello, nama saya {name}")

# 2. %-formatting -> Metode ini menggunakan operator Modulo (%) untuk memasukkan nilai variabel ke dalam string dengan menggunakan format khusus yang ditentukan oleh tipe data variabel.

name = "Fitria Melliyanni"
print("Nama saya %s" % (name))

# 3. str.format() -> Metode ini memungkinkan penggabungan variabel/nilai ke dalam string dengan menempatkan tanda kurung kurawal atau {} sebagai penempatan variabel.

name = "Fitria Melliyanni"
print("Nama saya {}".format(name))


## Tipe Data Collection

# inisialisasi list pada Python cukup mudah, yakni menggunakan kurung siku “[]” dan setiap elemennya dipisahkan dengan koma. 

x = [1, 2.2, 'python']
print(type(x))

x = [1, 'python', True, 1.0]

print(x[3])

# List Python bersifat mutable yang artinya nilai di dalamnya dapat diubah.

x = [1, 2.2, 'python']
x[0] = 'Indonesia'
print(x)


# Konsep indexing merujuk kepada pengambilan data dalam Python berdasarkan indeksnya.

x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0])
print(x[2])
print(x[-1])
print(x[-3])


# Pada dua sintaks pertama, Anda memerintahkan untuk menampilkan indeks ke-0 dan indeks ke-2. Selanjutnya, dua sintaks terakhir memerintahkan untuk menampilkan indeks terakhir dan indeks ke-3 dari terakhir.


# konsep slicing merujuk pada pengambilan data berdasarkan indeks dari rentang tertentu.

# sequence[start:stop:step]
# Start merupakan indeks pertama yang Anda ambil. Stop merupakan indeks terakhir yang ingin Anda ambil. Step merupakan jumlah elemen yang ingin Anda lewati di antara setiap elemen slice. Secara default, nilai step adalah 1.

x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0:5:2])
print(x[1:])
print(x[:3])

# Pada sintaks pertama, Anda memerintahkan untuk mengambil data dari indeks ke-0 hingga indeks ke-4 dengan setiap elemen ke-2 dan kelipatannya akan dilewati. Pada sintaks kedua, Anda memerintahkan untuk menampilkan data dari indeks ke-1 hingga terakhir. Pada sintaks ketiga, Anda memerintahkan untuk menampilkan data dari indeks ke-0 hingga indeks ke-2 (ingat, bersifat eksklusif).


# Tuple adalah jenis dari list yang tidak dapat diubah elemennya.
x = (1, "python", 1+3j)
print(type(x))


#  melakukan indexing dan slicing pada tuple sama seperti list. 
x = (5, 'program', 1+3j)
print(x[1])
print(x[0:3])

# Tuple bersifat immutable yang artinya tidak dapat diubah.

# set merupakan kumpulan item tanpa urutan. 
# Set juga bersifat unik, artinya, data yang Anda simpan pada set tidak akan ada duplikat. 

x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))


# Method merupakan tindakan atau operasi yang dapat dilakukan oleh suatu objek.

# set adalah himpunan dalam matematika. Ini maknanya Anda dapat melakukan operasi union (gabungan) dan intersection (irisan) pada set. Python menyediakan method “.union()” dan “.intersection()” untuk tipe data set.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection:", intersection)

# Dictionary pada Python merupakan kumpulan pasangan key-value yang bersifat tidak berurutan. 

x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }

print(type(x))

# mencoba mengakses data pada dictionary dengan menggunakan metode indexing.

x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }

print(x ['name'])

# Menambah Data pada Dictionary

x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
x ['Job'] = "Web Developer"

print(x)

# Menghapus Data pada Dictionary

x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
del x['isMarried']

print(x)

# Mengubah Data pada Dictionary
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
x ['name'] = "python"

print(x)

# Konversi Integer ke Float
print(float(5))

# Konversi Float ke Integer
print(int(5.6))
print(int(-5.6)) 

# Konversi dari-dan-ke String

print(int("25"))
print(str(25))
print(float("25"))
print(str(25.6))

# Konversi Kumpulan Data

print(set([1,2,3]))
print(tuple({5,6,7}))
print(list('hello'))


# Konversi ke Dictionary
print(dict([[1,2],[3,4]]))

# Konversi list dari beberapa tuple yang isinya pasangan nilai menjadi dictionary.

print(dict([(3,26),(4,44)]))