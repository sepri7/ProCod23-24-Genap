import tkinter as tk
import ttkbootstrap as tb

class PersegiPanjang:
    def __init__(self, master ):
        self.master = master
        master.title("PACK")
        master.maxsize(900,  600) 
        self.kiriFramee  =  tb.Frame(master,  width=200,  height=  400)
        self.kiriFramee.pack(side='left',  fill='both',  padx=10,  pady=5,  expand=True)

        self.kananFramee  =  tb.Frame(master,  width=650,  height=400)
        self.kananFramee.pack(side='right',  fill='both',  padx=10,  pady=5,  expand=True)


        self.kiriFm = tb.Label(self.kiriFramee,  text="Mini Image", font=("arial", 20))
        self.kiriFm.pack(side='top',  padx=5,  pady=5)
        self.images  =  tb.PhotoImage(file=r"img/pj.png")
        self.miniImg  =  self.images.subsample(3,3)

        self.imgKiri = tb.Label(self.kiriFramee,  image=self.miniImg)
        self.imgKiri.pack(fill='both',  padx=5,  pady=5)

        self.imgKanan = tb.Label(self.kananFramee, image=self.images)
        self.imgKanan.pack(fill='both',  padx=5,  pady=5)

        self.menus  =  tb.Frame(self.kiriFramee,  width=400,  height=185)
        self.menus.pack(side='left',  fill='both',  padx=5,  pady=5)

        self.filter_menus  =  tb.Frame(self.kiriFramee,  width=90,  height=185)
        self.filter_menus.pack(side='left',  fill='both',  padx=5,  pady=5,  expand=True)


        self.panjang = tb.IntVar()
        self.lebar = tb.IntVar()

        LABELluas = tb.Label(self.menus,  text="LUAS KELILING", font=("arial", 10, 'bold'))
        LABELluas.pack(anchor='w',  padx=5,  pady=3,  ipadx=10)

        LABELkeliling = tb.Label(self.filter_menus,  text="Persegi Panjang", font=("arial", 10, 'bold'))
        LABELkeliling.pack(anchor='w',  padx=5,  pady=3,  ipadx=10)

        LABELpanjang = tb.Label(self.menus,  text="PANJANG", font=("arial", 10, 'italic'))
        LABELpanjang.pack(padx=5,  pady=5)
        FORMpanjang = tb.Entry(self.filter_menus,  textvariable= self.panjang)
        FORMpanjang.pack(padx=5,  pady=5)

        LABELlebar = tb.Label(self.menus,  text="LEBAR", font=("arial", 10, 'italic'))
        LABELlebar.pack(padx=5,  pady=5)
        FORMlebar = tb.Entry(self.filter_menus,  textvariable= self.lebar)
        FORMlebar.pack(padx=5,  pady=5)


        tb.Button(self.menus,  text="Cari Luas",  command=self.CariLuas).pack(anchor='e',  padx=5,  pady=30,  ipadx=10)
        tb.Button(self.filter_menus,  text="Cari Keliling",  command=self.CariKeliling).pack(anchor='w', padx=5,  pady=10)

    def CariLuas(self):
        self.imgKanan.config(image='', text=f"Hasil Luas dengan panjang ({self.panjang.get()}) dan lebar ({self.lebar.get()}) = {self.panjang.get() * self.lebar.get()}", font=("arial", 10), foreground="red")

    def CariKeliling(self):
        self.imgKanan.config(image='', text=f"Hasil Keliling dengan panjang ({self.panjang.get()}) dan lebar ({self.lebar.get()}) = {(self.panjang.get() * 2) + (self.lebar.get() * 2)}", font=("arial", 10), foreground="red")

if __name__ == "__main__":
    root  =  tb.Window(themename="superhero")
    PersegiPanjang(root)

    root.mainloop()