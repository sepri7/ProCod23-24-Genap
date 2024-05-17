# __main__
print(f"__name__ yang di main : { __name__ }")

import fungsi

def tambah( a, b ):
    return a + b

import module

if __name__ == "__main__":
    a = 6 
    b = 8
    print(f" result : { tambah( a,b )}")