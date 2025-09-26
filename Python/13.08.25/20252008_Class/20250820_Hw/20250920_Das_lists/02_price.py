goods = ['розы', 'кроссовки', 'машина', 'тетрадка', 'шоколадка']
prices = [500, 3500, 10000000, 34, 120]

prices_less_than_thousand = []
for price in prices:
    if price < 1000:
        prices_less_than_thousand.append(price)

print(prices_less_than_thousand)