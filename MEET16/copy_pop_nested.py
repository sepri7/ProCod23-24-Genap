dataDict = {
    "plm" : "Palembang",
    "em" : "Muara Enim",
    "pr" : "Prabumulih",
    "llg" : "Lubuklinggau"
}
data_copy = dataDict
dataDict["plm"] = "PALEMBANG"
print( f"DataDict = { dataDict }")
print( f"data_copy = { data_copy }")
data_copy2 = dataDict.copy()
dataDict["llg"] = "LUBUKLINGGAU"
print( f"DataDict = { dataDict }")
print( f"data_copy2 = { data_copy2 }")

print("-"*15, "POP")
data_pop = dataDict.pop( "plm" )
print( f"Data Pop = { data_pop }")
print( f"dataDict = { dataDict }")

print("-"*15, "PopItem")
data_popItem = dataDict.popitem() # data menjadi tuple
print( f"data_popItem = { data_popItem }")
print( f"dataDict = { dataDict }")

print("-"*15, "NESTED DICTIONARY")
dataNest = {
    "mobil1" : {
        "merk" : "rush",
        "color" : "red",
        "year" : 2022
    },
    "mobil2" : {
        "merk" : "avanza",
        "color" : "putih",
        "year" : 2020
    }
}
print( f"Merk Mobil1 = { dataNest[ "mobil1" ]["merk"] }")
print( f"Merk Mobil2 = { dataNest.get( "mobil2" ).get( "merk" ) }")
print( f"color Mobil2 = { dataNest['mobil2'].get( "color" ) }")

print("-"*15, "DEEPCOPY")
from copy import deepcopy
dataNest_copy = deepcopy( dataNest )
dataNest["mobil2"]["merk"] = "Xenia"
print( f" dataNest= { dataNest } ")
print( f" dataNest_copy= { dataNest_copy } ")

print("-"*15, "1.COMPREHENSION")
data = "ABC"
data1 = { i for i in data } # ini jadi data set
print( f" data1 = { data1 }, type  = { type ( data1 ) } ")
data1 = { i : i*3 for i in data }
print( f" data1 = { data1 }, type  = { type ( data1 ) } ")
print("-"*15, "2.COMPREHENSION")
data1 = [ "x" , "y", "z" ]
data2 = [ 7 , 8, 9 ]
dataFinal = { k : v**3 for k,v in zip( data1, data2 ) }
print ( f"Data Final = { dataFinal }")

print("-"*15, "3.COMPREHENSION")
data = { "ana" : 85, "ibnu" : 90, "indah" : 100, "bunga" : 86 }
data = { k:v for k,v in data.items() if v > 86 }
print( f"Data = {data}" )