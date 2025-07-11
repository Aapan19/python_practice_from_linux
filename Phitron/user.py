from abc import ABC, abstractmethod
from datetime import datetime

class User(ABC):
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email
        # to do --> set user id dynamically
        self.__id = 0
        self.__nid = nid
        self.wallet = 0

    @abstractmethod
    def display_profile(self):
        self.current_ride = None
        raise NotImplementedError
    
class Rider(User):
    def __init__(self, name, email, nid, current_location):
        self.current_ride = None
        self.wallet = 0
        self.current_location = current_location
        super().__init__(name, email, nid)

    def display_profile(self):
        print(f'Rider: With name: {self.name} and email: {self.email}')

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount

    def update_location(self, current_location):
        self.current_location = current_location

    def request_rider(self, location, destination):
        if not self.current_ride:
            # to do --> set ride properly  # Done
            # to do --> set current ride via ride match  # Done
            ride_request = Ride_request(self, destination)
            ride_matcher = Ride_matching()
            self.current_ride = ride_matcher.find_driver(ride_request)

class Driver(User):
    def __init__(self, name, email, nid, current_location):
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = 0

    def display_profile(self):
        print(f'Driver: With name: {self.name} and email: {self.email}')

    def accept_ride(self, ride):
        ride.set_driver(self)

class Ride:
    def __init__(self, start_location, end_location):
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None

    def set_driver(self,driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self, rider, amount):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

class Ride_request:
    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location = end_location

class Ride_matching:
    def __init__(self):
        self.aavailable_drivers = []

    def find_driver(self, ride_request):
        if self.aavailable_drivers > 0:
            # to do --> find the closest driver of the rider
            driver = self.aavailable_drivers[0]
            ride = Ride(ride_request.rider.current_location, ride_request.end_location)
            driver.accept_ride(ride)
            return ride