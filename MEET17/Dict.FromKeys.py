#FromKeys : Dict
data = dict.fromkeys( range(5), "oke" )
print ( f"data = {data}")

print( "-"*20)
data = {
    "siswa" : "",
    "kelas" : "",
    "jurusan" : ""
}
datas = dict.fromkeys( data.keys() )
data["siswa"] = input("Siswa = ")
data["kelas"] = input("kelas = ")
data["jurusan"] = input("jurusan = ")
NewData = { "siswa01" : data }
print ( f"NewData = {NewData}")

print( "-"*20)
import random
import string
keys_1 = random.randint( 1, 10 )
print ( f"Keys_1 = {keys_1}" )
keys_2 = random.choice( "ABCDEF" )
print ( f"keys_2 = {keys_2}" )
print( f" A - Z =  { string.ascii_uppercase }" )
keyFinal = "".join(random.choice( string.ascii_uppercase ) for i in range( 3 ) )
print ( f" KeyFinal = { keyFinal } ")

print( "-"*20)
data = ( "name", "kelas", "eMail" )
datas = dict.fromkeys( data )
datas["name"] = input( "Name = " )
datas["kelas"] = input( "kelas = " )
datas["eMail"] = input( "eMail = " )
NewData = { keyFinal : data }
print( f"NewData Final = { NewData }")

import os
os.system( "cls" ) # win
# os.system( "clear" ) # mac
print ( f' name\t kelas\t eMail ' )