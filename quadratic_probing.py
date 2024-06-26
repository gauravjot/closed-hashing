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
            print('Insertion successful at index', str(key)+'!')
            return True

        elif table[key] == 'Delete_Value':  # Insert into hash table in previously deleted space
            table[key] = value
            print('Insertion successful at index', str(key) + '!')
            return True

        else:  # If collision, then probe for vacant location
            failed_key = key
            i += 1
            key = (key + i**2) % len(table)  # Quadratic probing
            print('Insertion at index', failed_key, 'failed. Probe to index', key)


# Function to search for index of certain value
def search_in_table(table, value):
    key = hash_function(value, len(table))
    i = 0

    while True:
        if table[key] == value:  # Return value if key location matches
            print('Search successful!')
            return key

        elif table[key] == 'None':  # Value does not exist, return false
            print('Search unsuccessful, value does not exist.')
            return False

        else:  # Probe for correct value
            failed_key = key
            i += 1
            key = (key + i ** 2) % len(table)  # Quadratic probing
            print('Value does not match at index', str(failed_key) + ', probing to index', key)


# Function to delete an element from the hash table
def delete_from_table(table, value):
    key = hash_function(value, len(table))
    i = 0

    while True:
        if table[key] == value:  # Replace value with 'Delete_Value' if key location matches
            table[key] = 'Delete_Value'
            print('Deletion successful at index', str(key) + '!')
            return True

        elif table[key] == 'None':  # Value does not exist, return false
            print('Deletion unsuccessful, value does not exist.')
            return False

        else:  # Value does not match, probe for correct value
            failed_key = key
            i += 1
            key = (key + i ** 2) % len(table)  # Quadratic probing
            print('Value does not match at index', str(failed_key) + ', probing to index', key)


# Demo functions:

# Turn phone numbers text file into array of integers
phone_numbers = read_phone_numbers('levi_phone_numbers.txt')

# Initialize 'empty' hash table
hash_table = ['None'] * hash_table_size(len(phone_numbers))
print('Hash table size:', len(hash_table))
print('------------------------------------------------------------------------------------\n')

# Insert phone numbers into hash table
for x in range(len(phone_numbers)):
    print('Inserting value:', phone_numbers[x])
    insert_into_table(hash_table, phone_numbers[x])
    print(hash_table, '\n')

print('------------------------------------------------------------------------------------\n')

# Search for a specific phone number
print('Search for number:', phone_numbers[2])
location = search_in_table(hash_table, phone_numbers[2])
print('Number is at index:', location, '\n')

# Search for a number that does not exist in table
print('Search for number: 1234567890')
location = search_in_table(hash_table, 1234567890)
print('Number is at index:', location)
print('------------------------------------------------------------------------------------\n')

# Delete this number from the hash table
print('Delete number:', phone_numbers[3])
print('Original hash table:')
print(hash_table)
delete_from_table(hash_table, phone_numbers[3])
print(hash_table, '\n')

# Try to delete number that does not exist
print('Delete number: 1234567890')
print('Original hash table:')
print(hash_table)
delete_from_table(hash_table, 1234567890)
