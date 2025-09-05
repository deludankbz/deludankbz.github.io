import markdown 
from config import Config
from lxml import html

config = Config()

convHtml = markdown.markdown(
    config.getArticle(),
    extensions=['toc']
)

newDom = html.fromstring(config.getIndex())
body = newDom.cssselect("body")[0] # returns a list
body.insert(0, html.fromstring(convHtml))

resultHtml = html.tostring(newDom, method='html', encoding='unicode', doctype='html').__str__()

# print(resultHtml)
config.updateIndex(resultHtml)
# with open('test.html', 'w', encoding='utf-8') as fs:
#     fs.write(soup)
