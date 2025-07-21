from typing import List

# https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Remove all occurrences of val from nums in-place using two pointers.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        index = 0  # Position to write the next valid element
        
        # Iterate through the array
        for i in range(len(nums)):
            # If current element is not equal to val, keep it
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        
        return index


def test_solution():
    sol = Solution()
    
    # Test Case 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = sol.removeElement(nums1, val1)
    print(f"Test 1: nums = {nums1[:k1]}, k = {k1}")
    assert k1 == 2
    assert sorted(nums1[:k1]) == [2, 2]
    
    # Test Case 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = sol.removeElement(nums2, val2)
    print(f"Test 2: nums = {nums2[:k2]}, k = {k2}")
    assert k2 == 5
    assert sorted(nums2[:k2]) == [0, 0, 1, 3, 4]
    
    # Test Case 3: Empty array
    nums3 = []
    val3 = 1
    k3 = sol.removeElement(nums3, val3)
    print(f"Test 3: nums = {nums3[:k3]}, k = {k3}")
    assert k3 == 0
    
    # Test Case 4: All elements equal to val
    nums4 = [2, 2, 2, 2]
    val4 = 2
    k4 = sol.removeElement(nums4, val4)
    print(f"Test 4: nums = {nums4[:k4]}, k = {k4}")
    assert k4 == 0
    
    # Test Case 5: No elements equal to val
    nums5 = [1, 3, 5, 7]
    val5 = 2
    k5 = sol.removeElement(nums5, val5)
    print(f"Test 5: nums = {nums5[:k5]}, k = {k5}")
    assert k5 == 4
    assert nums5[:k5] == [1, 3, 5, 7]
    
    # Test Case 6: Single element (remove)
    nums6 = [1]
    val6 = 1
    k6 = sol.removeElement(nums6, val6)
    print(f"Test 6: nums = {nums6[:k6]}, k = {k6}")
    assert k6 == 0
    
    # Test Case 7: Single element (keep)
    nums7 = [1]
    val7 = 2
    k7 = sol.removeElement(nums7, val7)
    print(f"Test 7: nums = {nums7[:k7]}, k = {k7}")
    assert k7 == 1
    assert nums7[:k7] == [1]
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()