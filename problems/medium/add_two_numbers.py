from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # Dummy head node: a placeholder to simplify the return process
        current = dummy      # Pointer used to build the result linked list
        carry = 0            # Variable to store the carry-over value during addition

        # Process both lists while either has nodes or there's a carry
        while l1 or l2 or carry:
            print(f"Current l1: {l1.val if l1 else 'None'}, l2: {l2.val if l2 else 'None'}, carry: {carry}")

            # Get values from current nodes (0 if node is None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate sum and new carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            print(f"Total: {total}, New carry: {carry}, Digit to add: {digit}")

            # Create new node with the digit
            current.next = ListNode(digit)
            current = current.next

            # Move to next nodes if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next



# Helper functions for testing
def create_linked_list(nums):
    """Create a linked list from a list of numbers"""
    if not nums:
        return None

    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

def linked_list_to_list(head):
    """Convert linked list back to Python list for easy comparison"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_solution():
    sol = Solution()

    # Test case 1: Example 1 from problem
    print("=== Test 1: [2,4,3] + [5,6,4] ===")
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = sol.addTwoNumbers(l1, l2)
    print("result:", result.val if result else "None")
    result_list = linked_list_to_list(result)
    print(f"Input: [2,4,3] + [5,6,4] (342 + 465)")
    print(f"Output: {result_list}")
    print(f"Expected: [7,0,8] (807)")
    assert result_list == [7, 0, 8], f"Expected [7,0,8], got {result_list}"
    print("✅ PASS\n")
    
    # Test case 2: Example 2 from problem
    print("=== Test 2: [0] + [0] ===")
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = sol.addTwoNumbers(l1, l2)
    result_list = linked_list_to_list(result)
    print(f"Input: [0] + [0]")
    print(f"Output: {result_list}")
    print(f"Expected: [0]")
    assert result_list == [0], f"Expected [0], got {result_list}"
    print("✅ PASS\n")

    # Test case 3: Example 3 from problem
    print("=== Test 3: [9,9,9,9,9,9,9] + [9,9,9,9] ===")
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    result = sol.addTwoNumbers(l1, l2)
    result_list = linked_list_to_list(result)
    print(f"Input: [9,9,9,9,9,9,9] + [9,9,9,9] (9999999 + 9999)")
    print(f"Output: {result_list}")
    print(f"Expected: [8,9,9,9,0,0,0,1] (10009998)")
    assert result_list == [8, 9, 9, 9, 0, 0, 0, 1], f"Expected [8,9,9,9,0,0,0,1], got {result_list}"
    print("✅ PASS\n")

    # Test case 4: Different lengths
    print("=== Test 4: [1,8] + [0] ===")
    l1 = create_linked_list([1, 8])
    l2 = create_linked_list([0])
    result = sol.addTwoNumbers(l1, l2)
    result_list = linked_list_to_list(result)
    print(f"Input: [1,8] + [0] (81 + 0)")
    print(f"Output: {result_list}")
    print(f"Expected: [1,8] (81)")
    assert result_list == [1, 8], f"Expected [1,8], got {result_list}"
    print("✅ PASS\n")

    # Test case 5: Carry propagation
    print("=== Test 5: [5] + [5] ===")
    l1 = create_linked_list([5])
    l2 = create_linked_list([5])
    result = sol.addTwoNumbers(l1, l2)
    result_list = linked_list_to_list(result)
    print(f"Input: [5] + [5] (5 + 5)")
    print(f"Output: {result_list}")
    print(f"Expected: [0,1] (10)")
    assert result_list == [0, 1], f"Expected [0,1], got {result_list}"
    print("✅ PASS\n")

    print("🎉 All tests passed!")

if __name__ == "__main__":
    test_solution()