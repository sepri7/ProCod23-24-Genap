from datetime import date as dt

print( f"<< \t\t UMUR \t\t >>")
print( "-"*25 )
print( "Masukkan tanggal, bulan, tahun ( Lahir )." )
print ( "\n" )
tanggal = int( input("Tanggal \t\t: ") )
bulan = int( input("Bulan \t\t\t: ") )
tahun = int( input("Tahun \t\t\t: ") )

tgl_lahir = dt( tahun, bulan, tanggal )
today = dt.today()
print( f"Tanggal lahir \t\t: {tgl_lahir} ( days : {tgl_lahir.day} ) " )
print( f"Tanggal Hari ini \t: {today} " )

selisih_tgl =  today - tgl_lahir
print( f" selisih tanggal : {selisih_tgl.days} " )

usia_tahun = selisih_tgl.days // 365
usia_sisa_bulan = (selisih_tgl.days % 365) // 30
print( f"Umur anda { usia_tahun } dan {usia_sisa_bulan} bulan" )