import random

# Menu
menu = {
    1: {"name": "Cake", "price": 500},
    2: {"name": "Cupcake", "price": 50},
    3: {"name": "Cookies", "price": 30},
    4: {"name": "Brownie", "price": 120},
    5: {"name": "Donut", "price": 80},
    6: {"name": "Muffin", "price": 90},
    7: {"name": "Macaron", "price": 35}
}

cart = {}

# Customer Details
customer_name = ""
customer_mobile = ""
customer_address = ""

# Get Customer Details
def get_customer_details():
    global customer_name, customer_mobile, customer_address

    print("\n--- Enter Customer Details ---")
    customer_name = input("Enter your name: ")

    while True:
        customer_mobile = input("Enter your mobile number: ")
        if len(customer_mobile) == 10 and customer_mobile.isdigit():
            break
        else:
            print("⚠️ Enter valid 10-digit number")

    customer_address = input("Enter your delivery address: ")

# Show Menu
def show_menu():
    print("\n------ MENU ------")
    for key, value in menu.items():
        print(f"{key}. {value['name']} - ₹{value['price']}")

# Place Order
def place_order():
    show_menu()
    
    try:
        item = int(input("Enter item number: "))
        
        if item in menu:
            qty = int(input("Enter quantity: "))
            
            if item in cart:
                cart[item] += qty
            else:
                cart[item] = qty
            
            print("✅ Item added to cart!")
        else:
            print("❌ Invalid item!")
    
    except ValueError:
        print("⚠️ Please enter valid numbers!")

# View Cart
def view_cart():
    print("\n------ YOUR CART ------")
    total = 0
    
    if not cart:
        print("Cart is empty!")
        return
    
    for item, qty in cart.items():
        name = menu[item]["name"]
        price = menu[item]["price"]
        cost = price * qty
        total += cost
        print(f"{name}x{qty} = ₹{cost}")
    
    print("Total =", total)

# Generate Bill
def generate_bill():
    if not cart:
        print("⚠️ Cart is empty!")
        return

    confirm = input("\nConfirm order? (yes/no): ")
    if confirm.lower() != "yes":
        print("❌ Order cancelled!")
        return

    order_id = random.randint(1000, 9999)

    print("\n====== BAKEMART BILL ======")
    print("Order ID:", order_id)
    print("Customer Name:", customer_name)
    print("Mobile:", customer_mobile)
    print("Delivery Address:", customer_address)

    print("\n------ ITEMS ------")
    
    total = 0
    for item, qty in cart.items():
        name = menu[item]["name"]
        price = menu[item]["price"]
        cost = price * qty
        total += cost
        print(f"{name}({price}) x{qty} = ₹{cost}")

    print("\nSubtotal =", total)

    # Discount
    discount = 0
    if total > 1000:
        discount = total * 0.10
        print(f"Discount (10%) = -₹{discount}")

    # GST
    gst = total * 0.05
    print(f"GST (5%) = ₹{gst}")

    # Delivery Charge
    delivery_charge = random.choice([30, 50, 80])
    print(f"Delivery Charge = ₹{delivery_charge}")

    # Final Amount
    final_total = total - discount + gst + delivery_charge
    print("\nFinal Amount =", final_total)

    # Payment Method
    payment = input("\nSelect Payment Method (cash/upi): ")
    if payment.lower() == "upi":
        print("📲 UPI Payment Successful!")
    else:
        print("💵 Cash on Delivery selected")

    # Auto Send Bill
    print(f"\n📱 Bill sent to {customer_mobile} successfully!")

    # Order Tracking
    print("\nOrder Status:")
    print("🧑‍🍳 Preparing your order...")
    print(f"\nHello {customer_name}, your order of  is confirmed!")
    print("🚚 Out for delivery...")
    print("✅ Delivered!")
    print("\n❤️ Thank you for ordering from BakeMart!")

    # 🔥 Clear cart after order
    cart.clear()

# Main Program
while True:
    print("\n====== WELCOME TO BAKEMART======")
    print("1. Enter Customer Details")
    print("2. View Menu")
    print("3. Place Order")
    print("4. View Cart")
    print("5. Generate Bill")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        get_customer_details()
    elif choice == "2":
        show_menu()
    elif choice == "3":
        if customer_name == "" or customer_address == "":
            print("⚠️ Please enter customer details first!")
        else:
            place_order()
    elif choice == "4":
        view_cart()
    elif choice == "5":
        if customer_name == "":
            print("⚠️ Enter customer details first!")
        else:
            generate_bill()
    elif choice == "6":
        print("👋 Exiting... Thank you!")
        break
    else:
        print("❌ Invalid choice!")
