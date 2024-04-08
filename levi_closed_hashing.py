# Closed Hashing Algorithm (Quadratic Probing) - COMP 359 Assignment 3
# By Levi de Greeff (300171992)
# Assignment Partner: Gauravjot Garaya
# University of the Fraser Valley
# April 9, 2024

# Remove dashes from phone number
def remove_dashes(phone_number):
    return phone_number.replace('-', '')

# Read file with phone numbers
def read_file(path):
    phone_numbers = []
    with open(path, 'r') as file:
        for line in file:
            phone_number = line.strip()
            phone_number = remove_dashes(phone_number)
            phone_numbers.append(phone_number)
    return phone_numbers

# Determine if a number is prime for use in hash table size
def is_prime(num):
    if num <= 1:
        return False;
    elif num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False
    return True

# Find hash table size by taking nearest prime number lower than N*1.7
# Ideal hash table size is between 1.3x to 2.0x the size of the data set
def hash_table_size(num):
    if num == 1:
        return 1
    num2 = int (num*1.7)
    lower = num2 - 1
    while True:
        if is_prime(lower):
            return lower
        lower -= 1

# Hash function, returns key % table size to determine the index
def hash_function(value, table_size):
    return value % table_size

