# Closed Hashing Algorithm (Quadratic Probing) - COMP 359 Assignment 3
# By Levi de Greeff (300171992)
# Assignment Partner: Gauravjot Garaya
# University of the Fraser Valley
# April 9, 2024

# Remove dashes from phone number
def remove_dashes(phone_number):
    return phone_number.replace('-', '')

# Read file with phone numbers
def read_phone_numbers(path):
    phone_numbers = []
    with open(path, 'r') as file:
        for line in file:
            phone_number = line.strip()
            phone_number = remove_dashes(phone_number)
            phone_numbers.append(int(phone_number))
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

# Function to insert value into hash table
# Empty array will be initialized with 'None' for all elements
def insert_into_table(hash_table, value):
    key = hash_function(value, len(hash_table))
    i = 0

    while True:
        if hash_table[key] == 'None': # Insert into hash table if spot is vacant
            hash_table[key] = value
            break;

        else: # If collision, then probe for vacant location
            i += 1
            key = (key + i**2) % len(hash_table) # Quadratic probing

def search_in_table(hash_table, value):
    key = hash_function(value, len(hash_table))
    i = 0

    while True:
        if hash_table[key] == value: # Return value if key location matches
            return key

        else: # If values do not match, probe for correct value
            i += 1
            key = (key + i ** 2) % len(hash_table) # Quadratic probing


phone_numbers = read_phone_numbers('levi_phone_numbers.txt')
hash_table = ['None'] * hash_table_size(len(phone_numbers))
insert_into_table(hash_table, phone_numbers[0])
insert_into_table(hash_table, phone_numbers[1])
print(hash_table)
print(search_in_table(hash_table, 6043454407)) # Should be at index 2
