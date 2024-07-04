import requests
import json
import sys

try:
    n = float(sys.argv[1])
except (ValueError and IndexError):
    sys.exit()

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    print("no luck")
    sys.exit()

o = response.json()

cost = float(o["bpi"]["USD"]["rate_float"])

print(F"${(cost * n):,.4f}")



