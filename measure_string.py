def measure_string(a):
  count = 0
  for p in a:
    if p[0] == 'A':
      count = count + 1
  return(count)

print(measure_string(['John','Bob','Alice']))
print(measure_string(['Eric','Cynthia']))