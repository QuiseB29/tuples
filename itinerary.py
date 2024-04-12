def item_list(tuple_list):
    for item in tuple_list:
        print("Name:", item[0])
        print("Origin:", item[1])
        print("Destination:", item[2])
        print()
        
        
data = [("Alice", "New York","London"), ("Bob", "Tokyo", "San Francisco")]
item_list(data)