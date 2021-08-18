"""
Also, the ProductStore class must have the following methods:

add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name). The discount must be specified in percentage
sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error. It also increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
"""


class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


class ProductStore:
    products = []
    
    def add(self, product: object, amount: int) -> None:
        self.products.append(product)
        product.price += 0.3 * product.price
        product.amount = amount
    
    def set_discount(self, identifier, percent, identifier_type='name'):
        for i in range(0, len(self.products)):
            if self.products[i].name == identifier or self.products[i].type == identifier:
                self.products[i].discount = percent
            #else:
                #raise ValueError('No such product in the store.')
            
    
    def sell_product(self, product_name, amount):
        pass
    
    def get_income(self):
        pass

    def get_all_products(self):
        pass
    
    def get_product_info(self, product_name):
        pass


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)

s.set_discount('Food', 10)

# print(p.discount)



print(p.__dict__)
