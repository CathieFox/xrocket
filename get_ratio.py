import requests

def get_crypto_rate(base, quote):
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

# Example usage
base_currency = "TONCOIN"
quote_currency = "USDT"
rate = get_crypto_rate(base_currency, quote_currency)
print(f"The current rate for {base_currency}/{quote_currency} is {rate}")
