import statistics
def Sik( **data ):
    h_mean = statistics.mean( data[ "nilai" ] )
    h_median = statistics.median ( data[ "nilai" ] )
    h_modus = statistics. multimode( data[ "nilai" ] )
    return h_mean, h_median, h_modus

datas = [ 60, 70, 60, 60, 80, 90, 100 ]

hasil_mean, hasil_median, hasil_modus = Sik( nilai = datas )

print(datas)
print( f" mean = { hasil_mean }")
print( f" median = { hasil_median }")
print( f" modus = { hasil_modus }")