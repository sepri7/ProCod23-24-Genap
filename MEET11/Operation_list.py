#                  0/ -3         1/ -2         2/ -1 
data_list1 = [ "Ignatius", "Global", "School"  ]
print( f"data_list1 Ke-0 : { data_list1[ 0 ] } " )
print( f"data_list1 Ke-1 : { data_list1[ 1 ] } " )
print( f"data_list1 Ke-2 : { data_list1[ 2 ] } " )
print( f"data_list1 -2 : { data_list1[ -2 ] } " )

print("-"*10, "Bagian/irisan -item list")
data_list2 = [ 1, 2, 3, 4, "a", "b", True ]
print( f"Data list2 [0:3] : { data_list2[ 0:3 ] }" )
print( f"Data list2 [-2:1] : { data_list2[ -2:1 ] }" )
print( f"Data list2 [1: ] : { data_list2[ 1: ] }" )
print( f"Data list2 [ :-2 ] : { data_list2[ :-2 ] }" )

print("-"*10, "Join -list")
data1 = [ 1, 2, 3, 4 ]
data2 = [ "a","b","c" ]
print ( f" data1 + data2 = { data1 + data2 }" )
data1.extend( data2 )
print( f"data1 = {data1} " )

print("-"*10, "Len-")
print( f"Jumlah item data1 = { len( data1 ) } ")

print("-"*10, "Repetition")
data3 = [ "x","y", "z" ] * 3
print( f" data3  = { data3 } ")

print("-"*10, "Membership")
if "x" in data3:
    print ( "True" )
else:
    print ( "False" )

print("-"*10, "Iterasi")
for i in data_list1:
    print ( f"data : { i }" )

print("-"*10, "ADD -Item")
data_list1.insert( 0, "SMA"  )
print ( f" data_list1 - insert : { data_list1 } " )
data_list1.append( "Keren" )
print ( f" data_list1 - append : { data_list1 } " )

print("-"*10, "UPDATE -Item")
data_list1[ -1 ] = "oke"
print ( f" data_list1 - UPDATE : { data_list1 } " )

print("-"*10, "DELETE -Item")
data_list1.pop()
print ( f" data_list1 - DELETE.pop : { data_list1 } " )
data_list1.remove( "SMA" )
print( f"data_list1- DELETE.remove : { data_list1 } " )
del data_list1[ -1 ]
print( f"data_list1- DELETE.del : { data_list1 } " )

print("-"*10, "INDEX -Item") 
data5 = [ 1, 1, 6, 2, 3 ]
print ( f" data5 : 2 = { data5.index( 2 ) } " )

print("-"*10, "Count -Item")
print( f" jumlah item(1) di data5 = { data5.count( 1 ) }")

print("-"*10, "max-min -Item")
print( f"max data5 = { max(data5) } min = { min(data5)} ")

print("-"*10, "Sorting -Item")
data5.sort()
print( f" sort= { data5 } " )
data5.reverse()
print( f" reverse= { data5 } " )



