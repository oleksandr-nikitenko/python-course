"""
Also, the ProductStore class must have the following methods:
add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your
store(30 percent)
set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input
identifiers (type or name). The discount must be specified in percentage
sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case
raises an error. It also increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
"""


class Product:
    def __init__(self, type, name, price):
        self.type_ = type
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'Name: {self.name}, type: {self.type_}, price: {self.price}'


class ProductStore:
   
    def __init__(self):
        self. products = []
        self.__income = float()
        
    def add(self, product: Product, amount: int) -> None:
        product.price += 0.3 * product.price
        product.amount = amount
        self.products.append(product)
        
    def set_discount(self, identifier: str, percent: int) -> None:
        for i in range(0, len(self.products)):
            if self.products[i].name == identifier or self.products[i].type_ == identifier:
                self.products[i].price -= self.products[i].price * (percent / 100)
            
    def sell_product(self, product_name: str, amount: int) -> None:
        for i in range(0, len(self.products)):
            if self.products[i].name == product_name and self.products[i].amount >= amount:
                self.products[i].amount -= amount
                self.__income += self.products[i].price * amount
            else:
                continue
                
    def get_income(self) -> float:
        return self.__income

    def get_all_products(self) -> str:
        products_display = str()
        for i in self.products:
            if i.amount != 0:
                products_display += f'{i.name.upper()}: type: {i.type_}, price: {i.price}, amount: {i.amount}\n'
        return products_display
    
    def get_product_info(self, product_name: str) -> tuple:
        for i in range(0, len(self.products)):
            if self.products[i].name == product_name:
                return self.products[i].name, self.products[i].amount


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)
assert s.get_product_info('Ramen') == ('Ramen', 290)







