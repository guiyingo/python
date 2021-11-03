# =============================================================================
# 3.1 百度新闻数据挖掘 by 王宇韬 代码更新：www.huaxiaozhi.com 资料下载区
# =============================================================================
# 书本里的代码有问题，了解下思路就行了，代码还是以下载为准，再对照实践。
import requests
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

url = 'https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd=台海'  # 把链接中rtt参数换成4即是按时间排序，默认为1按焦点排序，3.4.1小节也有讲到
res = requests.get(url, headers=headers).text  # 加上headers用来告诉网站这是通过一个浏览器进行的访问
# print(res)

p_href = '<h3 class="news-title_1YtI1"><a href="(.*?)"'
href = re.findall(p_href, res, re.S)
# print(href)

p_title = '<h3 class="news-title_1YtI1">.*?>(.*?)</a>'
title = re.findall(p_title, res, re.S)
# print(title)

p_date = '<span class="c-color-gray2 c-font-normal"(.*?)</span>' #原代码多一个>
# p_date = '<span class="c-color-gray2 c-font-normal"'
date = re.findall(p_date, res,re.S)
# print(date)

# p_source = '<span class="c-color-gray c-font-normal c-gap-right">(.*?)</span>'#原代码多一个  >
p_source = '<span class="c-color-gray c-font-normal c-gap-right"(.*?)</span>'
source = re.findall(p_source, res)

# for i in range(len(source)):
#     p_source = '"(.*?)"'

#     # source_1 = []
#     source[i] = re.findall(p_source, source[i])  ##重点理解，这里列表的元素也变成列表了；Findall函数只能用于文本，直接对列表无效，所以只能对列表中元素筛选，筛选的结果是列表，作为元素存储在列表中。
#     # print(source[])

# for i in range(len(date)):
#     p_date = 'aria-label="(.*?)">'
#     date[i] = re.findall(p_date,date[i])
#     # print(source[i])

# print(title)
# # print(href)
# print(date)
# print(source)


for i in range(len(title)):  # range(len(title)),这里因为知道len(title) = 10，所以也可以写成for i in range(10)
    title[i] = title[i].strip()  # strip()函数用来取消字符串两端的换行或者空格，不过目前（2020-10）并没有换行或空格，所以其实不写这一行也没事
    title[i] = re.sub('<.*?>', '', title[i])  # 核心，用re.sub()函数来替换不重要的内容
    
    p_source = '"(.*?)"'
    # source_1 = []
    source[i] = re.findall(p_source, source[i]) 


    p_date = 'aria-label="(.*?)">'
    date[i] = re.findall(p_date,date[i])

    # print(str(i + 1) + '.' + title[i] + '(' + source[i] + ' ' + date[i] + ')')
    print(str(i+1) + '.' + title[i]+';'+source[i][0] + ';' + date[i][0])
    print(href[i])

