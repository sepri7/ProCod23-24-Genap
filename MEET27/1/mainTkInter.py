import tkinter as tk
from tkinter import ttk as tema
from tkinter.messagebox import showinfo
import ttkbootstrap as tb
# root = tk.Tk()
# https://ttkbootstrap.readthedocs.io/en/latest/themes/
root = tb.Window( themename= "vapor" )

nama = tk.StringVar()
kelas = tk.IntVar()
jk = tk.StringVar()
ba = tk.StringVar()
setuju = tk.BooleanVar()

def kirim():
    if setuju.get() == True:
        stj = "bersedia"
    else:
        stj = "tidak bersedia"

    h = f"hallo nama saya { nama.get()} jenis kelamin {jk.get()} di kelas {kelas.get() } dan saya { stj } mengerjakan project bahasa asing  { ba.get() } "
    showinfo(title="BIO", message = h)   

root.title("TESTER..")
root.geometry( "400x500" )
root.resizable(False, False)
root.config(bg="gray")

frame = tema.Frame(root)
frame.pack(padx=10, pady=10, fill="x", expand=True )
# pack     grid     place
labelNama = tema.Label(frame, text="NAMA :")
labelNama.pack(padx=10, fill="x", expand=True )
formNama = tema.Entry(frame, textvariable= nama )
formNama.pack(padx=10, fill="x", expand=True )

labelkelas = tema.Label(frame, text="KELAS :")
labelkelas.pack(padx=10, fill="x", expand=True )
formkelas = tema.Entry(frame, textvariable= kelas )
formkelas.pack(padx=10, fill="x", expand=True )

labelJK = tema.Label(frame, text="Jenis Kelamin :", font=("arial",12, 'bold'))
labelJK.pack(padx=10, fill="x", expand=True )
formJK = tema.Combobox(frame, textvariable= jk, values=["laki-laki","perempuan"])
formJK.pack(padx=10, fill="x", expand=True )
formJK.current(0)

labelba = tema.Label(frame, text="ba :")
labelba.pack(padx=10, fill="x", expand=True )
ba1 = tema.Radiobutton(frame, value="dkv", text="dkv", variable=ba)
ba1.pack(padx=10, fill="x", expand=True )
ba2 = tema.Radiobutton(frame, value="coding", text="coding", variable=ba)
ba2.pack(padx=10, fill="x", expand=True )

stj = tema.Checkbutton(frame, variable=setuju, text="Saya setuju mengerjakan Project Akhir ..", onvalue=1, offvalue=0)
stj.pack(padx=10, fill="x", expand=True )

BTN = tema.Button( frame, text="KIRIM", command=kirim )
BTN.pack(padx=10, fill="x", expand=True )
root.mainloop()