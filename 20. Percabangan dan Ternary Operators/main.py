ketersediaan = "Daging ayam"

if ketersediaan == "Daging ayam":
    print("Ibu membeli dan memasak ayam")
else:
    print("Ibu membeli dan memasak tempe")



print('-------------------------')


score = 100

if score == 100:
    print("Nilai Anda sempurna!")


print('-----------------------')

x = ""

if x:
    print("Ini True")
    


print('-----------------------')

# versi one-liner
score = 100

if score == 100: print("Nilai Anda sempurna!")


print('-----------------------')

tinggi_badan = 120

if tinggi_badan >=160:
    print("Anda boleh menaiki roller coaster")
else:
    print("Anda tidak diperbolehkan menaiki roller coaster")


print('-----------------------')

nilai = 65

if nilai>=80:
   print("Selamat! Anda mendapat nilai A")
   print("Pertahankan!")
elif nilai>=70:
   print("Hore! Anda mendapat nilai B")
   print("Tingkatkan!")
elif nilai>=60:
   print("Hmm.. Anda mendapat nilai C")
   print("Ayo semangat!")
else:
   print("Waduh, Anda mendapat nilai D")
   print("Yuk belajar lebih giat lagi!")


print('-----------------------')

nilai = 81
perilaku = 'tidak baik'

if nilai>=80 and perilaku == 'baik':
   print("Selamat! Anda mendapat nilai A dan telah berkelakuan baik")
   print("Pertahankan!")
elif nilai>=80 and perilaku != 'baik':
   print("Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik")
   print("Perbaiki lagi ya!")
else:
   print("Yuk belajar lebih giat lagi!")


# Ternary Operators
lulus = True
print("selamat") if lulus else print("perbaiki")

# bentuk blok normalnya:
lulus = True
if lulus:
    print("Selamat") 
else:
    print("Perbaiki")


# implementasi ternary tuples
lulus = True
kelulusan = ("Perbaiki, Anda belum lulus.","Selamat, Anda lulus!")[lulus]
print(kelulusan)

# bentuk normal blok nya:
lulus = True
if lulus:
    print("Selamat, Anda lulus!") 
else:
    print("Perbaiki, Anda belum lulus.")
