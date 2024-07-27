import math

from app.customer import Customer
from app.shop import Shop


class Car:
    FUEL_PRICE = 0

    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    @classmethod
    def change_fuel_price(cls, price: float) -> None:
        cls.FUEL_PRICE = price

    def calculate_cost_distance(self, customer: Customer, shop: Shop) -> float:
        sh_cord = (shop.location[0], shop.location[1])
        cu_cord = (customer.location[0], customer.location[1])
        return round((math.sqrt(
            (sh_cord[0] - cu_cord[0]) ** 2 + (sh_cord[1] - cu_cord[1]) ** 2
        ) * 2 * self.fuel_consumption / 100 * Car.FUEL_PRICE), 2)
