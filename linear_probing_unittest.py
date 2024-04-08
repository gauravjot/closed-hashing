import time
import unittest
from linear_probing import LinearProbing


class TestLinearProbing(unittest.TestCase):

    def test_same_size_arr(self):
        input_arr = [4, 14, 19, 9004, 33]
        mod_factor = 5
        answer = [14, 19, 9004, 33, 4]
        perform_test(self, input_arr, mod_factor, answer)

    def test_smaller_arr(self):
        input_arr = [19, 50, 89, 40]
        mod_factor = 5
        answer = [50, 89, 40, None, 19]
        perform_test(self, input_arr, mod_factor, answer)


def perform_test(self, input_arr, mod_factor, answer):
    print("\n====================================================")
    print(f"Test: {self.id()}")
    print("----------------------------------------------------\n")

    # not interested in how long it takes to create the object
    linear_probing = LinearProbing(input_arr, mod_factor)
    # track time
    start_time = time.time()
    hash_table = linear_probing.hash()  # measure time taken to hash
    print("Time taken\t: {:.10f}s".format(time.time() - start_time))

    result = False
    if len(hash_table) == len(answer):
        for i in range(len(answer)):
            result = hash_table[i] == answer[i]

    print("Test passed" if result else "Test failed")

    self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
