num = int( (input( "Masukkan nilai 10 - 15 atau nilai 20 - 25 atau 35-40 : " )) )

while  not((num > 10 and num < 15) or (num > 20 and num < 25) or (num > 35 and num < 40))  :   
    print( " Salah..." )
    num = int( (input( "Masukkan nilai 10 - 15 atau nilai 20 - 25 atau 35-40 : " )) )
else:
    print( " Benar..." )