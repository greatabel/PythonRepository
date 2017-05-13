
#import tkinter
#Traceback (most recent call last):
#  File "<pyshell#11>", line 1, in <module>
#    import tkinter
#ImportError: No module named tkinter

import sys, Tkinter
sys.modules['tkinter'] = Tkinter # put the module where python looks first for modules
#import tkinter # now works!

top =Tkinter.Tk()

hello =Tkinter.Label(top,text='hello world!')
hello.pack()

quit=Tkinter.Button(top,text='Quit it',command=top.quit,bg='white',fg='red')
quit.pack(fill=Tkinter.X,expand=2)

Tkinter.mainloop()
