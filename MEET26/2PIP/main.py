#NOTED:
#PIP is a package manager for Python packages
#Check PIP VERSION      :   pip --version
#contoh, Install PIP    :   pip numpy
#List Packages          :   pip list
   
import numpy as npy
data = [ 5, 6, 7, 9 ]
# print( f"data**2 = { data**2 } " )# tidak bisa

datas = [ i**2 for i in data ]
print( f"datas**2 = { datas } " )
dataVektor = npy.array( [8,7,6,2] )
print( f"dataVektor**2 = { dataVektor**2 } " )
dataVektor_2 = npy.array( [ (1,4), (6, 7) ] )
print( f"dataVektor_2**2 =\n { dataVektor_2**2 } " )
dataZ = npy.zeros( [(2), (2)] )
dataO = npy.ones( [(2), (2)] )
print(dataZ)
print ( dataVektor_2 + dataZ + dataO )