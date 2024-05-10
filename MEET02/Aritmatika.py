'''
Aritmatika Python :
1. + ( Penjumlahan )
2. - ( Penguragan )
3. * ( Perkalian )
4. / ( Pembagian )
5. ** ( Pangkat )
6. % ( Modulus )
7. // ( Floor Division - Hasil bagi) 
'''

a = 4
b = 2

#Penjumlahan
Hasil = a + b
print( a, " + ", b, " = ", Hasil)
print( a, " + ", b, " = ", a + b)

#Pengurangan
Hasil = a - b
print( a, " - ", b, " = ", Hasil)

#Perkalian
Hasil = a * b
print( a, " * ", b, " = ", Hasil)

#Pembagian
Hasil = a / b
print( a, " / ", b, " = ", Hasil)

#Modulus
Hasil = a % b
print( a, " % ", b, " = ", Hasil)

#Floor Division
Hasil = a // b
print( a, " // ", b, " = ", Hasil)

#Eksponen
Hasil = a ** b
print( a, " ** ", b, " = ", Hasil)

'''
Prioritas Operasi  Aritmatika :
1. ()
2. **
3. * / % //
4. + -
'''
x = 4
y = 5
z = 6

Hasil = x * ( y - z )
print( " x * ( y - z ) = ", Hasil )

Hasil = ( x + y ) // ( z - x ) ** x
print( " ( x + y ) // ( z - x ) ** x = ", Hasil)

