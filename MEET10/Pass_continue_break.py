#pass
print( "-"*15, " - Pass" )
for i in range( 5 ):
    print( f"{ i }" )
    if i == 3 :
        pass   # dummy
print( "-"*20 )
for i in range ( 7 ):
    if i == 5:
        pass
    else:
        print( f"{ i }" )
print( "-"*20 )
# try:
#     a = int ( input ( "a = "))
#     b = int ( input ( "b = "))
#     print ( f"{a} + {b} = {a+b}")
# except:
#     pass

print( "-"*15, " - Break ")
for i in range ( 10 ):
    if i == 3:
        break
    else:
        print(  f"{i}" )

print( "-"*15, " - Continue ")
for i in range ( 10 ):
    print(  f"{i}" )
    if i == 3:
        continue
    print("oke")
print( "done.. ")
