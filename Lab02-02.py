class Product:
    def __init__(self, name,quantity):
        self.name = name
        self.quantity = quantity
        
class Store:
    def __init__(self):
        self.__products = []

    def add_product(self, name, quantity):
        product = Product(name, quantity)
        self.__products.append(product)


    def show_product(self):
        for product in self.__products:
            print(f"Product Name: {product.name}, Quantity: {product.quantity}")


my_srore = Store()
my_srore.add_product("Laotop", 15)
my_srore.add_product("Mouse", 50)
my_srore.show_product()