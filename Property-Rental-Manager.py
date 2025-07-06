# Task 1: Menu System and Subroutines

# Dictionary containing property details (original cost and remaining mortgage)
property_data = {
    "B12-3AB": {"Original cost": 153450, "Residual mortgage": 112345},
    "B13-4CD": {"Original cost": 212130, "Residual mortgage": 180234},
    "B14-5GH": {"Original cost": 120100, "Residual mortgage": 85980},
    "B15-6JK": {"Original cost": 135230, "Residual mortgage": 101321},
    "B16-7MO": {"Original cost": 183230, "Residual mortgage": 130234}
}

# Dictionary to store rental income
property_rents = {}

# Dictionary to store repair/maintenance costs
property_operations = {}

# Task 2: Subroutine to input property data
def input_property_data():
    print("\nInsert operation data for properties")
    print("Type 'stop' as Property name when finished.\n")

#Start the loop
    while True:
        # Read and normalize property name
        property_name = input("Enter Property name: ").strip().upper()

        if property_name.lower() == "stop":
            break  # Exit the loop

        # Validate property name
        if property_name not in property_data:
            print("Invalid property name. Please try again.\n")
            continue

        # Read amount (positive for rent, negative for repair)
        try:
            amount = float(input("Insert amount (positive for rent, negative for repairs): "))
        except ValueError:
            print("Invalid amount. Please enter a number (like 750 or -100).\n")
            continue

        # Process rent entry
        if amount > 0:
            if property_name not in property_rents:
                property_rents[property_name] = 0
            property_rents[property_name] += amount
            print(f" Rent of £{amount} added to {property_name}.\n")

        # Process repair entry
        elif amount < 0:
            repair_details = input("Insert repair details: ")
            if property_name not in property_operations:
                property_operations[property_name] = 0
            property_operations[property_name] += abs(amount)
            print(f" Repair cost of £{abs(amount)} added to {property_name}.\n")

        else:
            print("Amount cannot be zero.\n")

# Task 3: Subroutine to display summary report
def summary_data():
    print("\n=== Property Summary ===")

    # Print table headers
    print(f"{'Property#':<10}{'Original':>12}{'Repairs':>10}{'Amended':>12}{'Mortgage':>12}{'Rents':>10}{'Rent %':>10}")

    # Initialize totals
    total_original = 0
    total_repairs = 0
    total_amended = 0
    total_mortgage = 0
    total_rents = 0
    total_rent_percent = 0
    count_properties = 0

    # Process each property
    for prop in property_data:
        original = property_data[prop]["Original cost"]
        mortgage = property_data[prop]["Residual mortgage"]
        repairs = property_operations.get(prop, 0)
        rents = property_rents.get(prop, 0)
        amended = original + repairs

        if mortgage > 0:
            rent_percent = (rents / mortgage) * 100
        else:
            rent_percent = 0

        # Display individual property data
        print(f"{prop:<10}{original:>12,.0f}{repairs:>10,.0f}{amended:>12,.0f}{mortgage:>12,.0f}{rents:>10,.0f}{rent_percent:>9.2f}%")

        # Update totals
        total_original += original
        total_repairs += repairs
        total_amended += amended
        total_mortgage += mortgage
        total_rents += rents
        total_rent_percent += rent_percent
        count_properties += 1

    # Calculate average rent %
    avg_rent_percent = total_rent_percent / count_properties if count_properties else 0

    # Display totals row
    print("-" * 76)
    print(f"{'Total':<10}{total_original:>12,.0f}{total_repairs:>10,.0f}{total_amended:>12,.0f}{total_mortgage:>12,.0f}{total_rents:>10,.0f}{avg_rent_percent:>9.2f}%")
    print()

# Main menu to control user interaction
def main_menu():
    while True:
        print("\nRental Management Menu:")
        print("1. Enter property details")
        print("2. Display summary for rentals")
        print("3. Exit")

        option = input("Insert an option (1-3): ")

        if option == "1":
            input_property_data()
        elif option == "2":
            summary_data()
        elif option == "3":
            print("Program closed. Goodbye!")
            break
        else:
            print("Invalid option. Please insert 1, 2, or 3.")

# Start the program
main_menu()
