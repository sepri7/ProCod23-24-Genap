import tkinter as tk
import ttkbootstrap as tb

root = tb.Window( themename= "cosmo" )

class tester:
    def __init__(self, master): 
        self.master = master
        master.title("klik..")
        master.geometry("400x400")
        self.label1 = tb.Label(text="KLIK SAJA", font=("arial", 25,'bold'))
        self.label1.pack()
        self.kata1 = tb.Button(text="KATA 1", command=self.defKata1, bootstyle="success")
        self.kata1.pack()
        self.kata2 = tb.Button(text="KATA 2", command=self.defKata2, bootstyle="info")
        self.kata2.pack()
        self.DTY = tb.Button(text="EXIT", command=master.destroy, bootstyle="warning")
        self.DTY.pack()
        self.labelT1 = tb.Label(text="", font=("arial", 15,'bold'))
        self.labelT1.pack()
    def defKata1( self ):
        self.labelT1.config( text="KATA SATU" )
    def defKata2( self ):
        self.labelT1.config( text="KATA DUA" )
if __name__== "__main__":
    tester( root )
    root.mainloop()