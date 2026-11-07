import pathlib,re
from html.parser import HTMLParser
r=pathlib.Path(__file__).parent
pages=[r/'index.html',r/'404.html',*sorted((r/'work').glob('*/index.html'))]
class Tags(HTMLParser):
 def __init__(self):super().__init__();self.links=[]
 def handle_starttag(self,tag,attrs):
  if tag in ('a','link','script','img'):
   d=dict(attrs);link=d.get('href') or d.get('src');
   if link:self.links.append(link)
for page in pages:
 text=page.read_text();assert '<title>' in text and 'name="description"' in text,page
 parser=Tags();parser.feed(text)
 for link in parser.links:
  if link.startswith(('https:','http:','mailto:','#')):continue
  path=(page.parent/link.split('#')[0]).resolve()
  assert path.exists(),(page,link)
print(f'OK: {len(pages)} HTML pages; local asset and route references resolved.')
