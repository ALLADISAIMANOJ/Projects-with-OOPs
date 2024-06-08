from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class Vehicle(ABC):
    def __init__(self, vehicle_id, brand, model, rate_per_day):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rate_per_day = rate_per_day
        self.is_available = True
    
    @abstractmethod
    def get_rate(self, duration):
        pass

class Car(Vehicle):
    def get_rate(self, duration):
        return self.rate_per_day * duration

class Bike(Vehicle):
    def get_rate(self, duration):
        return self.rate_per_day * duration

class Truck(Vehicle):
    def get_rate(self, duration):
        return self.rate_per_day * duration

class Rental:
    def __init__(self, rental_id, user, vehicle, duration):
        self.rental_id = rental_id
        self.user = user
        self.vehicle = vehicle
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(days=duration)
        self.total_cost = vehicle.get_rate(duration)
        self.vehicle.is_available = False

class RentalSystem:
    def __init__(self):
        self.vehicles = {}
        self.rentals = {}
        self.rental_id_counter = 1
    
    def add_vehicle(self, vehicle):
        self.vehicles[vehicle.vehicle_id] = vehicle
    
    def rent_vehicle(self, user, vehicle_id, duration):
        if vehicle_id not in self.vehicles:
            print("Vehicle not found.")
            return None
        vehicle = self.vehicles[vehicle_id]
        if not vehicle.is_available:
            print(f"Vehicle {vehicle_id} is currently unavailable.")
            return None
        rental = Rental(self.rental_id_counter, user, vehicle, duration)
        self.rentals[self.rental_id_counter] = rental
        self.rental_id_counter += 1
        print(f"Vehicle {vehicle_id} rented to {user.name} for {duration} days. Total cost: ${rental.total_cost:.2f}")
        return rental

    def return_vehicle(self, rental_id):
        if rental_id not in self.rentals:
            print("Rental record not found.")
            return False
        rental = self.rentals[rental_id]
        rental.vehicle.is_available = True
        del self.rentals[rental_id]
        print(f"Vehicle {rental.vehicle.vehicle_id} returned by {rental.user.name}.")
        return True

# Example Usage
if __name__ == "__main__":
    rental_system = RentalSystem()
    
    car1 = Car(1, "Toyota", "Camry", 40)
    bike1 = Bike(2, "Yamaha", "YZF-R3", 20)
    truck1 = Truck(3, "Ford", "F-150", 60)
    
    rental_system.add_vehicle(car1)
    rental_system.add_vehicle(bike1)
    rental_system.add_vehicle(truck1)
    
    user1 = User(1, "Alice")
    user2 = User(2, "Bob")
    
    rental1 = rental_system.rent_vehicle(user1, 1, 3)
    rental2 = rental_system.rent_vehicle(user2, 2, 5)
    
    rental_system.return_vehicle(rental1.rental_id)
    rental_system.return_vehicle(rental2.rental_id)
