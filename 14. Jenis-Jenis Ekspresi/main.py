# Ekspresi Menurut Arity dari Operator

# Biner

# (x + y), (x - y), (x * y), (x / y), (x ** y), (x < y), (x <= y), (x > y), (x >= y), (x % y), (x == y), (x != y).

# Uner

# (x += 1), (x-=1), (not x).

# penerapan ekspresi uner.

a = True
a = not a
print(a)

b = 6
b -= 1
print(b)

c = 6
c += 1
print(c)

d = 10
print(-d)


print('---------------------------')

# Ekspresi Menurut Tipe Data yang Dihasilkan

#Ekspresi aritmetika: jenis ekspresi yang memiliki operan bertipe numerik dan menghasilkan numerik.
# Ekspresi relasional: jenis ekspresi yang memiliki operan bertipe numerik dan menghasilkan nilai boolean/logika.
# Ekspresi logika: jenis ekspresi yang memiliki operan bertipe boolean/logika dan menghasilkan nilai boolean/logika.

print(2+2)
print(3<10)
print(True or False)