import requests
import lxml.html

html = requests.get('https://www.udemy.com/the-web-developer-bootcamp')
doc = lxml.html.fromstring(html.content)

# new_releases = doc.xpath('//div[@class="reviews-section--title--2Uzsu"]/text()')
new_releases = doc.xpath('//body[@id="udemy"]')
# print(doc)
print(new_releases)