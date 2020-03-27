from get_ip import freeProxy09
import random
from zhuye_index import	get_index_html_test,get_index_html
import pandas as pd
from one_youzi import get_data


ip_list=freeProxy09(page_count=1)
ip=random.choice(ip_list)
# user_agent列表
user_agent_list = [
	    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
	    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
	    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
	    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',
	    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36',
	    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
	]
user_agent=random.choice(user_agent_list)

url='https://www.lhbjd.com'

html=get_index_html(url+'/bbs/',user_agent,ip)
print(list(html.keys())[3:])

youzi_list=list(html.keys())[3:]
print(html[youzi_list[1]])
for i in range(len(youzi_list)):
    youzi_url=url+html[youzi_list[i]]

    data=get_data(youzi_url,user_agent,ip)


    dataname=youzi_list[i].split('(')[0]
    
    old_data=pd.read_excel('data/'+dataname+'.xlsx')
    old_data[list(old_data.columns)]=old_data[list(old_data.columns)].astype('str')
    newdata=pd.concat([old_data,data])
    newdata=newdata[newdata.duplicated()!=True] ##删除重复数据的方法duplicated（）
    newdata.to_excel('data/'+dataname+'.xlsx',index=False)
    print('已完成：    '+dataname)
    
    
    
    
    
    
    
    
    
    