# Closed Hashing Algorithm

## Linear Probing

To use linear probing implemented in this codebase, you need to create a new instance of the `LinearProbing` class and pass the required `table_size` argument.

```python
from linear_probing import LinearProbing

input_arr = [4, 14, 19, 9004, 33]
hash_table_size = 5 # Also for [ h(K) = K mod hash_table_size ]

# Start with preset input data
linear_probing = LinearProbing(table_size=hash_table_size, input_arr=input_arr)

# Start with empty hash table and insert elements
linear_probing = LinearProbing(table_size=hash_table_size)
linear_probing.insert(4)
linear_probing.insert(14)
linear_probing.insert(19)

# Get the hash table as list
print(linear_probing.get_table())

# Search for an element
print(linear_probing.search(19)) # Returns 2 (position)

# Delete an element
linear_probing.delete(19) # Returns 2 (position)
```

**Optimizing**: To optimize for large hash tables, choose a prime number as the hash table size. This will reduce the number of collisions as prime numbers have the least common factors with the `input_arr` elements.

**Testing**: To test the code, run the following command:

```bash
python linear_probing_unitest.py
```

**Debugging**: To debug the code, create an instance with `debug` argument set to `True`.

```python
linear_probing = LinearProbing(input_arr, hash_table_size, debug=True)
```
