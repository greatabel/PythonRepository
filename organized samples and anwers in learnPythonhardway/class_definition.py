class people:
 #basic property
 name=''
 age=0

 #define private property
 __weight = 0 

 def __init__(self,iname,iage,iweight):
					self.name=iname
					self.age=iage
					self.__weight=iweight

 def speak(self):
					print "%s is speaking: I am %d years old" %(self.name,self.age)  
 def abel_testreturn(self):
					return self.name,self.age 

#p=people('abel',28,160)
#p.speak()
#myname,myage=p.abel_testreturn()
#print myname,myage
