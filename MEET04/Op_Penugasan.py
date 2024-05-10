#Operator Assignment :
# 1. =
# 2. +=
# 3. -=
# 4. *=
# 5. /=
# 6. %=
# 7. //=
# 8. **=

print( "-"*15, " += " )
a = 10
a += 3 # a = a + 3
print( "a += ", a)

a = 10
a -= 3 # a = a - 3
print( "a -= ", a)

a = 10
a *= 3 # a = a * 3
print( "a *= ", a)

a = 10
a /= 3 # a = a / 3
print( "a /= ", a)

a = 10
a %= 3 # a = a % 3
print( "a %= ", a)

a = 10
a //= 3 # a = a // 3
print( "a //= ", a)

a = 10
b = 3
a **= b # a = a ** b
print( "a = ", a)

# Operator Assignment ( Logika ) - Bitwise
#1. &
#2. |
#3. ^

x = True
x &= False
print( "True &= False = ", x)

x = True
x &= True
print( "True &= True = ", x)

x = True
x |= False
print( "True |= False = ", x)

x = True
x |= True
print( "True |= True = ", x)

x = True
x ^= False # x = True ^ False
print( "True ^= False = ", x)

x = True
x ^= True # x = True ^True
print( "True ^= True = ", x)