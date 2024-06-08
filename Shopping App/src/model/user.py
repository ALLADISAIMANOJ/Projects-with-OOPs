class Customer:
    def __init__(self,name,phone_number=None,address=None,email=None) -> None:
        self._name=name
        self._phone_number=phone_number
        self._address=address
        self._email=email
        self.__loyalty_points=0
    
    def update_contact_details(self, address=None, phone_number=None, email=None):
        if address:
            self._address = address
        if phone_number:
            self._phone_number = phone_number
        if email:
            self._email = email
    @property
    def loyalty_points(self):
        return self.__loyalty_points

    def add_loyalty_points(self, points):
        if points > 0:
            self.__loyalty_points += points

    # Getter for name
    @property
    def printname(self):
        return self._name

    # Setter for name
    def updatename(self, name):
        self._name = name

    def __str__(self):
        return (f"Customer: {self._name}\n"
                f"Address: {self._address}\n"
                f"Phone: {self._phone_number}\n"
                f"Email: {self._email}\n"
                f"Loyalty Points: {self.__loyalty_points}")

customer = Customer("John Doe", address="123 Main St", phone_number="555-1234", email="john.doe@example.com")
#print(customer)  # Print customer details


