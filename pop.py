def pop(a):
  a.append(3)
  a.pop()
  return(a)
print(pop([1,2]))

def pop1(a):
  x = a.pop()
  y = a.pop()
  a.append(x)
  a.append(y)
  return(a)
print(pop1([1,2,3]))

def pop2(a):
  x = a.pop()
  a.append(x)
  return(a)
print(pop2([1,2]))

def pop3(a):
  x = a.pop()
  y = a.pop()
  a.append(y)
  a.append(x)
  return(a)
print(pop3([1,2,3]))

