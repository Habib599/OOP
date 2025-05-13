
class Product():
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
class Shop():
    def __init__(self):
        self.products=[]

    def add_product(self,product):
        self.products.append(product)
        print(f'{product.name} added to the shop.')
        
        
    def buy_product(self,product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print('Congreate! you successfully bought', product_name)
                return
        print('sorry! this product not avaiable')
        

my_shop = Shop()

# product make
p1 = Product("Apple", 1.2)
p2 = Product("Banana", 0.5)
p3 = Product("Orange", 0.8)

#add product
my_shop.add_product(p1)
my_shop.add_product(p2)
my_shop.add_product(p3)

#product buy
my_shop.buy_product("Banana")   # Success
my_shop.buy_product("Mango")    # Not available