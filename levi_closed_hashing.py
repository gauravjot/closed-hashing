# Closed Hashing Algorithm by Levi de Greeff (300171992)
# COMP 359 Assignment 3
# Assignment Partner: Gauravjot Garaya
# University of the Fraser Valley
# April 9, 2024

def remove_dashes(phone_number):
    return phone_number.replace('-', '')

def read_file(path):
    phone_numbers = []
    with open(path, 'r') as file:
        for line in file:
            phone_number = line.strip()
            phone_number = remove_dashes(phone_number)
            phone_numbers.append(phone_number)
    return phone_numbers

phone_numbers = read_file("levi_phone_numbers.txt")

print(phone_numbers)
