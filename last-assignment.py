def display_catalog(lst):
    print("\nCatalog List:")
    for item in lst:
        print(f"- {item}")

def display_section(section, section_name):
    print(f"\n{section_name}:")
    for item in section:
        print(f"- {item[0]}")  # Format item 

def main():
    catalog1 = (("Laptop", 1000), ("Camera", 500))
    catalog2 = (("Smartphone", 800), ("Tablet", 450))
    
    catalog_list = catalog1 + catalog2
    
    while True:
        print("\n1. View catalog list:")
        print("2. View catalog 1:")
        print("3. View catalog 2:")
        print("4. Exiting")
        choice = input("Enter your choice:")
        
        if choice == "1":
            display_catalog(catalog_list)
        elif choice == "2":
            display_section(catalog1, "Catalog 1")
        elif choice == "3":
            display_section(catalog2, "Catalog 2")
        elif choice == "4":
            print("Exiting")
            break
        else:
            print("Invalid choice, please try again")

main()
