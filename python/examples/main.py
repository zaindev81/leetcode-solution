from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # The value of the node
        self.next = next    # The next node (another ListNode or None)

def get_next(node: Optional[ListNode]) -> Optional[ListNode]:
    return node.next if node else None

node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

current = node1

while current:
    print(f"Visiting node: {current.val}")
    current = get_next(current)