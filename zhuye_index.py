from get_ip import freeProxy09
import requests
import random
from bs4 import BeautifulSoup as bs

def get_index_html(url,user_agent,ip):
	
	
	# user_agent列表
	user_agent_list = [
	    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
	    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
	    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
	    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',
	    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36',
	    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
	]

	# referer列表


	# 获取一个随机user_agent和Referer
	header = {'User-Agent': user_agent}
	response = requests.get(url, proxies={"http": ip}, timeout=3, headers=header).text

	soup2=bs(response,"lxml")
	'''
	soup=<div class="row rounded bg-light p-3">
	<div class="col-12 my-2">游资专区：</div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/asking/" target="_blank">Asking(<span class="text-danger">2</span>)</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/zhongxinmudanjiang/" target="_blank">中信牡丹江(<span class="text-danger">1</span>)</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/chengdubang/" target="_blank">成都帮(<span class="text-danger">1</span>)</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/zhaolaoge/" target="_blank">赵老哥(<span class="text-danger">1</span>)</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/zhongxingubei/" target="_blank">中信古北路</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/zhongxinsiji/" target="_blank">中信四季</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/zhongxinhuaihai/" target="_blank">中信淮海路</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/zhongxinliyang/" target="_blank">中信溧阳路</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/qiaobangzhu/" target="_blank">乔帮主</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/jiuzhouzhejiangfengongsi/" target="_blank">九州浙江分公司</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/foshanwuyingjiao/" target="_blank">佛山无影脚</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/gerourong/" target="_blank">割肉荣</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/huataixiamenxiahe/" target="_blank">华泰厦门厦禾路</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/huataiwudinglu/" target="_blank">华泰武定路</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/huataihunanfengongsi/" target="_blank">华泰湖南分公司</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/tanghanruo/" target="_blank">唐汉若</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/guoyuanhongqiaolu/" target="_blank">国元虹桥路</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/sunge/" target="_blank">孙哥</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/xiaoeyu/" target="_blank">小鳄鱼</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/shandongbang/" target="_blank">山东帮</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/huanlehai/" target="_blank">欢乐海</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/shenfuxing/" target="_blank">沈付兴</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/shennange/" target="_blank">深南哥</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/qingyangge/" target="_blank">清扬哥</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/wenzhoubang/" target="_blank">温州帮</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/chaoguyangjia/" target="_blank">炒股养家</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/duguyijian/" target="_blank">独孤一剑</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/ruihexian/" target="_blank">瑞鹤仙</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/zhangjianping/" target="_blank">章建平</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/luohuge/" target="_blank">罗湖哥</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/zhiyechaoshou/" target="_blank">职业炒手</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/luosheng/" target="_blank">落升</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/caifuqingchunlu/" target="_blank">财富庆春路</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/doubuqingbai/" target="_blank">都不清白</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/yinheningbocuibailu/" target="_blank">银河宁波翠柏路</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/longfeihu/" target="_blank">龙飞虎(克拉美书)</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/huafutiananlu/" target="_blank">华福田安路</a></div>
	<div class="col-6 col-md-4 col-lg-3 my-2"><a href="/bar/guangdaningbojiefangnanlu/" target="_blank">光大宁波解放南路</a></div>
	</div>

	'''
	html={}
	for i in soup2.find_all('div',"col-6 col-md-4 col-lg-3 my-2"):
		html[i.get_text()]=i.a['href']
	return html

def get_index_html_test(url):
	html={'股民学校(72)': '/bar/school/',
	 '综合(13)': '/bar/zonghe/',
	 '散户': '/bar/sanhu/',
	 'Asking(2)': '/bar/asking/',
	 '中信牡丹江(1)': '/bar/zhongxinmudanjiang/',
	 '成都帮(1)': '/bar/chengdubang/',
	 '赵老哥(1)': '/bar/zhaolaoge/',
	 '中信古北路': '/bar/zhongxingubei/',
	 '中信四季': '/bar/zhongxinsiji/',
	 '中信淮海路': '/bar/zhongxinhuaihai/',
	 '中信溧阳路': '/bar/zhongxinliyang/',
	 '乔帮主': '/bar/qiaobangzhu/',
	 '九州浙江分公司': '/bar/jiuzhouzhejiangfengongsi/',
	 '佛山无影脚': '/bar/foshanwuyingjiao/',
	 '割肉荣': '/bar/gerourong/',
	 '华泰厦门厦禾路': '/bar/huataixiamenxiahe/',
	 '华泰武定路': '/bar/huataiwudinglu/',
	 '华泰湖南分公司': '/bar/huataihunanfengongsi/',
	 '唐汉若': '/bar/tanghanruo/',
	 '国元虹桥路': '/bar/guoyuanhongqiaolu/',
	 '孙哥': '/bar/sunge/',
	 '小鳄鱼': '/bar/xiaoeyu/',
	 '山东帮': '/bar/shandongbang/',
	 '欢乐海': '/bar/huanlehai/',
	 '沈付兴': '/bar/shenfuxing/',
	 '深南哥': '/bar/shennange/',
	 '清扬哥': '/bar/qingyangge/',
	 '温州帮': '/bar/wenzhoubang/',
	 '炒股养家': '/bar/chaoguyangjia/',
	 '独孤一剑': '/bar/duguyijian/',
	 '瑞鹤仙': '/bar/ruihexian/',
	 '章建平': '/bar/zhangjianping/',
	 '罗湖哥': '/bar/luohuge/',
	 '职业炒手': '/bar/zhiyechaoshou/',
	 '落升': '/bar/luosheng/',
	 '财富庆春路': '/bar/caifuqingchunlu/',
	 '都不清白': '/bar/doubuqingbai/',
	 '银河宁波翠柏路': '/bar/yinheningbocuibailu/',
	 '龙飞虎(克拉美书)': '/bar/longfeihu/',
	 '华福田安路': '/bar/huafutiananlu/',
	 '光大宁波解放南路': '/bar/guangdaningbojiefangnanlu/'}
	return html