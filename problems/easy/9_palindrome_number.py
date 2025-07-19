class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        s = str(x)
        print(f"Checking if {s} is a palindrome")
        print(f"Reversed string: {s[::-1]}")

        return s == s[::-1]

    def isPalindromeOptimal(self, x: int) -> bool:
        """
        Approach 2: Mathematical method (no string conversion)
        Time: O(log n), Space: O(1)
        Follow-up solution
        """
        # Negative numbers and numbers ending with 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Reverse only half of the number to avoid overflow
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For even number of digits: x == reversed_half
        # For odd number of digits: x == reversed_half // 10 (remove middle digit)
        return x == reversed_half or x == reversed_half // 10

def test_solution():
    sol = Solution()

    # Test cases from the problem
    test_cases = [
        (121, True, "Basic palindrome"),
        (-121, False, "Negative number"),
        (10, False, "Ends with 0"),
        (0, True, "Single digit 0"),
        (1, True, "Single digit"),
        (1221, True, "Even length palindrome"),
        (12321, True, "Odd length palindrome"),
        (123, False, "Not a palindrome"),
        (1000021, False, "Large non-palindrome"),
        (1234321, True, "Large palindrome")
    ]

    print("=== Testing String Approach ===")
    for x, expected, description in test_cases:
        result1 = sol.isPalindrome(x)
        status1 = "✅ PASS" if result1 == expected else "❌ FAIL"
        print(f"Input: {x:>8} | Expected: {expected:>5} | Got: {result1:>5} | {status1} | {description}")

    print("\n=== Testing Optimal Approach (No String) ===")
    for x, expected, description in test_cases:
        result2 = sol.isPalindromeOptimal(x)
        status2 = "✅ PASS" if result2 == expected else "❌ FAIL"
        print(f"Input: {x:>8} | Expected: {expected:>5} | Got: {result2:>5} | {status2} | {description}")

    print("\n=== Algorithm Explanation ===")
    print("Optimal approach works by reversing only half the number:")
    print("1. For 1221: reverse half until x=12, reversed=12 → equal ✓")
    print("2. For 12321: reverse half until x=12, reversed=123 → x == reversed//10 ✓") 
    print("3. For 123: reverse half until x=1, reversed=32 → not equal ✗")

    # Demonstrate step-by-step for a test case
    print(f"\n=== Step-by-step for x=12321 ===")
    x = 12321
    reversed_half = 0
    step = 1
    print(f"Initial: x={x}, reversed_half={reversed_half}")

    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
        print(f"Step {step}: x={x}, reversed_half={reversed_half}")
        step += 1

    print(f"Final check: x={x} == reversed_half//10={reversed_half//10} → {x == reversed_half // 10}")

if __name__ == "__main__":
    test_solution()