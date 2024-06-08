from .user import Customer


class Order:
    def __init__(self,customer,total_price) -> None:
        self.customer=customer if customer is not None else Customer()
        self.total_price=total_price
        self.payment_method=None

    def calculate_cgst(self):
        cgst_rate = 0.06  # 6% CGST rate
        return self.total_price * cgst_rate

    def calculate_sgst(self):
        sgst_rate = 0.12  # 6% SGST rate
        return self.total_price * sgst_rate

    def calculate_total_bill(self):
        total_bill = self.total_price + self.calculate_cgst() + self.calculate_sgst()
        return total_bill
    
    def process_payment(self):
        if self.payment_method:
            self.payment_method.make_payment(self.calculate_total_bill())
        else:
            print("No payment method set.")

    def set_payment_method(self, payment_method):
        self.payment_method = payment_method


class PaymentMethod:
    def make_payment(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def make_payment(self, amount):
        print(f"Paid ${amount} using credit card.")

class PayPalPayment(PaymentMethod):
    def make_payment(self, amount):
        print(f"Paid ${amount} using PayPal.")