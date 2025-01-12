# Mengubah Huruf Besar/Kecil -> untuk mengubah string menjadi huruf kapital (UPPERCASE) atau huruf kecil (lowercase)

kata = 'fitria'
kata = kata.upper()
print(kata)

kata = 'MELLIYANNI'
kata = kata.lower()
print(kata)


# Awalan dan Akhiran -> metode dalam string yang biasanya dipergunakan untuk menghapus karakter whitespace pada suatu string atau untuk menghilangkan kata yang tidak diinginkan.

print("fitria1          ".rstrip()) # Metode rstrip() menghapus whitespace pada sebelah kanan atau akhir string.

print("           fitria2".lstrip()) # untuk menghapus whitespace pada sebelah kiri atau awal string.

print("         fitria3          ".strip()) # untuk menghapus whitespace pada bagian awal dan akhir string.

kata = 'CodeCodefitria4CodeCode'
print(kata.strip("Code"))  # menghilangkan karakter selain whitespace


# Metode startswith() bertujuan untuk menemukan suatu kata pada awal string. Metode ini mengembalikan nilai True.

print('fitria6 melliyanni'.startswith('fitria6'))


# Metode endswith() bertujuan untuk menemukan suatu kata pada akhir string. Metode ini juga mengembalikan nilai True jika menemukannya, sedangkan jika tidak menemukan kata yang diinginkan, nilai False dikembalikan.

print('fitria6 melliyanni'.endswith('melliyanni'))

# Memisah dan Menggabung String

# join()
print(' '.join(['fitria','melliyanni', '!']))
print('123'.join(['fitria','melliyanni']))

# metode split() bertujuan untuk memisahkan kata/substring berdasarkan delimiter.

print('fitria melliyanni !'.split())

# delimiter newline (\n) untuk memisahkan setiap baris pada string multiline.

print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n'))


# Mengganti Elemen String -> untuk mengganti elemen string di dalamnya dengan elemen string lainnya.

string = "Hi fitria, programmer"
print(string.replace("fitria", "mefitria30"))


# isupper() akan mengembalikan nilai True jika semua huruf dalam string adalah huruf kapital (uppercase). 

kata = 'FITRIA'
print(kata.isupper())

# islower() akan mengembalikan nilai True jika semua huruf dalam string adalah huruf kecil (lowercase). 

kata = 'fitria'
print(kata.islower())

# isalpha() -> Metode ini mengembalikan nilai True jika semua karakter dalam string adalah huruf alfabet. Jika ada satu huruf lain yang bukan alfabet, seperti angka, nilai False akan dikembalikan.

kata = 'mefitria30'
print(kata.isalpha())


kata = 'fitria'
print(kata.isalpha())

# isalnum() mengembalikan nilai True jika karakter dalam string adalah alfanumerik, yaitu hanya huruf atau hanya angka atau berisi keduanya. Jika tidak, nilai False akan dikembalikan.

print('-----------------------')

kata = 'mefitria30'
print(kata.isalnum())


kata = 'fitria@gmail.com'
print(kata.isalnum())


# Metode isdecimal() akan mengembalikan nilai True jika karakter dalam string berisi hanya angka/numerik. Jika tidak, nilai False akan dikembalikan.

print('-----------------------')

print('123'.isdecimal())

# Metode isspace() akan mengembalikan nilai True jika string hanya berisi whitespace, seperti spasi, tab, newline, atau karakter whitespace lainnya.

print('-----------------------')
print('         '.isspace())

# Metode istitle() mengembalikan nilai True jika string berisi huruf kapital pada setiap kata pertamanya. Jika tidak, nilai False dikembalikan.

print('Fitria Melliyanni'.istitle())

# Formatting pada String

# Metode zfill() bertujuan untuk menambahkan nilai nol (0) di depan sebuah string dengan panjang tertentu. Tujuan dari metode ini adalah membantu untuk memastikan bahwa sebuah angka atau nilai memiliki panjang tetap, terutama ketika ingin menyimpan nilai dalam format yang konsisten.

teks = 'Code'
tambah_number = teks.zfill(5)
print(tambah_number)

# Metode zfill() ini berguna ketika ingin memastikan bahwa angka atau nilai dalam string memiliki panjang tetap dan sesuai dengan format yang diinginkan. Metode zfill() dapat diterapkan untuk menetapkan nomor nota atau nomor antrian.


# rjust() berguna untuk merapikan pencetakan teks. Dengan metode rjust() ini, Anda dapat membuat teks menjadi rata kanan sehingga tampilannya lebih rapi.

print('fitria30'.rjust(20))

# rjust() akan menambahkan whitespace untuk membuat teks menjorok ke sebelah kanan. Angka 20 yang Anda masukkan bersifat sama seperti pada zfill(). 

print('30fitria30'.rjust(20, '!'))


# metode ljust(), bertujuan untuk membuat teks menjadi rata kiri.

print('fitria50'.ljust(20))

# Metode center() menjadikan teks rata tengah.

print('fitria'.center(10, '-'))


# String Literals

# Beberapa contoh escape character lainnya sebagai berikut. 

# \' Single quote
# \" Double quote
# \t Tab
# \n Newline (line break)
# \\ Backslash

print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.")


# Raw String -> digunakan untuk regex atau beberapa implementasi lain yang sangat bergantung pada keberadaan backslash.

print(r'fitria\tmelliyanni')
