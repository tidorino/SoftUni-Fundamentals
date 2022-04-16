import math
centuries = int(input())

years = centuries * 100
days = years * 365.2422
hours = math.floor(days) * 24
minutes = math.floor(hours) * 60

print(f"{centuries} centuries = {years} years = {math.floor(days)} days = {math.floor(hours)} "
      f"hours = {math.floor(minutes)} minutes")