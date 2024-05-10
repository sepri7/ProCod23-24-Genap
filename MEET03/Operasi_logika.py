'''
Operasi Logika di python :
1. and  ( & )
2. or   ( | )
3. xor  ( ^ )
4. not
'''
print("-"*15,  " and ")
a = True
b = True
hasil = a and b
print( a, " and ", b, " = ", hasil)

a = False
b = True
hasil = a and b
print( a, " and ", b, " = ", hasil)

a = True
b = False
hasil = a and b
print( a, " and ", b, " = ", hasil)

a = False
b = False
hasil = a and b
print( a, " and ", b, " = ", hasil)


print("-"*15,  " or ")
a = True
b = True
hasil = a or b
print( a, " or ", b, " = ", hasil)

a = False
b = True
hasil = a or b
print( a, " or ", b, " = ", hasil)

a = True
b = False
hasil = a or b
print( a, " or ", b, " = ", hasil)

a = False
b = False
hasil = a or b
print( a, " or ", b, " = ", hasil)


print("-"*15,  " ^ / xor ")
a = True
b = True
hasil = a ^ b
print( a, " ^ ", b, " = ", hasil)

a = False
b = True
hasil = a ^ b
print( a, " ^ ", b, " = ", hasil)

a = True
b = False
hasil = a ^ b
print( a, " ^ ", b, " = ", hasil)

a = False
b = False
hasil = a ^ b
print( a, " ^ ", b, " = ", hasil)

print( "-"*15, " not ")
a = True
b = False
hasil = not a
print( "not, ", a, " = ", hasil )
hasil = not b
print( "not, ", b, " = ", hasil )