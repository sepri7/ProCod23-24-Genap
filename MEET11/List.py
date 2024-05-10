# list :
# 1. number
# 2. karakter / string
# 3. bool
list_num = [ 1, 2, 3, 4, 10  ]
print( f"Data List angka : { list_num }")
list_str = [ "q", "w", "e", "r", "t", "y" ]
print( f"Data List str : { list_str }")
list_bool = [ True, False, False, True ]
print( f"Data List bool : { list_bool }")
list_mix = [
    1,
    2,
    True,
    "abc",
]
print( f"Data List mix : { list_mix }")
print( "-"*10, " List : LOOP-For" )
data_loop = [ i for i in range( 1, 10, 2 ) ]
print( f"Data List (loop) : { data_loop }")
data1 = [ i for i in range ( 1,10 ) if i % 2 == 1 ]
data2 = [ i for i in range ( 1,10 ) if i != 5 ]
print( f"Data1 data2 : { data1 } | { data2}")
