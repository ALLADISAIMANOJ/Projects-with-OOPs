from src.model.product import Product
from src.model.shoppingcart import ShoppingCart
from src.model.user import Customer
from src.model.order import Order
from src.model.order import CreditCardPayment

def main():
    customer1=Customer("Alladi Sai Manoj", 9963176278, "Hyderabad", 'alladi.saimanoj@gmail.com')
    customer2=Customer("Alladi Sai Priya", 6302115091, "Warangal", "alladisaipriya1206@gmail.com")

    product1=Product("$10","01","Rice")
    product2=Product("$20","02","Wheat")
    product3=Product("$30","03","Barley")
    product4=Product("$40","04","Pulses")
    product5=Product("$50","05","Jower")
    product6=Product("$60","06","Bajra")
    product7=Product("$70","07","Millets")
    product8=Product("$80","08","Corn")
    

    cart1=ShoppingCart(customer1)
    cart1.add_product([product1,product2,product3])

    cart2=ShoppingCart(customer2)
    cart2.add_product(product4)
    cart2.add_product(product5)

    cart1.display_cart_items()

    cart2.display_cart_items()

    cart1.totalcost()

    order=Order(customer1,cart2.totalcost())
    order.set_payment_method(CreditCardPayment())
    order.process_payment()

    



if __name__ == "__main__":
    main()