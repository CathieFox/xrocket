import requests


# 设置API端点和API密钥
url = 'https://trade.ton-rocket.com/account/balance'
api_key = '9F8hdV47kvU68ulyU8Brli6K26ccE5'  # 这里用你的实际API密钥替换

# 准备请求头，包括认证信息
headers = {
    'accept': 'application/json',
    'Rocket-Exchange-Key': api_key
}


response = requests.get(url, headers=headers)

# 初始化变量以存储特定货币的余额
toncoin_balance = 0
usdt_balance = 0

# 检查请求是否成功
if response.status_code == 200:
    # 解析返回的JSON数据
    data = response.json()
    print("请求成功")
    for balance in data['data']['balances']:
        if balance['code'] == 'TONCOIN':
            toncoin_balance = balance['amount']
            print(f"TONCOIN余额: {toncoin_balance}")
        elif balance['code'] == 'USDT':
            usdt_balance = balance['amount']
            print(f"USDT余额: {usdt_balance}")
else:
    print(f"请求失败，状态码: {response.status_code}")

# 使用或输出获取的余额数据
# print(toncoin_balance, usdt_balance)  # 例如，打印或进一步处理
