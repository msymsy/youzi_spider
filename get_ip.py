import requests
import json
from webrequest import WebRequest
from lxml import etree

def getHtmlTree(url, **kwargs):
    """
    获取html树
    :param url:
    :param kwargs:
    :return:
    """

    header = {'Connection': 'keep-alive',
              'Cache-Control': 'max-age=0',
              'Upgrade-Insecure-Requests': '1',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate, sdch',
              'Accept-Language': 'zh-CN,zh;q=0.8',
              }
    # TODO 取代理服务器用代理服务器访问
    wr = WebRequest()
    html = wr.get(url=url, header=header).content
    return etree.HTML(html)
def freeProxy09(page_count=1):
    """
    http://ip.jiangxianli.com/?page=
    免费代理库
    :return:
    """
    ip=[]
    for i in range(1, page_count + 1):
        url = 'http://ip.jiangxianli.com/?country=中国&?page={}'.format(i)
        html_tree = getHtmlTree(url)
        
        for index, tr in enumerate(html_tree.xpath("//table//tr")):
            if index == 0:
                continue
            a=":".join(tr.xpath("./td/text()")[0:2]).strip()
            ip.append(a)
            # yield ":".join(tr.xpath("./td/text()")[0:2]).strip()
    return ip

if __name__ == '__main__':
  ip=freeProxy09(page_count=2)
  print(ip)
