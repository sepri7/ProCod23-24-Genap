def tambahan( *angka ):
    hasil = 0
    for i in angka:
        hasil2  = hasil + i
        hasil = hasil2
    return hasil

def tambahan2( *angka ):
    hasil = 0
    for i in angka:
        hasil += i
    return hasil

def kalian( *angka ):
    hasil = 1
    for i in angka:
        hasil *= i
    return hasil