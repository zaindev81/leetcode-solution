from typing import List

# https://leetcode.com/problems/two-sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a hash map to store number -> index mapping
        num_to_index = {}

        for i, num in enumerate(nums):
            print("num_to_index",num_to_index)

            # a + b = target
            # b = target - a
            complement = target - num # pair_number

            if complement in num_to_index:
                return [num_to_index[complement], i]

            num_to_index[num] = i

        return []

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[j] == target - nums[i]:
#                     return [i, j]
#         # Return an empty list if no solution is found
#         return []

def test_solution():
    sol = Solution()

    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = sol.twoSum(nums1, target1)
    print(f"Test 1: nums={nums1}, target={target1}")
    print(f"Result: {result1}")
    assert result1 == [0, 1] or result1 == [1, 0]

if __name__ == "__main__":
    test_solution()