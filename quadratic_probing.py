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
    numbers = []
    with open(path, 'r') as file:
        for line in file:
            phone_number = line.strip()
            phone_number = remove_dashes(phone_number)
            numbers.append(int(phone_number))
    return numbers


# Determine if a number is prime for use in hash table size
def is_prime(num):
    if num <= 1:
        return False
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
    return True


# Find hash table size by taking nearest prime number lower than N*1.7
# Ideal hash table size is between 1.3x to 2.0x the size of the data set
def hash_table_size(num):
    if num == 1:
        return 1
    num2 = int(num*1.7)
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
def insert_into_table(table, value):
    key = hash_function(value, len(table))
    i = 0

    while True:
        if table[key] == 'None':  # Insert into hash table if spot is vacant
            table[key] = value
            return True

        else:  # If collision, then probe for vacant location
            i += 1
            key = (key + i**2) % len(table)  # Quadratic probing


# Function to search for index of certain value
def search_in_table(table, value):
    key = hash_function(value, len(table))
    i = 0

    while True:
        if table[key] == value:  # Return value if key location matches
            return key

        elif table[key] == 'None':  # Value does not exist, return false
            return False

        else:  # Probe for correct value
            i += 1
            key = (key + i ** 2) % len(table)  # Quadratic probing


# Function to delete an element from the hash table
def delete_from_table(table, value):
    key = hash_function(value, len(table))
    i = 0

    while True:
        if table[key] == value:  # Replace value with 'None' if key location matches
            table[key] = 'None'
            return True

        elif table[key] == 'None':  # Value does not exist, return false
            return False

        else:  # Value does not match, probe for correct value
            i += 1
            key = (key + i ** 2) % len(table)  # Quadratic probing


# Demo functions:

# Turn phone numbers text file into array of integers
phone_numbers = read_phone_numbers('levi_phone_numbers.txt')

# Initialize 'empty' hash table
hash_table = ['None'] * hash_table_size(len(phone_numbers))

# Insert phone numbers into hash table
for x in range(len(phone_numbers)):
    insert_into_table(hash_table, phone_numbers[x])

# Display filled hash table
print('Hash table created:')
print(hash_table, '\n')

# Search for a specific phone number
print('Search for number:', phone_numbers[8])
location = search_in_table(hash_table, phone_numbers[8])
print('Number is at index:', location, '\n')

# Delete this number from the hash table
print('Delete number:', phone_numbers[8])
print('Original hash table:')
print(hash_table)
delete = delete_from_table(hash_table, phone_numbers[8])
if delete:
    print('Deletion successful!')
    print(hash_table)
else:
    print('Deletion unsuccessful.')
