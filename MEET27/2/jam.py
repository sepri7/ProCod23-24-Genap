import ttkbootstrap as tb
from time import strftime
root = tb.Window( themename="superhero" )

def jam():
    label.config(text = strftime( " %H:%M:%S %p " ))
    label.after( 1000, jam )

label = tb.Label( font=("arial", 40, 'bold'), foreground="green" )
label.pack()
jam()
root.mainloop()