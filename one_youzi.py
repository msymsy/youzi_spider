from get_ip import freeProxy09
import requests
import random
from bs4 import BeautifulSoup as bs
from zhuye_index import	get_index_html_test,get_index_html
import pandas as pd

def get_data(youzi_url,user_agent,ip):
	'''
	从每个游资的url进来
	return 表格
	'''
	


# 获取一个随机user_agent和Referer
	header = {'User-Agent': user_agent}
	response = requests.get(youzi_url, proxies={"http":ip}, timeout=3, headers=header).text

	soup2=bs(response,"lxml")
	date=soup2.find_all('tr')[0].a.string
	'''
	表头['所用席位', '操作标的', '买入额(万)', '卖出额(万)', '净买入额(万)', '近3个月上榜', '上榜后上涨概率(%)', '上榜原因']
	'''
	xiwei=[]
	biaodi=[]
	buy=[]
	sell=[]
	jinmairue=[]
	shangban_num=[]
	shangbangailv=[]
	yuanyin=[]

	for num in range(2,len(soup2.find_all('tr'))-1):
	    c=soup2.find_all('tr')[num].find_all('td')
	    xiwei.append(c[0].get_text())
	    biaodi.append(c[1].get_text())
	    buy.append(c[2].get_text())
	    sell.append(c[3].get_text())
	    jinmairue.append(c[4].get_text())
	    shangban_num.append(c[5].get_text())
	    shangbangailv.append(c[6].get_text())
	    yuanyin.append(c[7].get_text())

	data=pd.DataFrame()
	data['日期']=[date]*len(xiwei)
	data['所用席位']=xiwei
	    
	data['操作标的']=biaodi
	data['买入额(万)']=buy
	data['卖出额(万)']=sell
	data['净买入额(万)']=jinmairue
	data['近3个月上榜']=shangban_num
	data['上榜后上涨概率(%)']=shangbangailv
	data['上榜原因']=yuanyin
	return data