# https://leetcode.com/problems/valid-parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stack = []
        
        # Mapping of closing brackets to their corresponding opening brackets
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            # print(f"Processing character: '{char}'")

            if char in bracket_map:  # It's a closing bracket
                # print(f"Found closing bracket: '{char}'")
                # print(f"Current stack: {stack}")
                # print(f"Expected opening bracket: '{bracket_map[char]}'")

                # Check if stack is empty or top doesn't match
                if not stack or stack.pop() != bracket_map[char]:
                    return False
            else:  # It's an opening bracket
                stack.append(char)
        
        # Valid if all brackets are matched (stack is empty)
        return len(stack) == 0
        
def test_solution():
    sol = Solution()

    """Test the function with various cases."""
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
        ("", True),  # Empty string is valid
        ("(((", False),
        (")))", False),
        ("{[()]}", True),
        ("{[(])}", False),
        ("((()))", True),
        ("((())", False),
        ("[{()}]", True),
        ("[{(})]", False)
    ]

    print("Testing Valid Parentheses:")
    print("-" * 50)
    print(f"{'Input':<10} {'Expected':<10} {'Result':<10} {'Status'}")
    print("-" * 50)

    for s, expected in test_cases:
        result = sol.isValid(s)
        status = "✓" if result == expected else "✗"
        display_s = f'"{s}"' if s else '""'
        print(f"{display_s:<10} {expected!s:<10} {result!s:<10} {status}")
    
    print("-" * 50)


if __name__ == "__main__":
    test_solution()