#Lambda : Statement (custom) Function yang tidak memiliki def

def kuadrat( num ):
    return num ** 2
print( f"Result Kuadrat : { kuadrat(4) }" )
#syntax :
# output = lambda variabel_parameter : expression
ResultKuadrat = lambda abc : abc ** 2
print( f"Result Kuadrat lambda : { ResultKuadrat(4) }" )

def pangkat ( angka, pangkat ):
    return angka ** pangkat
print( f"Result pangkat : { pangkat( 4,3 ) }" )

ResultPangkat = lambda a, b : a ** b

print( f"hasil 5 pangkat 2 { ResultPangkat( 5, 2 ) } ")

def batas():
    print(  "-"*15  )

batas()
dataAlf = [ "bbb", "cc", "d", "zzzz", "aa" ]
dataAlf.sort()
print( f"1. data sorted : { dataAlf }  ")

def pnjData( data ):
    return len( data )

dataAlf.sort( key = pnjData )
print( f"2. data sorted func : { dataAlf }  ")

dataAlf = [ "bbb", "cc", "d", "zzzz", "aa" ]
dataAlf.sort( key = lambda data: len(data)  )
print( f"3. data sorted lambda : { dataAlf }  ")

batas()
datas = [ 1, 2, 4, 8, 10, 12, 15, 18, 20, 21 ]
def kurangDari9 ( data ):
    return data < 9

datasKurang9 = list( filter( kurangDari9, datas ) )
print( f"Data Kurang dari 9 = { datasKurang9 }")

lamDatas9 = list( filter( lambda data : data < 9, datas ))
print( f"Data Kurang dari 9 Lambda = { lamDatas9 }")

batas()
# currying = Teknik berguna untuk membuat multi argument dan menjadikan pecahan fungsi lebih banyak
def pangkat( num, n ):
    return num ** n 
print( f"5 pangkat 2 { pangkat( 5,2 ) } " )
print( f"9 pangkat 2 { pangkat( 9,2 ) } " )

def pangkatC ( n ):
    return lambda angka : angka ** n

pangkat2 = pangkatC( 2 )
print( f"10 pangkat 2 { pangkat2( 10 ) } " )
pangkat5 = pangkatC( 5 )
print( f"4 pangkat 5 { pangkat5( 4 ) } " )
