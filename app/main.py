import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        json_data = json.load(file)
    Car.change_fuel_price(json_data["FUEL_PRICE"])
    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"]
        )
        for customer in json_data["customers"]
    ]
    shops = []
    for shop in json_data["shops"]:
        shops.append(
            Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            )
        )
    for customer in customers:
        purchase_flag = False
        print(f"{customer.name} has {customer.money} dollars")
        min_cost = 0
        shop_index = 0
        for index, shop in enumerate(shops):
            all_cost = (
                customer.car.calculate_cost_distance(customer, shop)
                + shop.calculate_purchase(customer)
            )
            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {all_cost}"
            )
            if min_cost == 0:
                min_cost = all_cost
                shop_index = index
            if all_cost < min_cost:
                min_cost = all_cost
                shop_index = index
        if min_cost <= customer.money:
            purchase_flag = True
        if purchase_flag:
            print(customer.arrive_at_shop(shops[shop_index]))
            print(shops[shop_index].fulfilled_purchase(customer))
            print(customer.arrive_home())
            print(f"{customer.name} now "
                  f"has {round(customer.money - min_cost, 2)} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money to make"
                  f" a purchase in any shop")
