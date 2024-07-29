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
    

# 设置API端点和API密钥
url = 'https://trade.ton-rocket.com/account/balance'
api_key = '9F8hdV47kvU68ulyU8Brli6K26ccE5'  # 这里用你的实际API密钥替换

# 准备请求头，包括认证信息
headers = {
    'accept': 'application/json',
    'Rocket-Exchange-Key': api_key
}

# 发送GET请求
response = requests.get(url, headers=headers)

# 检查请求是否成功
if response.status_code == 200:
    # 解析返回的JSON数据
    data = response.json()
    print("请求成功，账户余额信息如下:")
    for balance in data['data']['balances']:
        print(f"Coin: {balance['code']}, Value: {balance['amount']}")
else:
    print(f"请求失败，状态码: {response.status_code}")
    
    
