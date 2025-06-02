# we should have a parking lot containing parking spots
# we will have different vehicle types Car, bike
# we will have different fees structure like normal and preminum
# we will have different payment option card, cash etc.



class Vehicle:
    def __init__(self, number_plate, type, fee_strategy):
        self.number_plate = number_plate
        self.type = type
        self.fee_strategy = fee_strategy

class VehicleFactory:
    def get_vehicle(self, number_plate, type):
        match type:
            case "car":
                return Vehicle(number_plate, "car")
            case "bike":
                return Vehicle(number_plate, "bike")
            case _:
                raise ValueError("Unknown Vehicle type")

from abc import ABC, abstractmethod   
class FeeStrategy(ABC):
    @abstractmethod
    def get_fees():
        pass

class PremimumFeeStrategy(FeeStrategy):
    def get_fees(duration):
        return duration*15

class NormalFeeStrategy(FeeStrategy):
    def get_fees(duration):
        return duration*10
    

class PaymentStrategy(ABC):
    @abstractmethod
    def make_payment():
        pass

class CashPaymentStraegy(ABC):
    def make_payment():
        print("payment made by cash")


class ParkingSpots:
    def __init__(self, spot_number, occupied, type, vehicle):
        self.spot_number = spot_number
        self.occupied = occupied
        self.type = type
        self.vehicle = vehicle

    def fill_spot(self, vehicle):
        if not self.occupied:
            self.occupied = True
            self.vehicle = vehicle

    def vacate_spot(self):
        self.occupied = False
        self.vehicle = None
       


class CarParkingSpot(ParkingSpots):
    def fill_spot(self, vehicle):
        return super().fill_spot(vehicle)
    
    def vacate_spot(self, spot):
        spot.vacate_spot()
    

class ParkingLot:
    def __init__(self, parking_spots):
        self.parking_spots = parking_spots

    def find_available_spot(self):
        for each_spot in self.parking_spots:
            if not self.parking_spots.occupied:
                return each_spot


    def park_vehicle(self, vehicle):
        available_spot = self.find_available_spot
        available_spot.fill_spot(vehicle)

    def vacate_spot(self, spot):
        spot.vacate_spot()


#main
spot1 = CarParkingSpot("1", False, "Car", None)
spot2 = CarParkingSpot("2", False, "Car", None)

lot = ParkingLot([spot1, spot2])

fee_strategy = PremimumFeeStrategy

car = VehicleFactory.get_vehicle("1234", "car", fee_strategy)
lot.park_vehicle(car)

# get fees
fees = car.fee_strategy.get_fees(2)
payment_st = CashPaymentStraegy.make_payment()
lot.vacate_spot(spot1)

        


