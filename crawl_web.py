def crawl_web(seed):
  to_crawl = [seed]
  crawled = []
  while to_crawl:
    page = to_crawl.pop()
    if page not in crawled:
      #Union(to_crawl,get_all_links,get_page(page))
      crawled.append(page)
  return crawled
print(crawl_web('<div id="Google">Google <a href="https://www.google.fr/">Français</a>  <a href="https://www.google.de/">German</a> </div>'))