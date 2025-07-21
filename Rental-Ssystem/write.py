from datetime import datetime

def calculate_fine(rent_duration, price_per_month):
    try:
        today = datetime.now()
        expected_return_date = today.replace(month=today.month + rent_duration)
        fine = 0

       
        if today > expected_return_date:
            fine = price_per_month * 0.10  

        return fine
    
    except Exception as e:
        print("Error calculating fine:", str(e))
        return 0

def write_receipt(name, phone, user_land, grand_total, fine=0):
    """
    Write a receipt for rental or return transactions to a text file.
    """
    try:
        receipt_filename = name.lower() + "_" + phone + ".txt"
        with open(receipt_filename, "w") as file:
            file.write("Technorental Nepal\n")
            file.write("Kathmandu\n")
            file.write("Phone: 9746470346, 9865543253\n")
            file.write("Date: {}\n".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            file.write("Customer: {} ({})\n".format(name, phone))
            file.write("-----------------------------------------------------------------\n")
            file.write("Kitta No.  Anna  Month  Price/Month  Total\n")
            file.write("-----------------------------------------------------------------\n")

            for land in user_land:
                file.write("{:<10} {:<10} {:<10} {:<15} {:<10}\n".format(land[0], land[1], land[2], land[3], land[4]))

            file.write("-----------------------------------------------------------------\n")
            file.write("Grand Total: {}\n".format(grand_total))

            if fine > 0:
                file.write("Fine: {}\n".format(fine))
            
            file.write("Thank you for choosing Technorental Nepal!\n")
    
    except Exception as e:
        print("Error writing receipt:", str(e))

def terminal_receipt(name, phone, user_land, grand_total, fine=0):
    """
    Print the receipt for rental or return transactions to the terminal.
    """
    try:
        print("\t\t--- Technorental Nepal ---")
        print("\t\tDate: {}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        print("\t\tCustomer: {} ({})\n".format(name, phone))
        print("-----------------------------------------------------------------\n")
        print("Kitta No.  Anna  Month \tPrice/Month \tTotal")
        print("-----------------------------------------------------------------\n")

        for land in user_land:
            print("{:<10} {:<10} {:<10} {:<15} {:<10}".format(land[0], land[1], land[2], land[3], land[4]))

        print("-----------------------------------------------------------------\n")
        print("Grand Total: {}".format(grand_total))

        if fine > 0:
            print("Fine: {}\n".format(fine))
        
        print("Thank you for choosing Technorental Nepal!\n")
    
    except Exception as e:
        print("Error printing receipt:", str(e))
