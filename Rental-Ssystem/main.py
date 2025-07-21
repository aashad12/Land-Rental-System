from operation import *
from read import *
from write import *
from datetime import datetime

display_welcome()

def land_information():
    try:
        land_data = read()
        land_list = [
            (kitta_number, *land_info)
            for kitta_number, land_info in land_data.items()
        ]
        header = ["Kitta No.", "District", "Direction", "Anna", "Price", "Availability"]
        display_land(land_list, header)
    except Exception as e:
        print("An error occurred in land_information:", str(e))

def rent_land():
    try:
        name = valid_name()
        phone = valid_phone()
        available_land = get_available_land()

        if not available_land:
            print("No land available for rent.")
            return

        land_list = [
            (kitta_number, *land_info)
            for kitta_number, land_info in available_land.items()
        ]
        header = ["Kitta No.", "District", "Direction", "Anna", "Price", "Availability"]
        display_land(land_list, header)

        user_land = []
        grand_total = 0
        rented_kitta_numbers = []

        while True:
            try:
                kitta_number = valid_kitta_number()
                if kitta_number is None:
                    break
                elif kitta_number not in available_land:
                    print("Invalid kitta number or land already rented.")
                    print("\n")
                    continue
                elif kitta_number in rented_kitta_numbers:
                    print("You have already rented this kitta number.\n")
                    continue

                rented_kitta_numbers.append(kitta_number)
                update_availability(kitta_number, "Not Available")

                aana = int(available_land[kitta_number][2])
                per_month_price = int(available_land[kitta_number][3])
                month = valid_month()

                total_price = month * per_month_price
                grand_total += total_price
                user_land.append([kitta_number, aana, month, per_month_price, total_price])

                print("Successfully rented kitta number", kitta_number)
                print("\n")
                
                more = input("Do you want to rent more land? (yes/no): ").lower()
                if more == 'yes':
                    land_information()
                else:
                    break 

            except Exception as e:
                print("An error occurred while processing rental:", str(e))
                print("\n")

        if user_land:
            write_receipt(name, phone, user_land, grand_total)
            terminal_receipt(name, phone, user_land, grand_total)

    except Exception as e:
        print("An error occurred in rent_land:", str(e))

def return_land():
    try:
        name = valid_name()
        phone = valid_phone()
        rented_land = get_rented_land()

        if not rented_land:
            print("No rented land to return.")
            return

        land_list = [
            (kitta_number, *land_info)
            for kitta_number, land_info in rented_land.items()
        ]
        header = ["Kitta No.", "District", "Direction", "Anna", "Price", "Availability"]
        display_land(land_list, header)

        returned_land = []
        grand_total = 0  # Track the total fine for returned land

        while True:
            try:
                kitta_number = valid_kitta_number()
                if kitta_number is None:
                    break
                elif kitta_number not in rented_land:
                    print("Invalid kitta number or land is not rented.\n")
                    continue

                if kitta_number in returned_land:
                    print(f"Kitta number {kitta_number} has already been returned.\n")
                    continue

                # Calculate fine if the land is returned late
                rent_duration = 2  # Replace with your logic to determine rent duration
                price_per_month = int(rented_land[kitta_number][3])
                fine = calculate_fine(rent_duration, price_per_month) # type: ignore

                grand_total += fine  # Add fine to the grand total

                update_availability(kitta_number, "Available")
                returned_land.append(kitta_number)

                print(f"Thank you for returning kitta number {kitta_number}.")

            except Exception as e:
                print("An error occurred while returning land:", str(e))
                break

        # Generate and print the receipt if there are returned lands
        if returned_land:
            write_receipt(name, phone, [], grand_total, fine=grand_total)
            terminal_receipt(name, phone, [], grand_total, fine=grand_total)

    except Exception as e:
        print("An error occurred in return_land:", str(e))
def user_option():
    while True:
        try:
            print("\n1. Press 1 to rent land")
            print("2. Press 2 to return land")
            print("3. Press 3 for land information")
            print("4. Press 4 to exit\n")
    

            user_input = input("Enter your choice: ")

            if user_input == '1':
                rent_land()
            elif user_input == '2':
                return_land()
            elif user_input == '3':
                land_information()
            elif user_input == '4':
                exit_message()
                break
            else:
                print("Invalid option. Please try again.")
        except Exception as e:
            print("An error occurred:", str(e))

user_option()
