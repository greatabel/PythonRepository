from class_definition import people

class student(people):
  grade=''
  def __init__(self,n,a,w,g):
    people.__init__(self,n,a,w)
    self.grade=g
  def speak(self):
    print "%s is speaking:I'm %d years old and in grade %d" %(self.name,self.age,self.grade)  
  
  
  
#s = student('ken',20,60,3)  
#s.speak()  
 
