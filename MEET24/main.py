import fisika
import time
def batas():
    print("-"*15)

waktu_awal = time.time()

print( f"Massa Jenis = { fisika.MassaJenis.MassaJenis( 10, 2 ) }")
print( f"Massa = { fisika.MassaJenis.Massa( 10, 2 ) }")
print( f"Volume = { fisika.MassaJenis.Volume( 10, 2 ) }")

waktu_akhir = time.time()
print( f" Waktu yang dibutuhkan : { waktu_akhir - waktu_awal } ")

batas()
print( f"Usaha = { fisika.U( 12, 3 ) } ") 
print( f"Gaya = { fisika.G( 6, 2 ) } ") 
print( f"Jarak = { fisika.J( 9, 3 ) } ") 

batas()

print( f" Hasil Energi Potensial : { fisika.Ep( 4, 7, 4 ) } " )

batas()

diskon10 = fisika.JL( 10 )
diskon20 = fisika.JL( 20 )
print(f"Diskon 10% = { diskon10( 10000 ) } ")#1000
print(f"Diskon 20% = { diskon20( 10000 ) } ")#2000