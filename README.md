# Restaurant Order Management System

A modular, menu-driven restaurant management application built with Python, demonstrating the practical implementation and integration of three fundamental data structures: **Stack, Queue, and Singly Linked List**.

This project was developed as part of the SEN 306 – Software Construction coursework at Miva Open University. It demonstrates how fundamental data structures and software construction principles can be applied to a practical business scenario.

## Project Overview

Restaurants handle different types of information and operations every day, including customer records, incoming food orders, and operational activities.

This project explores how these activities can be organised using appropriate data structures.

The Restaurant Order Management System provides a simple terminal-based interface through which a restaurant manager can manage customer records, receive food orders, process orders in their arrival sequence, and undo the most recent customer registration.

Rather than placing all application logic in one file, the project separates each data structure into its own Python module. The main application imports and coordinates these modules.

## Key Features

### 1. Customer Management
Customer records are managed using a Singly Linked List.

The application supports:
- Registering new customers.
- Viewing all registered customers.
- Searching for a customer by name.
- Deleting customer records.
- Counting registered customers.
- Preventing duplicate customer names.

Each customer record contains a name and phone number.

### 2. Food Order Management
Food orders are managed using a Queue.

The application supports:
- Placing food orders for registered customers.
- Adding new orders to the waiting queue.
- Viewing the next order to be processed.
- Processing the oldest waiting order first.
- Checking whether there are orders waiting.

The Queue follows the First In, First Out (FIFO) principle, ensuring that orders are processed in the sequence they are received.

### 3. Undo Functionality
A Stack is used to maintain customer registration history.

Whenever a customer is registered, the registration is recorded in the Stack. When the undo operation is selected, the most recent registration is retrieved and removed from the customer list.

This demonstrates the Last In, First Out (LIFO) principle and the interaction between two different data structures.

The current implementation supports undoing the latest customer registration.

## Data Structures and Their Implementation

| Data Structure | Application | Principle |
|---|---|---|
| Stack | Customer registration history and undo functionality | LIFO |
| Queue | Food order processing | FIFO |
| Singly Linked List | Customer record management | Sequential node linking |

### Stack – `stack.py`

The Stack is implemented using a Python list.

It provides the following methods:

- `push(item)` – Adds an item to the top of the Stack.
- `pop()` – Removes and returns the most recently added item.
- `peek()` – Retrieves the top item without removing it.
- `is_empty()` – Checks whether the Stack is empty.
- `size()` – Returns the number of items in the Stack.

### Queue – `queue.py`

The Queue is implemented using a Python list.

It provides the following methods:

- `enqueue(item)` – Adds an item to the back of the Queue.
- `dequeue()` – Removes and returns the oldest item.
- `front()` – Retrieves the next item without removing it.
- `is_empty()` – Checks whether the Queue is empty.
- `size()` – Returns the number of items in the Queue.

### Singly Linked List – `linkedlist.py`

The Singly Linked List is implemented using two classes: `Node` and `LinkedList`.

Each Node stores customer data and a reference to the next Node. The Linked List maintains a reference to its first Node, known as the head.

It provides the following methods:

- `add_customer(data)` – Adds a customer to the end of the list.
- `display_customers()` – Displays all registered customers.
- `search_customer(name)` – Searches for a customer by name.
- `delete_customer(name)` – Removes a customer from the list.
- `size()` – Counts the registered customers.

## Software Architecture

The application follows a modular structure, separating data structure implementation from application control and user interaction.

```text
restaurant-order-management/
│
├── README.md
├── stack.py
├── queue.py
├── linkedlist.py
├── main.py
└── report.docx
```

**Module responsibilities:**

- `stack.py`: Implements Stack operations and stores customer registration history.
- `queue.py`: Implements Queue operations for managing food orders.
- `linkedlist.py`: Implements the Node and LinkedList classes for customer management.
- `main.py`: Imports the three data structures, provides the terminal menu, handles user input, and coordinates application operations.
- `README.md`: Provides project documentation.
- `report.docx`: Contains the coursework report.

## Software Construction Principles

The project applies the following software construction principles:

**1. Modular Design**

The application is divided into separate modules, with each data structure implemented in its own Python file. This makes the code easier to understand, test, maintain and reuse.

**2. High Cohesion**

Each class and its methods focus on a specific responsibility. For example, the Queue class handles food order operations, while the LinkedList class handles customer record management.

**3. Low Coupling**

The data structures are implemented independently of the main application. The `main.py` file imports their classes and coordinates their use through their public methods, reducing unnecessary dependencies between modules.

**4. Meaningful Naming Conventions**

Descriptive names such as `register_customer()`, `process_order()`, `enqueue()` and `delete_customer()` communicate the purpose of functions and methods clearly.

**5. Readability and Documentation**

The code uses consistent indentation, descriptive names, inline comments and docstrings to make the implementation easier to read and maintain.

## Technologies Used

- **Programming Language:** Python
- **Development Environment:** Visual Studio Code
- **Version Control:** Git
- **Repository Hosting:** GitHub

The application uses Python's built-in capabilities and does not require external packages.

## Getting Started

### Prerequisites

- Python installed on your computer.
- Git installed if you intend to clone the repository.
- A code editor or terminal.

### Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the project directory:

```bash
cd restaurant-order-management
```

### Run the Application

Execute:

```bash
python main.py
```

The application will display a menu containing the available operations.

## How to Use the Application

When the application starts, the user is presented with the following menu:

1. Register customer
2. View all customers
3. Search customer
4. Delete customer
5. Place food order
6. Process next food order
7. View next food order
8. Undo latest customer registration
9. Exit

Select an option by entering its corresponding number and follow the prompts displayed in the terminal.

## Testing and Verification

The application was tested through its individual data structure modules and the integrated main application.

The following operations were verified:

- Adding and removing Stack items.
- Retrieving the most recent Stack item.
- Adding and processing Queue items in FIFO order.
- Adding customer records to the Linked List.
- Displaying and searching customer records.
- Deleting customer records.
- Counting registered customers.
- Undoing the latest customer registration.
- Processing orders until the Queue becomes empty.
- Handling empty customer lists and empty order queues.

## Current Limitations

This is an educational, terminal-based implementation focused on demonstrating data structures and software construction principles.

- Customer records and food orders are stored in memory and are not preserved after the application exits.
- The application does not currently use a database.
- The undo functionality is limited to the most recent customer registration.
- The application does not include a graphical user interface, online ordering, payment processing or user authentication.

## Possible Future Improvements

The project could be extended with:

- Database integration for persistent customer and order records.
- A graphical or web-based user interface.
- More comprehensive order management, including cancellation and order status tracking.
- An expanded undo and activity history system.
- Customer identification using unique customer IDs rather than names.
- Input validation and more comprehensive automated tests.

## Author

**Amina Oyegoke**

Software Engineering Student | Miva Open University

**Project:** SEN 306 – Software Construction
