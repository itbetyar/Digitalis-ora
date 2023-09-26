# IT Betyar 2023 | Digitalis ora

# konyvtarak es ido importalasa
from tkinter import Tk 
from tkinter import Label 
import time

# az ablak letrehozasa
master = Tk() 
master.configure(bg="#1B1C24") # sotet hatter
master.title("Digitális óra")  # ablak cimke
master.geometry("550x120")


def get_time():    # ido bekerese funkcio
     # timevar-ba irjuk az idot stringben
     timeVar = time.strftime("%I:%M:%S %p")   
     # a clock label-t configuraljuk, a text reszebe
     # irjuk a timeVar erteket
     clock.config(text=timeVar)    
     clock.after(200,get_time) # 0.2 sec-enkent frissitunk

# az ora cimke/szoveg
clock = Label(master, font=("Calibri",60),bg="#1B1C24",fg="white") 
clock.pack(pady=5)

# a get_time funkcio meghivasa
get_time()

master.mainloop() 
