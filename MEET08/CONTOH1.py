umur = int ( input("Masukkan umur \t: ") )

if umur < 17:
    status = input( "Menikah [ Y/T ] : " ).upper()
    if status == "Y":
        print( "Boleh ikut pemilu" )
    elif status == "T":
        print( "Tidak berHak" )
    else:
        print( "Pilihan salah !" )
elif umur >= 17:
    print( "Boleh ikut pemilu" )
else: 
    print( "Pilihan salah !" )

    