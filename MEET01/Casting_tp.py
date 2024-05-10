# # Tipe data primary di python,
# # 1. integer ( int ) : angka (bulat)
# 2. float (float) : angka (pecahan)
# 3. string (str) :karakter / huruf
# 4. boolean ( bool ) : logika ( true/False)

print("-"*15, "DATA INTEGER")
data_int = -9
print("data = ", data_int, " tipe data = ",type(data_int) )

data_float = float(data_int)
print("data = ", data_float, " tipe data = ",type(data_float) )
data_str = str(data_int)
print("data = ", data_str, " tipe data = ",type(data_str) )
data_bool = bool(data_int) # jika value = 0 maka false, selain value =0 maka true
print("data = ", data_bool, " tipe data = ",type(data_bool) )

print("-"*15, "DATA FLOAT")
data_float = 0
print("data = ", data_float, " tipe data = ",type(data_float) )

data_int = int(data_float)
print("data = ", data_int, " tipe data = ",type(data_int) )
data_str = str(data_float)
print("data = ", data_str, " tipe data = ",type(data_str) )
data_bool = bool(data_float) # jika value = 0 maka false, selain value =0 maka true
print("data = ", data_bool, " tipe data = ",type(data_bool) )


print("-"*15, "DATA STRING")
data_string = "67"
print("data = ", data_string, " tipe data = ",type(data_string) )

data_int = int(data_string) # jika value data string, bukan angka maka casting tdk bisa
print("data = ", data_int, " tipe data = ",type(data_int) )
data_float = float(data_string)# jika value data string, bukan angka maka casting tdk bisa
print("data = ", data_float, " tipe data = ",type(data_float) )
data_bool = bool(data_string) # jika value = 0 maka false, selain value =0 maka true
print("data = ", data_bool, " tipe data = ",type(data_bool) )


print("-"*15, "DATA BOOL")
data_bool = False
print("data = ", data_bool, " tipe data = ",type(data_bool) )

data_int = int(data_bool) 
print("data = ", data_int, " tipe data = ",type(data_int) )
data_float = float(data_bool)
print("data = ", data_float, " tipe data = ",type(data_float) )
data_str = str(data_bool)
print("data = ", data_str, " tipe data = ",type(data_str) )