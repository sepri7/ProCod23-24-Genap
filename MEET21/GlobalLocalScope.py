varGlobal = "Globallllll"

for i in range( 1,3 ):
    print( f" {i}. { varGlobal }" )

if True:
    print( f" varGlobal if = { varGlobal } " )

def fungsi1():
    varLocal = "Locallll"
    print( f" varLocal = { varLocal }")
fungsi1()

# print( f"outside, varLocal : { varLocal} " )

nilai = 0
angka = 100
def fungsi2():
    nilai = 12 #local
    global angka 
    angka = 50

print ( f"1. nilai = { nilai } , angka = { angka }")
fungsi2()
print ( f"2. nilai = { nilai }, angka = { angka }")

kelas = "x"
jml = 40
def fungsi3( newKelas, newJml ):
    global kelas
    global jml
    kelas = newKelas
    jml = newJml
print( f"1. kelas = { kelas } dan jumlah = { jml }")
fungsi3( "xi", 35)
print( f"2. kelas = { kelas } dan jumlah = { jml }")
