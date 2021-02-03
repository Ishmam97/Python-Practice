import random as rnd
class Director:
   __builder = None
   
   def setBuilder(self, builder):
      self.__builder = builder
   
   def getEmployee(self):
      employee = Employee()
      
      frontEndSkills = self.__builder.frontEndSkills()
      employee.setfrontEndSkills(frontEndSkills)
      
      
      backend = self.__builder.getbackend()
      employee.setbackend(backend)
            
      frameworks = self.__builder.getframeworks()
      employee.setFrameworks(frameworks)
      
      return employee

# The whole product
class Employee:
   def __init__(self):
      self.__frameworkss = list()
      self.__backend = None
      self.__frontEndSkills = None

   def setfrontEndSkills(self, frontEndSkills):
      self.__frontEndSkills = frontEndSkills

   def setFrameworks(self, frameworks):
      self.__frameworkss.append(frameworks)

   def setbackend(self, backend):
      self.__backend = backend

   def specification(self):
      print( "frontend skills: %s /10" % self.__frontEndSkills.feSkills)
      print( "backend skills: %d /10" % self.__backend.beSkills)
      print( "no. frameworks: %d" % self.__frameworkss[0].frno)

class Builder:
      def getframeworks(self): pass
      def getbackend(self): pass
      def frontEndSkills(self): pass

class FrontendDeveloper(Builder):
   
   def getframeworks(self):
      frameworks = Frameworks()
      frameworks.frno = rnd.randint(1 , 5)
      return frameworks
   
   def getbackend(self):
      backend = Backend()
      backend.beSkills = rnd.randint(1 , 5)
      return backend
   
   def frontEndSkills(self):
      frontEndSkills = FrontEndSkills()
      frontEndSkills.feSkills = rnd.randint(5 , 10)
      return frontEndSkills

class BackEndDeveloper(Builder):
   
   def getframeworks(self):
      frameworks = Frameworks()
      frameworks.frno = rnd.randint(1 , 5)
      return frameworks
   
   def getbackend(self):
      backend = Backend()
      backend.beSkills = rnd.randint(5 , 10)
      return backend
   
   def frontEndSkills(self):
      frontEndSkills = FrontEndSkills()
      frontEndSkills.feSkills =  rnd.randint(1 , 5)
      return frontEndSkills
# Employee parts
class Frameworks:
   frno = None

class Backend:
   beSkills = None

class FrontEndSkills:
   feSkills = None

def main():
   femp = FrontendDeveloper()
   bemp = BackEndDeveloper()
   director = Director()
   
   
   
   director.setBuilder(femp)
   
   emp1 = director.getEmployee()

   director.setBuilder(bemp)
   
   emp2 = director.getEmployee()
   print( "new generated frontend employee")
   emp1.specification()
   print( "new generated backend employee")
   emp2.specification()

if __name__ == "__main__":
   main()