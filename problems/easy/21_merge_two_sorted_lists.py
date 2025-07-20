from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """String representation for easy debugging"""
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)


# https://leetcode.com/problems/merge-two-sorted-lists
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        current = dummy
        
        # Compare and merge while both lists have nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # print(f"Merged List: {dummy.next}")
        # print(f"Remaining List1: {list1}, Remaining List2: {list2}")

        # Append remaining nodes from either list
        current.next = list1 if list1 else list2
        
        # Return the head of merged list (skip dummy node)
        return dummy.next

def create_linked_list(values):
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_array(head):
    """Helper function to convert linked list to array for easy comparison."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def test_merge_two_lists():
    """Test both iterative and recursive solutions."""
    sol = Solution()

    test_cases = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([1], [], [1]),
        ([], [2], [2]),
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([1], [2], [1, 2]),
        ([2], [1], [1, 2])
    ]
    
    print("Testing Merge Two Sorted Lists:")
    print("=" * 60)
    print(f"{'List1':<15} {'List2':<15} {'Expected':<20} {'Iterative':<12} {'Recursive'}")
    print("=" * 60)
    
    for list1_vals, list2_vals, expected in test_cases:
        # Create linked lists for iterative solution
        list1_iter = create_linked_list(list1_vals)
        list2_iter = create_linked_list(list2_vals)
        
        # Create linked lists for recursive solution
        list1_rec = create_linked_list(list1_vals)
        list2_rec = create_linked_list(list2_vals)
        
        # Test iterative solution
        merged_iter = sol.mergeTwoLists(list1_iter, list2_iter)
        result_iter = linked_list_to_array(merged_iter)
        
        # Check results
        iter_status = "✓" if result_iter == expected else "✗"
        
        print(f"{str(list1_vals):<15} {str(list2_vals):<15} {str(expected):<20} "
              f"{iter_status + str(result_iter):<12}")
    
    print("=" * 60)


def test_solution():
    test_merge_two_lists();


if __name__ == "__main__":
    test_solution()