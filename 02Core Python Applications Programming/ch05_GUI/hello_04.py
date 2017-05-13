
#import tkinter
#Traceback (most recent call last):
#  File "<pyshell#11>", line 1, in <module>
#    import tkinter
#ImportError: No module named tkinter

import sys, Tkinter 
sys.modules['tkinter'] = Tkinter # put the module where python looks first for modules
#import tkinter # now works!
from Tkinter import *

def resize(ev=None):
    label.config(font='Helvetica -%d bold' % \
        scale.get())

top = Tk()
top.geometry('250x150')

label = Label(top, text='Hello World!',
    font='Helvetica -12 bold')
label.pack(fill=Y, expand=1)

scale = Scale(top, from_=10, to=40,
    orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=1)

quit = Button(top, text='QUIT',
    command=top.quit, activeforeground='white',
    activebackground='red')
quit.pack()

mainloop()

