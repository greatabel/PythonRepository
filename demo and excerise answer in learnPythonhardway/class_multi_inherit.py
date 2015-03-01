from class_inherit import student

class speaker():
 topic=''
 name=''
 def __init__(self,n,t):
   self.name=n
   self.topic=t
 def speak(self):
   print "I am %s,I am a speaker! my topic is %s" %(self.name,self.topic)

class sample(speaker,student):
 a=''
 def __init__(self,n,a,w,g,t):
      print '-^-'*20
      student.__init__(self,n,a,w,g)
      speaker.__init__(self,n,t)
  
  
  
s = sample('ken',99,60,3,"c# and python")  
s.speak()  
 
