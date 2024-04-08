# Linear Probing: Closed Hashing
# Author: Gauravjot Garaya (300203993)
# Partner: Levi de Greeff

# Things to know about Linear Probing:
# 1. To do linear probing, we need to have a hash table of size [mod]
# 2. We use the hash function to find the index of the key
# 3. If the index is occupied, we move to the next index
# 4. We keep moving until we find an empty index to insert the key

# Input data format: Array of integers

class LinearProbing:
    def __init__(self, input_arr, mod_factor) -> None:
        self.input_arr = input_arr
        self.mod_factor = mod_factor
        self.hash_table = [None] * mod_factor

    def hash(self):
        for key in self.input_arr:
            self._insert(key)
        return self.hash_table

    def _hash_function(self, key):
        return key % self.mod_factor

    def _insert(self, key):
        """
        Insert the key into the hash table.
        If the position is occupied, move to next position.
        """
        pos = self._hash_function(key)
        if self.hash_table[pos] == None:
            self.hash_table[pos] = key
        else:
            # Go to next position if it is not out-of-bounds; else go to start (0)
            start_pos = pos + 1 if pos < self.mod_factor - 1 else 0
            while start_pos != pos:
                # Insert the key if the position is empty
                if self.hash_table[start_pos] == None:
                    self.hash_table[start_pos] = key
                    break
                # otherwise move to next position
                start_pos = start_pos + 1 if start_pos < self.mod_factor - 1 else 0


if __name__ == "__main__":
    input_arr = [15, 12, 54, 23, 45, 63, 82, 11, 14, 4]
    mod_factor = 10
    linear_probing = LinearProbing(input_arr, mod_factor)
    print(linear_probing.hash())
