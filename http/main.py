import requests

#打印版本及版权
print(requests.__version__)
print(requests.__copyright__)

#打印网页
resp = requests.get("http://www.baidu.com")
print(resp.text)

#获取一个网页并剥离其HTML标签
import re

resp = requests.get("http://www.webcode.me")
content = resp.text
stripped = re.sub('<[^<]+?>', '', content)
print(stripped)

#创建一个GET请求
resp = requests.request(method='GET', url="http://www.webcode.me")
print(resp.text)

#使用get()方法获取请求/响应信息
url = "http://www.baidu.com"
res = requests.get(url)	
print(res.request.headers)		# 查看请求头信息
print(res.request.body)			# 查看请求正文
print(res.request.url)			# 查看请求url
print(res.request.method)		# 查看请求方法
print(res.content)		# 响应结果的字节码格式，一般用于图片，视频数据等
print(res.encoding)		# 查看响应正文的编码格式
print(res.text)			# 响应结果的字符串格式，非字节码
print(res.status_code)	# 响应结果状态码，200 表示成功
print(r.reason)			# 响应状态码的描述信息，如 OK，NotFound 等
print(res.cookies)		# 获取 cookies
print(res.headers)		# 查看响应的响应头
print(res.url)			# 查看响应的url

#使用get()方法请求指定资源
resp = requests.get("https://httpbin.org/get?name=Peter")
print(resp.text)

#数据在 Python 字典中发送
payload = {'name': 'Peter', 'age': 23}
resp = requests.get("https://httpbin.org/get", params=payload)
print(resp.url)
print(resp.text)
print(resp.json())  #使用json()方法解码

#定制请求头
url = "https://www.imooc.com/search/coursesearchconditions"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
payload = {
    'words': 'python'
}
res = requests.get(url, params=payload, headers=headers)
print(res.json()) #响应内容是 json 格式的字符串，我们使用 res.json() 方法进行解码
print(res.request.headers)  # 查看请求头

#head()方法检索文档标题
resp = requests.head("http://www.webcode.me")
print("Server: " + resp.headers['server'])
print("Content type: " + resp.headers['content-type'])

#post方法在给定的 URL 上调度 POST 请求，为填写的表单内容提供键/值对
data = {'name': 'Peter'}
resp = requests.post("https://httpbin.org/post", data)
print(resp.text)

#post()方法，data传入元组列表
url = 'http://httpbin.org/post'
payload = (('course', 'Python'), ('course', 'Java'))
r = requests.post(url=url, data=payload)
print(r.text)
