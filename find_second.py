def find_second(search, target):
  first = search.find(target)
  return(search.find(target,first+1))
print(find_second("bbtaabbtaa","t"))