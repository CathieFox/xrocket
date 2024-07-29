import requests
import json

def check_order_status(order_id):
    url = f'https://trade.ton-rocket.com/orders/{order_id}'
    headers = {
        'accept': 'application/json',
        'Rocket-Exchange-Key': '9F8hdV47kvU68ulyU8Brli6K26ccE5'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        order_data = response.json()
        print("Order details fetched successfully:")
        print(json.dumps(order_data, indent=2))

        # Check if the order is closed or not
        if order_data['data']['closed'] is None:
            print("The order is still open/not completed.")
        else:
            print("The order has been completed. Closed timestamp:", order_data['data']['closed'])
    else:
        print("Failed to fetch order details")
        print("Status code:", response.status_code)
        print("Error response:", response.json())

# Example usage:
check_order_status(13040643)  # Pass the specific order ID you want to check
