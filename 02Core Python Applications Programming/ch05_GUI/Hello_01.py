#http://stackoverflow.com/questions/4783810/install-tkinter-for-python

#import tkinter
#Traceback (most recent call last):
#  File "<pyshell#11>", line 1, in <module>
#    import tkinter
#ImportError: No module named tkinter

import sys, Tkinter
sys.modules['tkinter'] = Tkinter # put the module where python looks first for modules
#import tkinter # now works!

top=Tkinter.Tk()
label=Tkinter.Label(top,text="hello world from abel")
label.pack()
Tkinter.mainloop()
