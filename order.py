import random

# 全局菜单配置
MENU_CATEGORIES = {
    "Main Meals": ["burger", "cheeseburger", "chicken_wrap"],
    "Snacks & Sides": ["fries", "nuggets", "onion_rings"],
    "Drinks": ["soda", "coffee", "milkshake", "water"],
    "Desserts": ["ice_cream", "apple_pie", "sundae"]
}

MENU_PRICES = {
    # Main Meals
    "burger": 5.99,
    "cheeseburger": 6.49,
    "chicken_wrap": 6.99,
    # Snacks & Sides
    "fries": 2.49,
    "nuggets": 3.99,
    "onion_rings": 2.99,
    # Drinks
    "soda": 1.99,
    "coffee": 2.29,
    "milkshake": 3.49,
    "water": 0.99,
    # Desserts
    "ice_cream": 2.49,
    "apple_pie": 2.99,
    "sundae": 3.29
}

def show_welcome_banner():
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║                                                            ║
    ║              🍔 Welcome to Axelrod's Burger 🍔             ║
    ║                                                            ║
    ║              🎉 Delicious Food at Your Fingertips 🎉       ║
    ║                                                            ║
    ╚════════════════════════════════════════════════════════════╝
    """)

def select_dining_option():
    while True:
        print("\nPlease select dining option:")
        print("1. Dine In (Have Here)")
        print("2. Take Away")
        choice = input("Enter your choice (1/2): ").strip()
        if choice == "1":
            return "Dine In"
        elif choice == "2":
            return "Take Away"
        else:
            print("Invalid option, please try again!")

def show_help():
    print("AVAILABLE COMMANDS:")
    print("MENU                          Show available items")
    print("ADD <number> <quantity>       Add an item to the order (use item number)")
    print("UPDATE <index> <quantity>     Update quantity of an existing item")
    print("REMOVE <index>                Remove an item from the order")
    print("PRINT                         Show current order")
    print("CHECKOUT                      Finalize the order and show total")
    print("HELP                          Show this help menu")
    print("EXIT                          Exit the system")

def show_menu():
    print("========= 🧾 MENU =========")
    item_number = 1
    menu_items = {}  # 用于存储编号和产品的映射
    for category, items in MENU_CATEGORIES.items():
        print(f"\n--- {category} ---")
        for item in items:
            if item in MENU_PRICES:
                print(f"{item_number}. {item.replace('_', ' ').title():20} ${MENU_PRICES[item]:.2f}")
                menu_items[item_number] = item
                item_number += 1
    print("\n==========================")
    return menu_items

def print_order(order):
    if not order:
        print("Your order is empty!")
    else:
        print("----- CURRENT ORDER -----")
        print("Item                    Quantity    Price    Subtotal")
        print("--------------------------------------------------------")
        total = 0
        for idx, (item, quantity) in enumerate(order.items(), 1):
            price = MENU_PRICES[item]
            subtotal = price * quantity
            total += subtotal
            print(f"{idx}. {item.replace('_', ' ').title():<20} {quantity:^8} ${price:>6.2f} ${subtotal:>8.2f}")
        print("--------------------------------------------------------")
        print(f"Total: {'':<35} ${total:>8.2f}")
        print("-------------------------")

def calculate_total(order):
    total = sum(MENU_PRICES[item] * quantity for item, quantity in order.items())
    return total

def show_command_menu():
    print("\n=== Available Commands ===")
    print("┌─────────────────────────────────────────────┐")
    print("│ 1. MENU     - Show available menu items     │")
    print("│ 2. ADD      - Add item to order             │")
    print("│ 3. UPDATE   - Update item quantity          │")
    print("│ 4. REMOVE   - Remove item from order        │")
    print("│ 5. PRINT    - Show current order            │")
    print("│ 6. CHECKOUT - Complete order and show total │")
    print("│ 7. HELP     - Show detailed help menu       │")
    print("│ 8. EXIT     - Exit the system               │")
    print("└─────────────────────────────────────────────┘")

def get_command_input():
    while True:
        try:
            choice = int(input("\nEnter command number (1-8): ").strip())
            if 1 <= choice <= 8:
                return choice
            else:
                print("Please enter a number between 1 and 8!")
        except ValueError:
            print("Please enter a valid number!")

def generate_order_number():
    return random.randint(100, 999)

def select_payment_method():
    while True:
        print("\nSelect payment method:")
        print("1. Cash")
        print("2. Card")
        try:
            choice = int(input("Enter payment method (1-2): ").strip())
            if choice == 1:
                return "Cash"
            elif choice == 2:
                return "Card"
            else:
                print("Please enter 1 or 2!")
        except ValueError:
            print("Please enter a valid number!")

def process_checkout(order, dining_option):
    if not order:
        print("Your order is empty!")
        return
    
    print_order(order)
    payment_method = select_payment_method()
    order_number = generate_order_number()
    
    print("\n" + "="*50)
    print("           🎉 Order Successful! 🎉")
    print("="*50)
    print(f"Order Number: #{order_number}")
    print(f"Dining Option: {dining_option}")
    print(f"Payment Method: {payment_method}")
    print("="*50)
    print("Thank you for your order!")
    print("Please keep your order number for reference.")
    print("="*50 + "\n")
    
    order.clear()

def main():
    show_welcome_banner()
    dining_option = select_dining_option()
    print(f"\nYou selected: {dining_option}")
    print("Welcome to the Order System!\n")
    
    order = {}

    while True:
        show_command_menu()
        choice = get_command_input()

        if choice == 1:  # MENU
            menu_items = show_menu()

        elif choice == 2:  # ADD
            menu_items = show_menu()
            try:
                item_number = int(input("Enter item number: ").strip())
                if item_number not in menu_items:
                    print("Invalid item number!")
                    continue
                    
                item = menu_items[item_number]
                quantity = int(input("Enter quantity: ").strip())
                
                if quantity <= 0:
                    print("Quantity must be positive!")
                elif item in order:
                    order[item] += quantity
                    print(f"Updated: {item.replace('_', ' ').title()} x{order[item]}")
                else:
                    order[item] = quantity
                    print(f"Added: {item.replace('_', ' ').title()} x{quantity}")
            except ValueError:
                print("Please enter valid numbers!")

        elif choice == 3:  # UPDATE
            if not order:
                print("Your order is empty!")
            else:
                print_order(order)
                try:
                    index = int(input("Enter item number to update: ").strip())
                    quantity = int(input("Enter new quantity: ").strip())
                    if index < 1 or index > len(order):
                        print("Invalid item number!")
                    elif quantity <= 0:
                        print("Quantity must be positive!")
                    else:
                        item = list(order.keys())[index - 1]
                        order[item] = quantity
                        print(f"Updated: {item.replace('_', ' ').title()} x{quantity}")
                except:
                    print("Invalid input format!")

        elif choice == 4:  # REMOVE
            if not order:
                print("Your order is empty!")
            else:
                print_order(order)
                try:
                    index = int(input("Enter item number to remove: ").strip())
                    if index < 1 or index > len(order):
                        print("Invalid item number!")
                    else:
                        item = list(order.keys())[index - 1]
                        del order[item]
                        print(f"Removed: {item.replace('_', ' ').title()}")
                except:
                    print("Invalid input format!")

        elif choice == 5:  # PRINT
            print_order(order)

        elif choice == 6:  # CHECKOUT
            process_checkout(order, dining_option)

        elif choice == 7:  # HELP
            show_help()

        elif choice == 8:  # EXIT
            print("Exiting Order System.")
            break

        print("")

if __name__ == "__main__":
    main()
