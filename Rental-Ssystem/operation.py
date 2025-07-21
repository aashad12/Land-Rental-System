from read import *
from datetime import datetime

def display_welcome():
    print("\n\t\t\tWelcome to Technorental Service\n")
    print("\t\t\tPhone number:9746470346,9865543253\n")
    print("\t\t\t\tAddress : Kathandu\n")
    print("-"*80)
    print("Choose from the option given below: ")
    print("-"*80)

def update_availability(kitta_number, status):
    land_data = read()
    if kitta_number in land_data:
        land_data[kitta_number][-1] = status
        with open("data.txt", 'w') as file:
            for key, values in land_data.items():
                file.write(",".join(values) + "\n")
    else:
        raise ValueError("Invalid kitta number.")

def get_available_land():
    land_data = read()

    available_land = {}
    for kitta_number, land_info in land_data.items():
        if land_info[-1].strip().lower() == "available": 
            available_land[kitta_number] = land_info 

    return available_land

def get_rented_land():
    land_data = read()

    rented_land = {}
    for kitta_number, land_info in land_data.items():
        if land_info[-1].strip().lower() == "not available":
            rented_land[kitta_number] = land_info

    return rented_land

def display_land(land_list, header):
    column_widths = [max(len(str(item)) for item in col) + 2 for col in zip(header, *land_list)]
    table_width = sum(column_widths) + len(column_widths) - 1

    def format_row(row):
        formatted_row = " "
        for item, width in zip(row, column_widths):
            formatted_row += " " + str(item).ljust(width)
        return formatted_row

    print("-" * table_width+ "-" * 10)
    print(format_row(header))
    print("-" * table_width+ "-" * 10)

    for land in land_list:
        print(format_row(land))

    print("-" * table_width + "-" * 10)

def valid_name():
    while True:
        user_name = input("Please enter your name: ")
        try:
            int(user_name)
            print("Invalid name. Please try again.")
        except ValueError:
            return user_name 

def valid_phone():
    while True:
        user_phone = input("Please enter your phone number: ")
        try:
            int(user_phone)
            return user_phone
        except ValueError:
            print("Invalid phone number. Please try again.")

def valid_month():
    while True:
        try:
            month = int(input("Enter the number of months to rent: "))
            return month
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def valid_kitta_number():
    land_data = read()
    while True:
        try:
            user_input = input("Enter the kitta number to (rent or return) or '1' to quit: ")
            if user_input == "1":
                return None
            kitta_number = int(user_input)
            if kitta_number in land_data:
                return kitta_number
            else:
                print("Invalid kitta number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def exit_message():
    print("\n")
    print("Thank you for using our system. Have a good day!")
    print("\n")
