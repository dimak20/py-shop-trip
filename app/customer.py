class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int | float,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home_location = location
        self.money = money
        from app.car import Car
        self.car = Car(car["brand"], car["fuel_consumption"])

    def arrive_at_shop(self, shop: object) -> str:
        self.location = shop.location
        return f"{self.name} rides to {shop.name}\n"

    def arrive_home(self) -> str:
        self.location = self.home_location
        return f"{self.name} rides home"
