from datetime import datetime, timedelta

class StoreItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class User:
    def __init__(self, username, u_coins, last_purchase_date=None):
        self.username = username
        self.u_coins = u_coins
        self.inventory = []
        if last_purchase_date:
            self.last_purchase_date = datetime.strptime(last_purchase_date, "%Y-%m-%d")
        else:
            self.last_purchase_date = None

    def purchase_item(self, item):
        current_date = datetime.now()
        print(f"Current date: {current_date.strftime('%Y-%m-%d')}")  # Print the present date
        
        # Check if the user has enough U coins and hasn't purchased in the last 30 days
        if self.u_coins >= item.price:
            if self.last_purchase_date is None or (current_date - self.last_purchase_date) >= timedelta(days=30):
                self.u_coins -= item.price
                self.inventory.append(item)
                self.last_purchase_date = current_date
                print(f"Purchased {item.name}.")
                return True
            else:
                days_left = 30 - (current_date - self.last_purchase_date).days
                print(f"You can only purchase items once a month. Please wait {days_left} more days.")
        else:
            print("Not enough U coins.")
        return False

# Example Usage
store_items = [StoreItem("T-Shirt", 50000), StoreItem("Virtual Gift", 30000)]

username = input("Enter username: ")
u_coins = int(input("Enter amount of U coins: "))
last_purchase_date = input("Enter the last purchase date (YYYY-MM-DD) or leave blank if none: ")

if u_coins < 200000:
    print("You need at least 200,000 U coins to purchase items.")
else:
    user = User(username, u_coins, last_purchase_date)

    # Show available items
    print("Available items:")
    for idx, item in enumerate(store_items):
        print(f"{idx + 1}. {item.name} - {item.price} U coins")

    item_choice = int(input("Enter the number of the item you want to purchase: ")) - 1

    if 0 <= item_choice < len(store_items):
        item_to_purchase = store_items[item_choice]

        user.purchase_item(item_to_purchase)
    else:
        print("Invalid choice.")
