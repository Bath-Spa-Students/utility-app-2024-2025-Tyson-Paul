# Importing the pyfiglet module which allows to generate ASCII art text from strings
import pyfiglet

class VendingMachine:
    def __init__(self):
        # To define the menu as a dictionary where each item is identified by a unique code 
        # like item name, price, stock quantity, and category
        self.menu = {
            "A1": {"item": "Lays Chips", "price": 1.50, "stock": 7, "category": "Snacks"},
            "A2": {"item": "Oreo Cookies", "price": 2.75, "stock": 5, "category": "Snacks"},
            "A3": {"item": "KitKat", "price": 1.50, "stock": 8, "category": "Snacks"},
            "A4": {"item": "Cheetos Chips", "price": 3.70, "stock": 5, "category": "Snacks"},
            "A5": {"item": "Mcvities Biscuits", "price": 4.00, "stock": 9, "category": "Snacks"},
            "A6": {"item": "Cadbury Dairy Milk", "price": 2.50, "stock": 6, "category": "Snacks"},
            "A7": {"item": "M&M Chocolate", "price": 2.75, "stock": 5, "category": "Snacks"},
            "B1": {"item": "Coco Cola", "price": 2.50, "stock": 8, "category": "Drinks"},
            "B2": {"item": "Sparkling Water", "price": 1.25, "stock": 10, "category": "Drinks"},
            "B3": {"item": "Melco Mango Juice", "price": 1.50, "stock": 7, "category": "Drinks"},
            "B4": {"item": "Pepsi", "price": 2.50, "stock": 9, "category": "Drinks"},
            "B5": {"item": "Cold Coffee", "price": 4.50, "stock": 8, "category": "Drinks"},
            "B6": {"item": "Red Bull", "price": 5.00, "stock": 6, "category": "Drinks"},
            "B7": {"item": "Water", "price": 1.0, "stock": 6, "category": "Drinks"},
        }

    def display_welcome_message(self):
        # To display the "Welcome" message in large text using pyfiglet
        welcome_message = pyfiglet.figlet_format("Welcome to Ty's Vending Machine", font="cybermedium")
        print(welcome_message)

    def display_menu(self, show_welcome=True):
        # It shows welcome message if specified
        if show_welcome:
            self.display_welcome_message()
        
        # To organize items by category
        categories = {"Snacks": [], "Drinks": []}
        for item_id, details in self.menu.items():
            categories[details["category"]].append(item_id)
        
        # To display menu by category (Snacks or Drinks)
        print("\nMENU:")
        print("-" * 60)
        for category, items in categories.items():
            print(f"{category}:")
            print(f"{'ID':<5} {'Item':<20} {'Price (AED)':<15} {'Stock Left'}")
            print("-" * 60)
            for item_id in items:
                details = self.menu[item_id]
                print(f"{item_id:<5} {details['item']:<20} {details['price']:<15.2f} {details['stock']}")
            print("-" * 60)

    def process_purchase(self, item_id, payment):
        # To check if the item_id exists in the vending machine menu
        if item_id in self.menu:
            item = self.menu[item_id]

            # To check if the item is in stock or not 
            if item["stock"] > 0:
                # Confirming the item to the user before proceeding
                print(f"You have selected: {item['item']} for {item['price']:.2f} AED.")
                confirm = input("Do you want to proceed with the payment? (yes/no): ").strip().lower()

                # If the user cancels the purchase, it will exit the function
                if confirm != "yes":
                    print("Purchase cancelled.")
                    print("-" * 60)
                    return

                # To Check if the user has provided enough payment
                while payment < item["price"]:
                    balance_needed = item["price"] - payment
                    print(f"Insufficient funds. Please insert {balance_needed:.2f} AED more.")
                    # If user provides insufficient funds then it will ask to enter additional funds
                    payment += float(input("Enter additional funds: AED "))

                change = payment - item["price"]

                # To decrease stock of the item by 1 after user buys it
                self.menu[item_id]["stock"] -= 1

                # To display purchase success message and any change due
                print(f"Thank you for purchasing {item['item']}!")
                if change > 0:
                    print(f"Your change is {change:.2f} AED.")
                else:
                    print("Exact amount received. No change.")
                print("-" * 60)
            else:
                # To notify if the item is out of stock
                print(f"Sorry, {item['item']} is out of stock.")
                print("-" * 60)
        else:
            print("Invalid selection. Please choose a valid item.")
            print("-" * 60)

    def run(self):
         # Ti start a loop to repeatedly show the menu and process purchases
        while True:
            self.display_menu(show_welcome=True)
            try:
                item_id = input("\nEnter the item ID to purchase (or 0 to exit): ").strip().upper()

                # It exits if the user chooses '0'
                if item_id == "0":
                    print("Thank you for using Ty's Vending Machine. Goodbye!")
                    print("-" * 60)
                    break
                
                 # If the item_id is not valid, it inform the user
                if item_id not in self.menu:
                    print("Invalid item ID. Please choose a valid item ID.")
                    print("-" * 60)
                    continue
                
                 # To prompt the user for payment
                payment = float(input(f"Enter payment for item ID {item_id}: AED "))
                self.process_purchase(item_id, payment)

                # To ask if the user wants to make another purchase or not
                continue_purchase = input("Would you like to make another purchase? (yes/no): ").strip().lower()
                if continue_purchase != "yes":
                    print("Thank you for using Ty's Vending Machine. Goodbye!")
                    print("-" * 60)
                    break
            except ValueError:
                # Handles invalid numeric input
                print("Invalid input. Please enter numeric values.")
                print("-" * 60)

# Create a vending machine instance and run it
# The vending_machine.run() method will likely start the vending machine's operations
vending_machine = VendingMachine()
vending_machine.run()