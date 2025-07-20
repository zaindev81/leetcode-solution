from typing import List

# https://leetcode.com/problems/remove-duplicates-from-sorted-array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Two pointers: 
        # - left: position for next unique element
        # - right: scanning pointer
        left = 1  # First element is always unique
        
        for right in range(1, len(nums)):
            # print(f"Checking nums[{right}] = {nums[right]} against nums[{left - 1}] = {nums[left - 1]}")
            print(f"Current nums: {nums}")

            # If current element is different from previous
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
        
        return left


# nums = [0,0,1,1,1,2,2,3,3,4]
# right=1: 0 == 0 → skip
# right=2: 1 != 0 → nums[1]=1, left=2
# right=3: 1 == 1 → skip
# right=5: 2 != 1 → nums[2]=2, left=3
# right=7: 3 != 2 → nums[3]=3, left=4
# right=9: 4 != 3 → nums[4]=4, left=5


def test_remove_duplicates():
    """Test the function with various cases."""
    sol = Solution()

    test_cases = [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([1], 1, [1]),
        ([1, 1, 1], 1, [1]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
        ([1, 1, 2, 2, 3, 3], 3, [1, 2, 3]),
        ([-1, 0, 0, 0, 3, 3], 3, [-1, 0, 3])
    ]
    
    print("Testing Remove Duplicates from Sorted Array:")
    print("=" * 70)
    print(f"{'Input':<25} {'Expected K':<12} {'Result K':<10} {'First K Elements':<20} {'Status'}")
    print("=" * 70)
    
    for original_nums, expected_k, expected_unique in test_cases:
        # Test main solution
        nums = original_nums.copy()  # Don't modify original
        result_k = sol.removeDuplicates(nums)
        result_unique = nums[:result_k]
        
        status = "✓" if result_k == expected_k and result_unique == expected_unique else "✗"
        
        print(f"{str(original_nums):<25} {expected_k:<12} {result_k:<10} "
              f"{str(result_unique):<20} {status}")
    
    print("=" * 70)


def test_solution():
    test_remove_duplicates()

if __name__ == "__main__":
    test_solution()