import requests
from lxml import etree


page=1
target_url = 'http://www.xicidaili.com/nn/%d' % page
#完善的headers
target_headers = {'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer':'http://www.xicidaili.com/nn/',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
}

roo=requests.get(target_url,headers=target_headers)
print(roo)
roo=roo.text
etree_roo=etree.HTML(roo)
ip=etree_roo.xpath('//td[2]/text()')   #text()获取文本
port=etree_roo.xpath('//td[3]/text()')
protocol=etree_roo.xpath('//td[6]/text()')
add_ip=[]
for x in range(len(ip)):
    ip_list= protocol[x]+'#'+ip[x]+':'+port[x]
    print(ip_list)

# print(protocol+'#'+ip+':'+port)


