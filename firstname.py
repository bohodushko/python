class Person:
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname
  def display(self):
    print(self.firstname, self.lastname)
class Player(Person):
  pass
obj = Player("Aaa", "Bbb")
obj.display()
