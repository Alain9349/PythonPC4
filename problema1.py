import requests

try:
  n = int(input("Ingrese la cantidad de Bitcoins: "))
  response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
  response.raise_for_status()
  data = response.json()
  price = float(data["bpi"]["USD"]["rate_float"])
  amount = n * price
  print(f"${amount:,.4f}")
except requests.RequestException as e:
  print(f"Error al obtener el precio de Bitcoin: {e}")
except ValueError:
  print("Por favor, ingrese un número válido.")
