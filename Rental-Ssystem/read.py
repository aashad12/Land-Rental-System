def read():
    with open("data.txt", 'r') as file:
        kitta_num = 101
        land_data = {}
        for line in file:
            line = line.strip()
            if line:
                land_data[kitta_num] = line.split(',')
                kitta_num += 1
    return land_data


