print("*")
print("**")
print("***")
print("****")
print("*****")
print("******")

print ( "- for"*10 )
for i in range(10):
    print ( "+"* i)

print ( "- while"*10 )
i = 0
while i < 10:
    i += 1
    print ( f"{i}"* i)

print ( "ganjil- ( Left )"*10)
i = 0
while True:
    if i == 20:
        break
    elif i % 2 :
        print( f"+" * i )
    i += 1

print ( ">"*10)
i = 0
count = 20
space = 20
while True:
    if i == count:
        break
    elif i % 2 :
        print(f" "* space, "+"*i)
    space -= 1
    i += 1

print ( "^"*10)
i = 0
count = 20
space = int(1/2 * count)
while True:
    if i == count:
        break
    elif i % 2 :
        print(f" "* space, "+"*i)
        space -= 1
    i += 1

print ( "fString - segitiga" )
print ( "-"*10, "1. < Left Sided")
for i in range(10):
    x = "+" * i
    print(f"{x:<10}")
print ( "-"*10, "2. >")
for i in range(10):
    x = "+"*i
    print(f"{x:>10}")
print ( "-"*10, "3. ^")
for i in range(10):
    x = " +"*i
    print(f"{x:^20}")





