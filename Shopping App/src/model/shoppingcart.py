from .user import Customer
from .product import Product

class ShoppingCart:
    def __init__(self, customer=None, products=None):
        self.products = products if products is not None else []
        self.customer = customer if customer is not None else Customer()

    def add_product(self, *products):
        for product in products:
            if isinstance(product, list):
                self.products.extend(product)
            else:
                self.products.append(product)
    
    def delete_product(self, *products):
        for product in products:
            if isinstance(product, list):
                for i in product:
                    self.products.remove(i)
            else:
                self.products.remove(product)

    #display cart items

    def display_cart_items(self):
        if not self.products:
            print("Your cart is empty.")
        else:
            print(f"Items in {self.customer.printname}'s cart:")
            for i, product in enumerate(self.products, start=1):  # Use enumerate with start=1
                print(f"{i}. {product.name}: ${product.price}, Quantity: {product.quantity}")
    

    def totalcost(self):
        total=0
        points_earned=0
        for product in self.products:
            total+=int(product.price[1:])
        print(f'Total cost without discount Upto Now is {total}')
        return total

