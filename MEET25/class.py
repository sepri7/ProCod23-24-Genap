#class in python
class Mobil():
    # var class
    JmlMobil = 0
    def __init__ ( self, merk, warna, tahun ):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun
        Mobil.JmlMobil += 1
    def TampilMobil(self):
        print(f"Mobilku {self.merk}")
    def ubahWarna(self, warnaBaru):
        self.warna = warnaBaru

print( f"sebelum. Jumlah Data Mobil = {Mobil.JmlMobil}")
MobilAvanza = Mobil("Avanza", "Merah", 2024)
MobilXenia = Mobil("Xenia", "Putih", 2022)
MobilRush = Mobil("Rush", "Kuning", 2023)
print( f"Jumlah Data Mobil = {Mobil.JmlMobil}")
MobilAvanza.TampilMobil()
MobilXenia.TampilMobil()
print(f"Mobilku {MobilRush.merk} warna {MobilRush.warna} pada tahun {MobilRush.tahun}")
MobilAvanza.ubahWarna("hijau")
print(f"Warna baru {MobilAvanza.merk} = {MobilAvanza.warna}") 
