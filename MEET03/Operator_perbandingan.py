'''
Operator perbandingan :
1. >
2. <
3. >=
4. <=
5. ==
6. !=
'''
a = 5
b = 10

print("-"*15, " > ")
hasil = a > b 
print( a, " > ", b , " = ", hasil)
hasil = a > 2
print( a, " > ", 2 , " = ", hasil)

print("-"*15, " < ")
hasil = a < b
print( a, " < ", b , " = ", hasil)
hasil = a < 2
print( a, " < ", 2 , " = ", hasil)

print("-"*15, " >= ")
hasil = a >= b 
print( a, " >= ", b , " = ", hasil)
hasil = a >= 2
print( a, " >= ", 2 , " = ", hasil)
hasil = a >= 5
print( a, " >= ", 5 , " = ", hasil)

print("-"*15, " <= ")
hasil = a <= b
print( a, " <= ", b , " = ", hasil)
hasil = a <= 2
print( a, " <= ", 2 , " = ", hasil)
hasil = a <= 5
print( a, " <= ", 5 , " = ", hasil)

print("-"*15, " == ")
hasil = 4 == 5
print("Hasil = ", hasil)
hasil = 5 == 5
print("Hasil = ", hasil)

print("-"*15, " != ")
hasil = 4 != 5
print("Hasil = ", hasil)
hasil = 5 != 5
print("Hasil = ", hasil)