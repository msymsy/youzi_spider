import pandas as pd 
import os

path='data/'
dir_list=os.listdir(path)
data=pd.DataFrame()
for dir_name in dir_list:
	youzi_name=dir_name.split('.')[0]
	newpath=path+dir_name
	newdata=pd.read_excel(newpath)
	newdata['游资名称']=[youzi_name]*len(newdata)
	data=pd.concat([data,newdata])
data['日期']= pd.to_datetime(data['日期'], format = '%Y年%m月%d日')
data=data.sort_values(by='日期')
data.set_index(data['日期'],inplace=True)
data.to_excel('汇总.xlsx',index=False)