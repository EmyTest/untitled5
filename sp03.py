from urllib import request,parse
from http import cookiejar

cookie = cookiejar.CookieJar()
#生成cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
#创建http请求管理器
http_handler = request.HTTPHandler()
#生成http管理器
https_handler = request.HTTPHandler()
#创建请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)
def login():
   '''
   负责初次登录
   需要输入用户名密码，来获取cookie凭证
   :return:
   '''