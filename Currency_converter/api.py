import requests
import json

url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

currency_1 = "EUR"
currency_2 = "USD"
amount = "100"

querystring = {"from":currency_1,"to":currency_2,"amount":amount}

headers = {
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com",
	"X-RapidAPI-Key": "d89a5f7563msh0c167d15c18f43cp18cf23jsne8203ccaf856"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)
converted_amount = data['result']['convertedAmount']
formatted = "{:,.2f}".format(converted_amount)
print(converted_amount, formatted)
