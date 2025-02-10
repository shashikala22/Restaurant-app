class RestaurantApp:
    def __init__(self):
        self.menu = {
            "1. Pizza": 800,
            "2. Burger": 500,
            "3. Pasta": 600,
            "4. Fries": 300,
            "5. Soft Drink": 150,
            "6. Ice Cream": 200,
            "7. Coffee": 100,
            "8. Tea": 50
        }
        self.order = {}

    def show_menu(self):
        print("\nMenu:")
        for item, price in self.menu.items():
            print(f"{item}: Rs {price}")

    def take_order(self):
        self.show_menu()
        print("\nEnter the number of the item to order. Type 'done' when finished.")

        while True:
            item_number = input("Item Number: ").strip()
            if item_number.lower() == "done":
                break
            
            item_key = next((key for key in self.menu if key.startswith(item_number + ".")), None)
            
            if item_key:
                try:
                    quantity = int(input(f"Enter the quantity for {item_key}: "))
                    if quantity <= 0:
                        print("Quantity should be greater than 0.")
                        continue
                    
                    if item_key in self.order:
                        self.order[item_key] += quantity
                    else:
                        self.order[item_key] = quantity
                    
                    print(f"Added {quantity} X {item_key} to the order.")
                except ValueError:
                    print("Please enter a valid quantity.")
            else:
                print("Item not found in the menu. Please try again.")

    def view_bill(self):
        if not self.order:
            print("\nNo items ordered yet.")
            return
        
        print("\nYour Bill:")
        total = 0
        for item, quantity in self.order.items():
            price = self.menu[item] * quantity
            print(f"{item} X {quantity}: Rs {price}")
            total += price
        
        print(f"Total Amount: Rs {total}")
        self.process_payment(total)

    def process_payment(self, total):
        print("\nSelect Payment Method:")
        print("1. Cash")
        print("2. Credit/Debit Card")
        print("3. UPI")
        
        while True:
            payment_choice = input("Enter your payment choice: ").strip()
            if payment_choice in ["1", "2", "3"]:
                print("Payment Successful. Thank you for your order!")
                break
            else:
                print("Invalid choice. Please select a valid payment method.")

    def run(self):
        while True:
            print("\n--- Welcome to the Shashi Restaurant App ---")
            print("1. Show Menu")
            print("2. Place Order")
            print("3. View Bill and Pay")
            print("4. Exit")
            
            choice = input("Choose an option: ").strip()
            
            if choice == "1":
                self.show_menu()
            elif choice == "2":
                self.take_order()
            elif choice == "3":
                self.view_bill()
            elif choice == "4":
                print("Thank you for visiting. Have a GreatDay!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    app = RestaurantApp()
    app.run()
