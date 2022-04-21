def capitals():

    country = input().split(", ")
    capital = input().split(", ")
    result = dict(zip(country, capital))
    for key, value in result.items():
        print(f"{key} -> {value}")


capitals()
