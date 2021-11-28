from get_next_target import get_next_target


import get_next_target

def print_all_links(page):
  while True:
    url,endpos = get_next_target.get_next_target(page)
    if url:
      print(url)
      page = page[endpos:]
    else:
      break
print_all_links('<div id="Google">Google <a href="https://www.google.fr/">Français</a>  <a href="https://www.google.de/">German</a> </div>')
