
#import tkinter
#Traceback (most recent call last):
#  File "<pyshell#11>", line 1, in <module>
#    import tkinter
#ImportError: No module named tkinter

import sys, Tkinter
sys.modules['tkinter'] = Tkinter # put the module where python looks first for modules
#import tkinter # now works!

top =Tkinter.Tk()
quit =Tkinter.Button(top,text='hello',command=top.quit)
quit.pack()
Tkinter.mainloop()
