from datetime import datetime, timedelta

class Product:
    total_products = 0

    def __init__(self, name, price, manufacture_date, store_product_time=3*365):
        self.__name = name
        self.__price = price
        self.manufacture_date = manufacture_date
        self.expiry_date = self.manufacture_date + timedelta(days=store_product_time)
        Product.total_products += 1

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def is_expired(self):
        return datetime.now() > self.expiry_date

    @property
    def time_until_expiry(self):
        if self.is_expired:
            return "Просрочен"
        
        time_left = self.expiry_date - datetime.now()
        if time_left > timedelta(days=2):
            return f"{time_left.days} дней"
        else:
            hours_left = int(time_left.total_seconds() // 3600)
            return f"{hours_left} часов"

    def __str__(self):
        return (f"Продукт: {self.name}, Цена: {self.price} руб., "
                f"Статус: {self.time_until_expiry}")


class MilkProduct(Product):
    category = "Молочные продукты"
    def __init__(self, name, price, manufacture_date):
        super().__init__(name, price, manufacture_date, store_product_time=3)


class MeatProduct(Product):
    category = "Мясные продукты"
    def __init__(self, name, price, manufacture_date):
        super().__init__(name, price, manufacture_date, store_product_time=1)


class BakeryProduct(Product):
    category = "Хлебобулочные изделия"

class ExpiredProductError(ValueError):
    pass

def make_order(stock, items_to_buy):
    total_cost = 0
    items_to_remove = []

    print("\n--- Формирование заказа ---")
    for item in items_to_buy:
        if item.is_expired:
            raise ExpiredProductError(f"Нельзя купить просроченный товар: '{item.name}'")
        if item in stock:
            total_cost += item.price
            items_to_remove.append(item)
            print(f"Добавлено в заказ: {item.name} ({item.price} руб.)")
        else:
            print(f"Товар '{item.name}' отсутствует на складе и не может быть добавлен.")

    for item in items_to_remove:
        stock.remove(item)
    return total_cost

def calculate_loss(stock):
    total_loss = 0
    for item in stock:
        if item.is_expired:
            total_loss += item.price
    return total_loss


if __name__ == "__main__":
    now = datetime.now()
    
    milk1 = MilkProduct("Молоко Простоквашино 3.2%, 1.4л", 154.90, now - timedelta(days=1)) 
    milk2 = MilkProduct("Веселый молочник 1.5%, 930мл", 87.90, now - timedelta(days=3)) 
    milk3 = MilkProduct("Ростагроэксово 2.5%, 930мл", 89.99, now) 
    milk4 = MilkProduct("Домик в деревне 3.4-4.5%, 0.93л", 114.99, now - timedelta(days=2, hours=20)) 

    meat1 = MeatProduct("Куриная грудка замороженная, 250г", 299.99, now - timedelta(hours=10)) 
    meat2 = MeatProduct("Говядина высший сорт ГОСТ, 500г", 550.60, now - timedelta(days=1)) 
    meat3 = MeatProduct("Свинина карбонад копчёно-варёный, 300г", 399.99, now) 

    bakery1 = BakeryProduct("Хлеб Бородинский нарезка, 390г", 84.99, now - timedelta(days=1)) 
    bakery2 = BakeryProduct("Изделия макаронные Pasteroni высший сорт, 400г", 101.99, now - timedelta(days=5)) 
    canned = Product("Икра Красное Золото горбуша зернистая, 100г", 1199, now - timedelta(days=200))

# Store stock Items:
    store_stock = [milk1, milk2, milk3, milk4, meat1, meat2, meat3, bakery1, bakery2, canned]

    print(f"Всего создано продуктов: {Product.total_products}")
    print("\n--- Текущий ассортимент магазина ---")
    for product in store_stock:
        print(product)

# Calculating losses from expired goods : 
    loss = calculate_loss(store_stock)
    print(f"\n--- Расчет убытков ---")
    print(f"Общая цена просроченных товаров: {loss} руб.")

# Order to Make : 
    order_to_make = [milk3, meat1, milk2] 

    try:
        order_total = make_order(store_stock, order_to_make)
        print(f"\n--- Итог заказа ---")
        print(f"Сумма заказа: {order_total} руб.")
    except ExpiredProductError as e:
        print(f"\n!!! Ошибка при оформлении заказа: {e} !!!")


# successful order : 
    successful_order = [milk3, meat1, bakery1]
    try:
        order_total_2 = make_order(store_stock, successful_order)
        print(f"\n--- Итог заказа ---")
        print(f"Сумма заказа: {order_total_2} руб.")
    except ExpiredProductError as e:
        print(f"\n!!! Ошибка при оформлении заказа: {e} !!!")

# Remaining stock after purchases: 
    print("\n--- Ассортимент магазина после покупок ---")
    for product in store_stock:
        print(product)

