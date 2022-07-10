import urllib.request
from lxml import etree
#第一页 https://sc.chinaz.com/tupian/meinvtupian.html

#第二页 https://sc.chinaz.com/tupian/meinvtupian_2.html  3https://sc.chinaz.com/tupian/meinvtupian_2.html
def create_request(page):
    if(page==1):
        url = 'https://sc.chinaz.com/tupian/meinvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/meinvtupian_'+str(page)+'.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    request = urllib.request.Request(url = url , headers = headers )
    return request

def create_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content
def down_load(page,content):

    # urllib.request.urlretrieve(content)

    tree = etree.HTML(content)
    name_list=tree.xpath('//div[@id="container"]//a/img/@alt')
    src_list = tree.xpath('//div[@id="container"]//a/img/@src')
    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url ='https:'+src
        urllib.request.urlretrieve(url=url, filename= name + '.jpg')


if __name__ == '__main__':
    start_page = int(input('qishi'))
    end_page = int(input('jieshu'))

    for page in range(start_page,end_page+1):

        request = create_request(page)
        content = create_content(request)
        down_load(page,content)



