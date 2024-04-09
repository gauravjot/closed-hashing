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
    """ Does linear probing on an integer array.

    Args:
        input_arr (list):   List of integers
        table_size (int):   The size of hash table. Also the mod factor for hash function.
                            Choose a value that you think will best fit the data.

    Usage:
        linear_probing = LinearProbing(input_arr, mod_factor).hash()
    """

    def __init__(self, input_arr, table_size, debug=False) -> None:
        self.DEBUG = debug
        self.input_arr = input_arr
        self.table_size = table_size
        self.table = [None] * table_size
        self.DEL_SYMBOL = chr(0)  # DEL_SYMBOL is used to mark deleted elements

        # Generate hash table
        self._hash()

    def insert(self, key):
        """
        Insert the key into the hash table.
        If the position is occupied, move to next position.

        Args:
            key (int): Key to insert
        """
        pos = self._hash_function(key)
        if self.table[pos] == None:
            self.table[pos] = key
        else:
            if self.DEBUG:
                print(
                    f"Key {key}. Collision at {pos}. Moving to next position.", end=" ")
            start_pos = self._find_next_position(pos)
            if self.DEBUG:
                print(f"Probing at {start_pos}")
            while start_pos != pos:
                # Insert the key if the position is None or DEL_SYMBOL
                if self.table[start_pos] == None or self.table[start_pos] == self.DEL_SYMBOL:
                    self.table[start_pos] = key
                    break
                # otherwise move to next position
                if self.DEBUG:
                    print(
                        f"Key {key}. Collision at {start_pos}. Moving to next position.", end=" ")
                start_pos = self._find_next_position(start_pos)
                if self.DEBUG:
                    print(f"Probing at {start_pos}")
        # Show debug information if debug is True
        if self.DEBUG:
            heading = True if self.table.count(
                None) == self.table_size - 1 else False
            self.print(self.table_size, self.table, show_heading=heading)

    def search(self, key):
        """
        Search for the key in the hash table.
        If the key is not found, return -1.

        Args:
            key (int): Key to search
        """
        pos = self._hash_function(key)
        # If pos in None, return -1
        # Elif pos is the key, return pos
        # Else, probe until we find the key
        if self.table[pos] == None:
            return -1
        elif self.table[pos] == key:
            return pos
        else:
            start_pos = self._find_next_position(pos)
            while start_pos != pos:
                if self.table[start_pos] == key:
                    return start_pos
                start_pos = self._find_next_position(start_pos)
        return -1

    def delete(self, key):
        """
        Delete the key from the hash table.
        If the key is not found, return -1.
        Otherwise return the position.

        Args:
            key (int): Key to delete
        """
        pos = self.search(key)
        # Set the position to None
        if pos != -1:
            # Replace with DEL_SYMBOL for search to work correctly
            self.table[pos] = self.DEL_SYMBOL
        return pos

    def print(self, size=None, hash_table=None, show_heading=True):
        """Helper for debugging. Print the hash table in a friendly format.

        Args:
            size (int): Size of hash table
            hash_table (list): Hash table
            show_heading (bool, optional): Defaults to True. Show heading.
        """
        if hash_table is None:
            hash_table = self.table
            size = self.table_size
        # Format for str.format()
        # Read https://docs.python.org/3/library/string.html#format-specification-mini-language
        row_format = "|{:^6}" * size
        if show_heading:
            print()  # New line
            print(row_format.format(*range(size)), end="|\n")
            print(row_format.format("======", *["======"] * size), end="|\n")
        friendly_hash_table = []
        for x in hash_table:
            if x == self.DEL_SYMBOL:
                friendly_hash_table.append("-")
            elif x is None:
                friendly_hash_table.append("None")
            else:
                friendly_hash_table.append(x)
        print(row_format.format(*friendly_hash_table), end="|\n")

    def get_table(self):
        return self.table

    def _hash(self):
        # Clear the hash table
        self.table = [None] * self.table_size
        # Insert the keys into the hash table
        for key in self.input_arr:
            self.insert(key)

    def _hash_function(self, key):
        return key % self.table_size

    def _find_next_position(self, pos):
        # Cyclic List
        # Go to next position if it is not out-of-bounds; else go to start (0)
        return pos + 1 if pos < self.table_size - 1 else 0


# Quick Testing


if __name__ == "__main__":
    input_arr = [15, 12, 54, 23, 45, 63, 82, 11]
    mod_factor = 7
    linear_probing = LinearProbing(input_arr, mod_factor, debug=True)
    table = linear_probing.get_table()

    # Search for keys
    print(f"\nSearch 23: \t{linear_probing.search(23)}")
    print(f"Search 10: \t{linear_probing.search(10)}\n")

    # Delete key, should return key position
    print(f"Delete 23: \t{linear_probing.delete(23)}")

    # Print the hash table to see deleted key
    linear_probing.print(mod_factor, table)

    # Search for deleted key
    print(f"Search 23: {linear_probing.search(23)}")
