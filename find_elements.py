#return index of the first element in the list that mathces value
def find_element(list,value):
  for p in list:
    if p == value:
      return list.index(p)
  return (-1)
print(find_element([1,2,3,4],3))
print(find_element(['alpha','beta'],'gamma'))
def find_element1(list,value):
  return ", ".join(map(str,[list.index(p) for p in list if p == value]))
print(find_element1([1,2,3,4],3))