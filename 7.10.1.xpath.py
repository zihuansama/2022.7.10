# from lxml import etree
# tree = etree.parse('xpath.html')
#
#
# li_list = tree.xpath('//body//li')
# print(li_list)
# print(len(li_list))

import urllib.request

url = 'https://www.baidu.com/'

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# with open('baidu.html','w',encoding='utf-8')as fp:
#     fp.write(content)
from lxml import etree
tree = etree.HTML(content)
result = tree.xpath('//input[@id="su"]/@value')[0]#xpath 的返回值是一个列表类型的数据
#返回的是['百度一下']
print(result)
