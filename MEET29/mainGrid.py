import tkinter as tk
import ttkbootstrap as tb

class PersegiPanjang:
    def __init__(self, master ):
        self.master = master
        master.title("GRID")
        master.maxsize(900,  600) 
        self.kiriFramee  =  tb.Frame(master,  width=200,  height=  400)
        self.kiriFramee.grid(row=0,  column=0,  padx=10,  pady=5)

        self.kananFramee  =  tb.Frame(master,  width=650,  height=400)
        self.kananFramee.grid(row=0,  column=1,  padx=10,  pady=5)


        self.kiriFm = tb.Label(self.kiriFramee,  text="Mini Image", font=("arial", 20))
        self.kiriFm.grid(row=0,  column=0,  padx=5,  pady=5)
        self.images  =  tb.PhotoImage(file=r"img/pj.png")
        self.miniImg  =  self.images.subsample(3,3)

        self.imgKiri = tb.Label(self.kiriFramee,  image=self.miniImg)
        self.imgKiri.grid(row=1,  column=0,  padx=5,  pady=5)

        self.imgKanan = tb.Label(self.kananFramee, image=self.images)
        self.imgKanan.grid(row=0,  column=0,  padx=5,  pady=5)

        self.menus  =  tb.Frame(self.kiriFramee,  width=180,  height=185)
        self.menus.grid(row=2,  column=0,  padx=5,  pady=5)


        self.panjang = tb.IntVar()
        self.lebar = tb.IntVar()

        LABELluas = tb.Label(self.menus,  text="LUAS KELILING", font=("arial", 10, 'bold'))
        LABELluas.grid(row=0,  column=0,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s')

        LABELkeliling = tb.Label(self.menus,  text="Persegi Panjang", font=("arial", 10, 'bold'))
        LABELkeliling.grid(row=0,  column=1,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s')

        LABELpanjang = tb.Label(self.menus,  text="PANJANG", font=("arial", 10, 'italic'))
        LABELpanjang.grid(row=1,  column=0,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s')
        FORMpanjang = tb.Entry(self.menus,  textvariable= self.panjang)
        FORMpanjang.grid(row=1,  column=1,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s')

        LABELlebar = tb.Label(self.menus,  text="LEBAR", font=("arial", 10, 'italic'))
        LABELlebar.grid(row=2,  column=0,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s')
        FORMlebar = tb.Entry(self.menus,  textvariable= self.lebar)
        FORMlebar.grid(row=2,  column=1,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s')


        tb.Button(self.menus,  text="Cari Luas",  command=self.CariLuas).grid(row=4,  column=0,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s')
        tb.Button(self.menus,  text="Cari Keliling",  command=self.CariKeliling).grid(row=4,  column=1,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s')

    def CariLuas(self):
        self.imgKanan.config(image='', text=f"Hasil Luas dengan panjang ({self.panjang.get()}) dan lebar ({self.lebar.get()}) = {self.panjang.get() * self.lebar.get()}", font=("arial", 10), foreground="red")

    def CariKeliling(self):
        self.imgKanan.config(image='', text=f"Hasil Keliling dengan panjang ({self.panjang.get()}) dan lebar ({self.lebar.get()}) = {(self.panjang.get() * 2) + (self.lebar.get() * 2)}", font=("arial", 10), foreground="red")

if __name__ == "__main__":
    root  =  tb.Window(themename="superhero")
    PersegiPanjang(root)

    root.mainloop()