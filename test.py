import unittest

def find_sum_negative_between_min_max(arr):
    if not arr:
        return 0
    
    max_idx = min_idx = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[max_idx]:
            max_idx = i
        if arr[i] < arr[min_idx]:
            min_idx = i
    
    left = min(max_idx, min_idx)
    right = max(max_idx, min_idx)
    
    sum_neg = 0
    for i in range(left + 1, right):
        if arr[i] < 0:
            sum_neg += arr[i]
    
    return sum_neg


class TestArraySum(unittest.TestCase):
    
    def test_basic_case(self):
        self.assertEqual(find_sum_negative_between_min_max([10, -5, -3, 20]), -8)
    
    def test_no_negative_between(self):
        self.assertEqual(find_sum_negative_between_min_max([5, 1, 2, 10]), 0)
    
    def test_all_negative(self):
        self.assertEqual(find_sum_negative_between_min_max([-1, -5, -3, -10, -2]), -8)
    
    def test_single_element(self):
        self.assertEqual(find_sum_negative_between_min_max([5]), 0)
    
    def test_two_elements(self):
        self.assertEqual(find_sum_negative_between_min_max([10, -5]), 0)
    
    def test_max_before_min(self):
        self.assertEqual(find_sum_negative_between_min_max([20, -1, -2, -5, 5]), -3)
    
    def test_min_before_max(self):
        self.assertEqual(find_sum_negative_between_min_max([-10, 3, 4, 5, 2]), 0)
    
    def test_empty_array(self):
        self.assertEqual(find_sum_negative_between_min_max([]), 0)


if __name__ == "__main__":
    unittest.main()
