def union(a,b):
  for i in b:
    if i not in a:
      a.append(i)
  return(a)
print(union([1,2,3],[2,4,6]))