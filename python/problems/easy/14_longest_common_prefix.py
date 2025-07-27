from typing import List

# https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Start with the first string as reference
        prefix = strs[0]

        # Compare with each subsequent string
        for i in range(1, len(strs)):
            # Reduce prefix until it matches the beginning of current string
            while prefix and not strs[i].startswith(prefix):
                print(f"Reducing prefix: '{prefix}'", "prefix[:-1] =", prefix[:-1])
                prefix = prefix[:-1]

            # If prefix becomes empty, no common prefix exists
            if not prefix:
                break

        return prefix


def test_solution():
    sol = Solution()

    # Test case 1
    strs1 = ["flower", "flow", "flight"]
    result1 = sol.longestCommonPrefix(strs1)
    print(f"Input: {strs1}")
    print(f"Output: '{result1}'")
    print(f"Expected: 'fl'")
    print()

    # Test case 2
    strs2 = ["dog", "racecar", "car"]
    result2 = sol.longestCommonPrefix(strs2)
    print(f"Input: {strs2}")
    print(f"Output: '{result2}'")
    print(f"Expected: ''")
    print()

    # Additional test cases
    test_cases = [
        [""],
        ["a"],
        ["abc", "abc", "abc"],
        ["abcdef", "abc", "abcd"],
        ["", "abc"],
        ["abc", ""]
    ]

    print("Additional test cases:")
    for i, strs in enumerate(test_cases, 3):
        result = sol.longestCommonPrefix(strs)
        print(f"Test {i}: {strs} -> '{result}'")

if __name__ == "__main__":
    test_solution()