#list
dataList = [ 1, 2, 3, 4, 1 ]
dataTuple = ( "a", "b", "c", "b" )
dataSet = { "x", "y", 9, 9 } # set = himpunan
print( f"List = { dataList }" )
print( f"Tuple = { dataTuple }" )
print( f"Set = { dataSet }" )
print( "-"* 15)
print ( f"Data list ke 0 = { dataList[ 0 ] }")
print ( f"Data Tuple ke 0 = { dataTuple[ 0 ] }")
# print ( f"Data Set ke 0 = { dataSet[ 0 ] }") #tdk bisa
print( "-"* 15)
dataList.insert( 0, "awal" )
print( f"List = { dataList }" )
dataSet.add( "igs" )
print( f"Set = { dataSet }" )
# dataTuple.add( "oke" ) # tdk bisa
print( "-"* 15) # remove
dataList.remove("awal")
print( f"List = { dataList }" )
dataSet.remove( "igs" )
print( f"Set = { dataSet }" )
print( "-"* 15) # update
dataList[ 0 ] = "abc"


