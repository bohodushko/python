import get_next_target

def get_all_links(page):
  links = []
  while True:
    url, endpos = get_next_target.get_next_target(page)
    if url:
      links.append(url)
      page = page[endpos:]
    else:
      break
  return (links)
print(get_all_links('<div id="Google">Google <a href="https://www.google.fr/">Français</a>  <a href="https://www.google.de/">German</a> </div>'))
