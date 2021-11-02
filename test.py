import requests
import re
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

url = 'https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd=阿里巴巴'  # 把链接中rtt参数换成4即是按时间排序，默认为1按焦点排序，3.4.1小节也有讲到
res = requests.get(url, headers=headers).text  # 加上headers用来告诉网站这是通过一个浏览器进行的访问
print(res)     

p_info = '<p class="c-author">(.*?)</p>'
info =  re.findall(p_info,res,re.S)
print(info)
