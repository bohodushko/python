def is_friend(name):
  if name[0] == 'M' or name[0] == 'N':
    return True
  else:
    return False

print(is_friend('Mark'))