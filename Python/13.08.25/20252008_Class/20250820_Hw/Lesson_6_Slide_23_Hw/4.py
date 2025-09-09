# 4. Вывести на экран таблицу из 4 строк:
# три товара и сумма без использования цикла
apple = 150
apple_str = 'Яблоки'
shoes = 2300
shoes_str = 'Кроссовки'
soap = 70
soap_str = 'Мыло'
print(f'''{apple_str:9s}  {apple}
{shoes_str:9s}  {shoes}
{soap_str:9s}  {soap}
{'':9s}  {soap + apple + shoes}
''')
