import requests

# API端点URL
url = 'https://trade.ton-rocket.com/version'

# 发送GET请求
response = requests.get(url)

# 确认请求成功
if response.status_code == 200:
    # 解析JSON响应体
    data = response.json()
    print("Version", data['version'])
else:
    print("请求失败，状态码:", response.status_code)
    