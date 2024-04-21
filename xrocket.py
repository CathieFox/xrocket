import requests
import json
import time



def balance():
    
    global toncoin_balance, usdt_balance  # 声明全局变量
    
    # 设置API端点和API密钥
    url = 'https://trade.ton-rocket.com/account/balance'    
    
    api_key = 'SWQFoqJQ90bjRrOlRE3W05l2LTWVas'  # 这里用你的实际API密钥替换

# 准备请求头，包括认证信息
    headers = {
    'accept': 'application/json',
    'Rocket-Exchange-Key': api_key
    }


    response = requests.get(url, headers=headers)

# 初始化变量以存储特定货币的余额
    toncoin_balance = 0
    usdt_balance = 0
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

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def get_ratio(base, quote):
    url = f"https://trade.ton-rocket.com/rates/crypto/{base}/{quote}"
    headers = {'accept': 'application/json'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if data['success']:
            rate = data['data']['rate']
            return rate
        else:
            return "Failed to fetch rate, API returned an error."
    else:
        return f"Failed to fetch rate, status code: {response.status_code}"

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


def post_order_sell(ratio1,amount_sell):
    
    global order_id_sell
    
    url = 'https://trade.ton-rocket.com/orders'
    headers = {
        'accept': 'application/json',
        'Rocket-Exchange-Key': api_key,
        'Content-Type': 'application/json'
    }
    data = {
        "pair": "TONCOIN-USDT",
        "type": "SELL",
        "executeType": "LIMIT",
        "rate": ratio1,
        "amount": amount_sell,  # Using the variable amount here
        "currency": "TONCOIN"
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 201:
        print("Order executed successfully")
        order_data = response.json()
        print("Order details:", order_data)

        # Check if the specific order ID is in the response and store it
        order_id_sell = order_data['data']['orderId']
        print("Current order ID is:", order_id_sell)
        
    else:
        print("Failed to execute order")
        print("Status code:", response.status_code)
        print("Error response:", response.json())

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def post_order_buy(ratio1,amount_buy):
    
    global order_id_buy
    
    url = 'https://trade.ton-rocket.com/orders'
    headers = {
        'accept': 'application/json',
        'Rocket-Exchange-Key': api_key,
        'Content-Type': 'application/json'
    }
    data = {
        "pair": "TONCOIN-USDT",
        "type": "BUY",
        "executeType": "LIMIT",
        "rate": ratio1,
        "amount": amount_buy,  # Using the variable amount here
        "currency": "USDT"
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 201:
        print("Order executed successfully")
        order_data = response.json()
        print("Order details:", order_data)

        # Check if the specific order ID is in the response and store it
        order_id_buy = order_data['data']['orderId']
        print("Current order ID is:", order_id_buy)
        
    else:
        print("Failed to execute order")
        print("Status code:", response.status_code)
        print("Error response:", response.json())

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def check_order(order_id):
    
    global order_data_check
    
    url = f'https://trade.ton-rocket.com/orders/{order_id}'
    headers = {
        'accept': 'application/json',
        'Rocket-Exchange-Key': api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        order_data_check = response.json()
        print("Order details fetched successfully:")
        print(json.dumps(order_data_check, indent=2))

        # Check if the order is closed or not
#        if order_data_check['data']['closed'] is None:
#            print("The order is still open/not completed.")
#        else:
#            print("The order has been completed. Closed timestamp:", order_data_check['data']['closed'])
    else:
        print("Failed to fetch order details")
        print("Status code:", response.status_code)
        print("Error response:", response.json())

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def cancel_order(order_id_cancel):
    url = f'https://trade.ton-rocket.com/orders/{order_id_cancel}'
    headers = {
        'accept': 'application/json',
        'Rocket-Exchange-Key': api_key
    }

    response = requests.delete(url, headers=headers)

    if response.status_code == 200:
        print("订单取消成功")
        print("Response:", response.json())
    else:
        print("订单取消失败")
        print("Status code:", response.status_code)
        print("Error response:", response.json())



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


api_key = ''  # 这里用你的实际API密钥替换

# Example usage
base_currency = "TONCOIN"
quote_currency = "USDT"


balance()
ratio = get_ratio(base_currency, quote_currency)
print(f"The current rate for {base_currency}/{quote_currency} is {ratio}")


#更改为float 格式
toncoin_balance1 = float(toncoin_balance)
usdt_balance1 = float(usdt_balance)
ratio1 = float(ratio)

count = 0

while True:

    
    balance()
    ratio = get_ratio(base_currency, quote_currency)
    print(f"The current rate for {base_currency}/{quote_currency} is {ratio}")


    #更改为float 格式
    toncoin_balance1 = float(toncoin_balance)
    usdt_balance1 = float(usdt_balance)
    ratio1 = float(ratio)


    #amount set
    amount_sell = 0.9 * toncoin_balance1
    amount_buy  = 0.9 * usdt_balance1


    #主函数
    if toncoin_balance1 * ratio1 >= usdt_balance1 :
        print("Sell")
        post_order_sell(ratio1,amount_sell)
        
        for i in range(2):
            check_order(order_id_sell)
            time.sleep(0.5)
            
            
        if order_data_check['data']['closed'] is None:
            print("The order is still open/not completed.")
            cancel_order(order_id_sell)
            
            
        else:
            print("The order has been completed. Closed timestamp:", order_data_check['data']['closed'])            


    else :
        print("Buy")
        post_order_buy(ratio1,amount_buy)
        
        for i in range(2):
            check_order(order_id_buy)  
            time.sleep(0.5)
            
            
        if order_data_check['data']['closed'] is None:            
            print("The order is still open/not completed.")
            cancel_order(order_id_buy)
            

        else:
            print("The order has been completed. Closed timestamp:", order_data_check['data']['closed'])


