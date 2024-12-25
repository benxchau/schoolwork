def railway_ticket_system():
    destinations = {
        "London": 10.15,
        "Manchester": 22.50,
        "Birmingham": 21.40
    }

    while True:
        print("Welcome to the Railway Ticket Booking System!")
        while True:
            name = input("What is your name? ").strip()
            if name:
                break
            else:
                print("Name cannot be empty. Please enter your name.")

        print("\nDestinations and Prices:")
        for destination, price in destinations.items():
            print(f"{destination} - £{price:.2f}")

        while True:
            try:
                num_tickets = int(input("How many tickets would you like to purchase? "))
                if num_tickets > 0:
                    break
                else:
                    print("Please enter a number greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a number")

        total_price = destinations[destination] * num_tickets

        print("\nTransaction Summary:")
        print(f"Name: {name}")
        print(f"Destination: {destination}")
        print(f"Number of Tickets: {num_tickets}")
        print(f"Total Price: £{total_price:.2f}")

        while True:
            print_receipt = input("\nWould you like to print your receipt? (yes/no): ").lower().strip()
            if print_receipt in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please answer 'yes' or 'no'.")

        if print_receipt == 'yes':
            print("\nReceipt:")
            print("=========================")
            print(f"Name: {name}")
            print(f"Destination: {destination}")
            print(f"Number of Tickets: {num_tickets}")
            print(f"Total Price: £{total_price:.2f}")
            print("=========================")
            print("Thank you for your purchase!")
        else:
            print("\nThank you for your purchase!")

        while True:
            another_transaction = input("\nWould you like to purchase another ticket? (yes/no): ").lower().strip()
            if another_transaction in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please answer 'yes' or 'no'.")

        if another_transaction == 'no':
            print("\nThank you for using the Railway Ticket Booking System")
            break

# Run the system
railway_ticket_system()
