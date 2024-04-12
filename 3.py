def iterate_orders(orders):
    for order in orders:
        name, item, quantity = order
        print(f"Name:{name}, Item:{item}, Quantity:{quantity}")
        
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Kim", "TV", 3),
    ("Timmy", "Soundbar", 4),
]

iterate_orders(orders)



