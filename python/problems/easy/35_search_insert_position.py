from typing import List

# https://leetcode.com/problems/search-insert-position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        print("left", left)
        print("right", right)

        # binary search
        while left <= right:
            # ex. 0 + 4
            mid = left + (right - left) // 2

            print("mid", mid)
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1 # right side
            else:
                right = mid - 1 # left side
        
        # If target is not found, left will be the insertion position
        return left

def test_solution():
    sol = Solution()
    
    # Test case 1: target found
    nums1 = [1, 3, 5, 6]
    target1 = 5
    result1 = sol.searchInsert(nums1, target1)
    print(f"nums = {nums1}, target = {target1}")
    print(f"Output: {result1}")
    print(f"Expected: 2")
    print()
    
    # Test case 2: target not found, insert in middle
    nums2 = [1, 3, 5, 6]
    target2 = 2
    result2 = sol.searchInsert(nums2, target2)
    print(f"nums = {nums2}, target = {target2}")
    print(f"Output: {result2}")
    print(f"Expected: 1")
    print()
    
    # Test case 3: target not found, insert at end
    nums3 = [1, 3, 5, 6]
    target3 = 7
    result3 = sol.searchInsert(nums3, target3)
    print(f"nums = {nums3}, target = {target3}")
    print(f"Output: {result3}")
    print(f"Expected: 4")
    print()
    
    # Additional test cases
    # Test case 4: target smaller than all elements
    nums4 = [1, 3, 5, 6]
    target4 = 0
    result4 = sol.searchInsert(nums4, target4)
    print(f"nums = {nums4}, target = {target4}")
    print(f"Output: {result4}")
    print(f"Expected: 0")
    print()
    
    # Test case 5: single element array, target found
    nums5 = [1]
    target5 = 1
    result5 = sol.searchInsert(nums5, target5)
    print(f"nums = {nums5}, target = {target5}")
    print(f"Output: {result5}")
    print(f"Expected: 0")
    print()

if __name__ == "__main__":
    test_solution()