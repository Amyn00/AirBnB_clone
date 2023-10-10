# 0x00. AirBnB clone - The console

<img src="https://github.com/Amyn00/AirBnB_clone/blob/master/images/hbnb.png" height="200" width="1000"/>

## Description
The AirBnB Clone project is a simplified replica of the popular vacation rental platform Airbnb. It is designed to demonstrate the functionality of a command-line-based property rental system, where users can create, manage, and book properties.

## Command Interpreter

The command interpreter is a text-based interface that allows users to interact with the AirBnB Clone system. It provides a set of commands to manage properties, users, and bookings. These commands include creating new properties, viewing property details, booking properties, and more.

### How to Start

To start the AirBnB Clone command interpreter, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Amyn00/AirBnB_clone.git
   ```

2. Navigate to the project directory:
   ```bash
   cd AirBnB_clone
   ```

3. Run the commande interpreter:
   ```bash
   ./console.py
   ```

### How to Use
Once the command interpreter is running, you can use various commands to interact with the AirBnB Clone system. Here are some common commands:

* `create`: Create a new property or user.
* `show`: Display details of a property or user.
* `all`: List all properties or users.
* `book`: Book a property for a specific date range.
* `quit` or `exit`: Exit the command interpreter.
For detailed information on available commands and their usage, you can use the help command within the interpreter.

**Examples**
Here are some examples of how to use the AirBnB Clone command interpreter:
1. Creating a new property:
```bash
(hbnb) create Place name="Cozy Cabin" price=150
```
2. Booking a property:
```bash
(hbnb) book Place 1 "2023-11-01" "2023-11-05"
```
3. Listing all properties:
```bash
(hbnb) all Place
```
