import requests
url = "https://niuchao.com/"
res = requests.get(url)
print(res.text)  