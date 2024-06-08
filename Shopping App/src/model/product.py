class Product:
    def __init__(self, price, product_code, name,quantity=0) -> None:
        self.price = price
        self.product_code = product_code
        self.name = name
        self.quantity=quantity
    
    def __str__(self):
        return "Product Details are:\n name: %s\n product_code %s \n price %s\n quantity %s" % (self.name,self.product_code,self.price,self.quantity)
        