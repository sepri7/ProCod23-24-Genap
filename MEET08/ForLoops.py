#FOR LOOP :  range()
for x in range(5):
    print( f"LOOP range (5) : {x}" )
print( "-"*15 )
for z in range( 1, 11 ):
    print( f"LOOP range ( 1, 11 ) : {z}" )
print( "-"*15 )
for i in range ( 1, 11, 2 ):
    print( f"LOOP range ( 1, 11, 2 ) : {i}" )

print( "-"*15 )
for i in ("Ignatius"):
    print ( f"For i in data : {i}" )

print( "-"*15 )
for z in range (1,5):
    print( f" range(1,5) - false( selesai !) ")
else:
    print( "Selesai !" )

print( "-"*15 )
data = [ 1, 3, 2, 5 ]
for i in data:
    print( f" for i in data : {i}" )

print( "-"*15 )
data_hewan = [ "ayam","kelinci", "kucing" ]
for i in data_hewan:
    print( f" Saya memiliki hewan peliharaan {data_hewan}" )
