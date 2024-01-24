def avg(data):
    totalProducts = len(data["products"])
    totalPrice = 0
    for i in range(totalProducts):
        totalPrice += data["products"][i]["price"]

    return round(totalPrice/totalProducts, 3)


print(avg({
    "products": [
        {
            "name": "Product 1",
            "price": 100
        },
        {
            "name": "Product 2",
            "price": 700
        },
        {
            "name": "Product 3",
            "price": 300
        }
    ]})
)  # print the average price of all products (round to 3 decimal)
