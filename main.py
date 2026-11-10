
from stack import Stack
from queue import Queue
from linkedlist import LinkedList


# Create objects from our three data structures
customers = LinkedList()
orders = Queue()
history = Stack()


def register_customer():
    print("\n--- Register Customer ---")

    name = input("Enter customer name: ").strip()
    phone = input("Enter phone number: ").strip()

    if not name or not phone:
        print("Name and phone number cannot be empty.")
        return

    if customers.search_customer(name):
        print("A customer with this name already exists.")
        return

    customer = {
        "name": name,
        "phone": phone
    }

    customers.add_customer(customer)

    # Save the registration in the Stack for undo
    history.push(customer)

    print("Customer registered successfully!")


def view_customers():
    print("\n--- Registered Customers ---")

    if customers.size() == 0:
        print("No customers registered yet.")
        return

    customers.display_customers()
    print("Total customers:", customers.size())


def search_customer():
    print("\n--- Search Customer ---")

    name = input("Enter customer name: ").strip()
    customer = customers.search_customer(name)

    if customer:
        print("Customer found:", customer)
    else:
        print("Customer not found.")


def delete_customer():
    print("\n--- Delete Customer ---")

    name = input("Enter customer name: ").strip()

    if customers.delete_customer(name):
        print("Customer deleted successfully!")
    else:
        print("Customer not found.")


def place_order():
    print("\n--- Place Food Order ---")

    name = input("Enter customer's name: ").strip()

    customer = customers.search_customer(name)

    if not customer:
        print("Customer not found. Please register the customer first.")
        return

    food = input("Enter food ordered: ").strip()

    if not food:
        print("Food name cannot be empty.")
        return

    order = {
        "customer": name,
        "food": food
    }

    orders.enqueue(order)

    print("Order added to the kitchen queue!")


def process_order():
    print("\n--- Process Food Order ---")

    order = orders.dequeue()

    if order is None:
        print("There are no orders waiting.")
    else:
        print("Order processed successfully!")
        print("Customer:", order["customer"])
        print("Food:", order["food"])


def view_next_order():
    print("\n--- Next Order ---")

    order = orders.front()

    if order is None:
        print("There are no orders waiting.")
    else:
        print("Customer:", order["customer"])
        print("Food:", order["food"])


def undo_registration():
    print("\n--- Undo Latest Customer Registration ---")

    customer = history.pop()

    if customer is None:
        print("There is no registration to undo.")
        return

    deleted = customers.delete_customer(customer["name"])

    if deleted:
        print("Registration undone for:", customer["name"])
    else:
        print("That customer has already been deleted.")


def main():
    while True:
        print("\n================================")
        print(" RESTAURANT ORDER MANAGEMENT")
        print("================================")
        print("1. Register customer")
        print("2. View all customers")
        print("3. Search customer")
        print("4. Delete customer")
        print("5. Place food order")
        print("6. Process next food order")
        print("7. View next food order")
        print("8. Undo latest customer registration")
        print("9. Exit")

        choice = input("\nEnter your choice (1-9): ").strip()

        if choice == "1":
            register_customer()
        elif choice == "2":
            view_customers()
        elif choice == "3":
            search_customer()
        elif choice == "4":
            delete_customer()
        elif choice == "5":
            place_order()
        elif choice == "6":
            process_order()
        elif choice == "7":
            view_next_order()
        elif choice == "8":
            undo_registration()
        elif choice == "9":
            print("Thank you for using the Restaurant Order Management System!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 9.")


if __name__ == "__main__":
    main()
