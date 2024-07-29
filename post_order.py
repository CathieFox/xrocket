import requests
import json

def execute_order(amount):
    url = 'https://trade.ton-rocket.com/orders'
    headers = {
        'accept': 'application/json',
        'Rocket-Exchange-Key': '9F8hdV47kvU68ulyU8Brli6K26ccE5',
        'Content-Type': 'application/json'
    }
    data = {
        "pair": "TONCOIN-USDT",
        "type": "SELL",
        "executeType": "LIMIT",
        "rate": 8,
        "amount": amount,  # Using the variable amount here
        "currency": "USDT"
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 201:
        print("Order executed successfully")
        order_data = response.json()
        print("Order details:", order_data)

        # Check if the specific order ID is in the response and store it
        order_id = order_data['data']['orderId']
        if order_id == 13039297:
            print("The specific order ID 13039297 is found.")
            # Now you can use this order_id for other purposes
        else:
            print("The specific order ID 13039297 is not found. Current order ID is:", order_id)
        
    else:
        print("Failed to execute order")
        print("Status code:", response.status_code)
        print("Error response:", response.json())

# Call the function with a specific amount
execute_order(3)  # Pass any amount you wish to use here
