import time
import unittest
from linear_probing import LinearProbing
from random import random


# To run the tests, simply run this file `python linear_probing_unittest.py`

# Time is measured for testing insertion tests

class TestLinearProbing(unittest.TestCase):

    def test_empty_arr(self):
        print(f"\n\nTest {self.id()}")
        table_size = 5
        answer = [None, None, None, None, None]
        # Test
        start_time = time.time()
        hash_table = LinearProbing(table_size=table_size).get_table()
        print("Time taken\t: {:.10f}s".format(time.time() - start_time))
        self.assertEqual(hash_table, answer)

    def test_same_size_arr(self):
        print(f"\n\nTest {self.id()}")
        input_arr = [4, 14, 19, 9004, 33]
        table_size = 5
        answer = [14, 19, 9004, 33, 4]
        # Test
        start_time = time.time()
        hash_table = LinearProbing(
            input_arr=input_arr, table_size=table_size).get_table()
        print("Time taken\t: {:.10f}s".format(time.time() - start_time))
        self.assertEqual(hash_table, answer)

    def test_smaller_arr(self):
        print(f"\n\nTest {self.id()}")
        input_arr = [19, 50, 89, 40]
        table_size = 5
        answer = [50, 89, 40, None, 19]
        # Test
        start_time = time.time()
        hash_table = LinearProbing(
            input_arr=input_arr, table_size=table_size).get_table()
        print("Time taken\t: {:.10f}s".format(time.time() - start_time))
        self.assertEqual(hash_table, answer)

    def test_larger_arr(self):
        print(f"\n\nTest {self.id()}")
        input_arr = [19, 50, 89, 40, 33, 14, 9004, 77]
        table_size = 5
        answer = [50, 89, 40, 33, 19]
        # Test
        start_time = time.time()
        hash_table = LinearProbing(
            input_arr=input_arr, table_size=table_size).get_table()
        print("Time taken\t: {:.10f}s".format(time.time() - start_time))
        self.assertEqual(hash_table, answer)

    def test_inserting_key(self):
        print(f"\n\nTest {self.id()}")
        table_size = 5
        answer = [14, 19, 9004, 33, 4]
        # Test
        start_time = time.time()
        linear_probing = LinearProbing(table_size=table_size)
        linear_probing.insert(4)
        linear_probing.insert(14)
        linear_probing.insert(19)
        linear_probing.insert(9004)
        linear_probing.insert(33)
        hash_table = linear_probing.get_table()
        print("Time taken\t: {:.10f}s".format(time.time() - start_time))
        self.assertEqual(hash_table, answer)

    def test_searching_for_key(self):
        print(f"\n\nTest {self.id()}")
        input_arr = [19, 50, 89, 40, 33, 14, 9004, 77]
        table_size = 5
        linear_probing = LinearProbing(
            input_arr=input_arr, table_size=table_size)
        self.assertEqual(linear_probing.search(19), 4)
        self.assertEqual(linear_probing.search(50), 0)
        self.assertEqual(linear_probing.search(89), 1)
        self.assertEqual(linear_probing.search(40), 2)
        self.assertEqual(linear_probing.search(33), 3)
        self.assertEqual(linear_probing.search(14), -1)
        self.assertEqual(linear_probing.search(9004), -1)
        self.assertEqual(linear_probing.search(77), -1)

    def test_deleting_key(self):
        print(f"\n\nTest {self.id()}")
        input_arr = [19, 50, 89, 40]
        table_size = 5
        linear_probing = LinearProbing(
            input_arr=input_arr, table_size=table_size)
        linear_probing.delete(19)
        linear_probing.delete(50)
        self.assertEqual(linear_probing.search(19), -1)
        self.assertEqual(linear_probing.search(50), -1)
        self.assertEqual(linear_probing.search(89), 1)
        self.assertEqual(linear_probing.search(40), 2)

    """ Testing:
            Best case, Worst case, Average case scenarios
    """
    # Best case scenario

    def test_large_arr_no_collisions(self):
        print(f"\n\nTest {self.id()}")
        input_arr = [x for x in range(10000)]
        table_size = 131071
        answer = input_arr + ([None] * (table_size - 10000))
        # Test
        start_time = time.time()
        hash_table = LinearProbing(
            input_arr=input_arr, table_size=table_size).get_table()
        print("Time taken\t: {:.10f}s".format(time.time() - start_time))
        self.assertEqual(hash_table, answer)

    # Worst case scenario
    # This test will take a long time to run
    # Took
    def test_large_arr_all_collisions(self):
        print(f"\n\nTest {self.id()}")
        input_arr = [5] * (10000)
        table_size = 131071
        answer = ([None] * (5)) + input_arr + \
            ([None] * (table_size - 5 - 10000))
        # Test
        start_time = time.time()
        hash_table = LinearProbing(
            input_arr=input_arr, table_size=table_size).get_table()
        print("Time taken\t: {:.10f}s".format(time.time() - start_time))
        self.assertEqual(hash_table, answer)

    # Average case scenario
    def test_large_arr_some_collisions(self):
        print(f"\n\nTest {self.id()}")
        # Some randoms will round to the same number over 10000 times
        input_arr = [round(random() * 5000) for _ in range(10000)]
        table_size = 131071
        # Test
        start_time = time.time()
        hash_table = LinearProbing(
            input_arr=input_arr, table_size=table_size).get_table()
        print("Time taken\t: {:.10f}s".format(time.time() - start_time))
        # Answer is unknown at runtime, so this is only used for time testing
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
