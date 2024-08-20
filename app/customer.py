import math
from decimal import Decimal, ROUND_HALF_UP
from typing import Any


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: Decimal,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home_location = location
        self.money = Decimal(str(money))
        self.car = Car(car["brand"], car["fuel_consumption"])

    def arrive_at_shop(self, shop: object) -> str:
        self.location = shop.location
        return f"{self.name} rides to {shop.name}\n"

    def arrive_home(self) -> str:
        self.location = self.home_location
        return f"{self.name} rides home"


class Car:
    FUEL_PRICE = Decimal("0")

    def __init__(self, brand: str, fuel_consumption: Decimal) -> None:
        self.brand = brand
        self.fuel_consumption = Decimal(str(fuel_consumption))

    @classmethod
    def change_fuel_price(cls, price: Decimal) -> None:
        cls.FUEL_PRICE = Decimal(str(price))

    def calculate_cost_distance(
            self,
            customer: Customer,
            shop: Any
    ) -> Decimal:
        sh_cord = (Decimal(shop.location[0]), Decimal(shop.location[1]))
        cu_cord = (
            Decimal(customer.location[0]),
            Decimal(customer.location[1])
        )
        distance = Decimal(math.sqrt(
            (sh_cord[0] - cu_cord[0]) ** 2 + (sh_cord[1] - cu_cord[1]) ** 2
        ))
        cost = distance * 2 * self.fuel_consumption / 100 * Car.FUEL_PRICE
        return cost.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
