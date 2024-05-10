print("<< \t NOTA PENJUALAN - TOKO XYZ \t >>")
print( "_"*40 )
nama_barang = input( "Nama Barang\t: " )
harga_barang = int( input( "Harga Barang\t: " ) )
jumlah_beli = int( input( "Jumlah Beli\t: " ))

subTotal = harga_barang * jumlah_beli
print(f"SubTotal\t:Rp. {subTotal:>20} ")

diskon = 0.2 * subTotal
print(f"Diskon\t\t:Rp. {diskon:>20.0f} ")

total = subTotal - diskon
print(f"Total\t\t:Rp. {total:>20.0f} ")

