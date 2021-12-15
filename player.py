class Player:
  
  def __init__(self, name, age):
      self.name = name
      self.age = age
  
  def newHi(self):
    print("Hi, My name is " + self.name)
  
  def newHi1(self):
    print('Hi, My name is ' + self.name + ". " + "I'm " + str(self.age) + " years old." )

obj = Player("Developer", 45)
obj.newHi1()

