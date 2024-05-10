#Type Hints :
# berguna untuk membuat Default Tipe data pada variabel parameter Function.
def tambahan_100( z ):
    return 100 + z
print( f"Hasil : { tambahan_100( 50 ) }")
# print( f"Hasil : { tambahan_100( "kosong" ) }")
def tambahan_50( x : int ):
    return 50 + x
print( f"Hasil : { tambahan_50( 20 ) }")

# args ( Argument ) - KwArgs ( Keyword Argument ):
#- Magic variabel.
#- Result Parameter Argument : tuple
#- Result Parameter KwArgs : Dictionary
#- Menggunakan nya waktu jumlah parameter tidak menentu ( non Fixed)
def batas():
    print("_"*20)
batas()
def yourName( name1,name2,name3 ):
    return name1,name2,name3
print ( f" name : {yourName( "ana", "lola", "ina" )}" )
# print ( f" name : {yourName( "ana", "lola", "ina","dede" )}" ) # tdk bisa
batas()
def Bio( *data ):
    return data
print ( f" name args : {Bio( "ana", "lola", "ina","dede" )}" ) 
batas()
def plusPlus( *data ):
    hasil = 0
    for i in data:
        hasil += i
    return hasil
def plus2 ( *data ):
    hasil = sum( *data )
    return hasil
print ( f" SUM : {plusPlus( 2, 4, 7, 9, 5 )}" ) 
print ( f" SUM-plus2 : {plus2( [2, 4, 7, 9, 5] )}" ) 
batas()
#KwArgs
def mapel( **data ):
    return data
print( f"Mapel : { mapel( mapel1 = "b.ind", mapel2 = "inf", mapel3 = "biologi" ) }")
def materi( **data ):
    for key, value in data.items():
        print( f" { key }. \t{ value }" )

materi( a = "List", b = "set", c = "tuple" )
batas()
def MixFinal( parameter1, parameter2, *args, **kwArgs ):
    return parameter1, parameter2, args, kwArgs

parameter1, parameter2, args, kwArgs = MixFinal( 1,2,3,4,5,6, a = "abc" )
print ( f" Parameter 1 : {parameter1}")
print ( f" Parameter 2 : {parameter2}")
print ( f" args : {args}")
print ( f" kwArgs : {kwArgs}")
