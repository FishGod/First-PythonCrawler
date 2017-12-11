# coding:utf8
from urllib import request
import http.cookiejar

url = "http://www.baidu.com"

print("第一种方法")
# 用urllib2的urlopen方法将url这个字符串作为参数来进行网页的下载
response1 = request.urlopen(url)
# 打印response1的状态码
print(response1.getcode())
# 打印返回内容网页的长度
print(len(response1.read()))

print("第二种方法")
# 通过Request对象增加一些特殊的处理
req = request.Request(url)
# 将爬虫伪装成一个浏览器
req.add_header('user-agent', 'Mozilla/5.0')
# 用urllib2的urlopen方法将url这个字符串作为参数来进行网页的下载
response2 = request.urlopen(req)
# 打印response2的状态码
print(response2.getcode())
# 打印返回内容网页的长度
print(len(response2.read()))

print("第三种方法（增加cookie处理）")
# 创建cookie容器
cj = http.cookiejar.CookieJar()
# 以容器作为参数创建一个Handler作为opener的参数
opener = request.build_opener(request.HTTPCookieProcessor(cj))
# 给urllib2安装这个opener
request.install_opener(opener)
# 用urllib2的urlopen方法将url这个字符串作为参数来进行网页的下载
response3 = request.urlopen(url)
# 打印response3的状态码
print(response3.getcode())
# 打印cookie的内容
print(cj)
# 打印网页内容
print(response3.read())