# Dictionary = Assosiasion Array
# key : value
#1
dataDict1 = {
    "nama" : "sepri", 
    "kelas" : "x", 
    "alamat" : "plg",
    "nama" : "budi"
}
print ( f"Dict 1 = { dataDict1 }")
#2
dataDict2 = dict(
    nama = "sepri", 
    kelas = "x", 
    alamat = "plg",
    mapel = [ "pjok","ips", "ipa" ]
    # nama = "budi" #tdk bisa
)
print ( f"Dict 2 = { dataDict2 }")
print( f"1.Nama = {  dataDict2["nama"] }" )
print( f"2.Nama = {  dataDict1.get( "name"," tidak ditemukan!" ) }" )
print( f"1,Mapel = { dataDict2["mapel"] }" )
print( f"2.Mapel = { dataDict2["mapel"][1] }" )
print( f"3.Mapel = { dataDict2.get( "mapel" )[-1] }" )

print("-"*15, "UPDATE & ADD")
dataDict2[ "nama" ] = "Indah"
print ( f"Dict 2 = { dataDict2 }")
dataDict2[ "agama" ] = "islam"
print ( f"Dict 2 UPDATED 1.= { dataDict2 }")
dataDict2.update( { "nama" : "Pinky" } )
print ( f"Dict 2 UPDATED 2.= { dataDict2 }")
dataDict2.update( dict( nama = "Kiki", agama ="Kristen" ) )
print ( f"Dict 2 UPDATED 3.= { dataDict2 }")
print("-"*15, "remove")
del dataDict2["nama"]
print ( f"Dict 2 DEL 1.= { dataDict2 }")
dataDict2.clear()
print ( f"Dict 2 DEL 2.= { dataDict2 }")
print("-"*15, "Empty Dict.")
data = dict( a = "v" )
print( data )
data.update( dict( a = "Abc", b = "xyz" ) )
print( data )
