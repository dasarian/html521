goods = ['розы', 'кроссовки', 'машина', 'тетрадка', 'шоколадка']
prices = [500, 3500, 10000000, 34, 120]

prices_less_than_thousand = [price for price in prices if price < 1000]
print("Цены меньше тысячи:", prices_less_than_thousand)
