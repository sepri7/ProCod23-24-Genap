#import : berguna untuk melampirkan file eksternal .py

import tester
import bio

import data

# variabel dalam data ada dalam sebuah namespace
print ( f" nama di data = { data.nama } " )
print ( f" kelas di data = { data.kelas } " )

import tambah
print( f" 1 + 2 = { tambah.plus( 1,2 ) }")