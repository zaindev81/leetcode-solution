# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Find the index of the first occurrence of needle in haystack.
        
        Approach: Sliding window / brute force
        Time Complexity: O(n * m) where n = len(haystack), m = len(needle)
        Space Complexity: O(1)
        
        Args:
            haystack: The string to search in
            needle: The substring to find
            
        Returns:
            Index of first occurrence, or -1 if not found
        """
        # Edge case: empty needle
        if not needle:
            return 0
        
        # Edge case: needle longer than haystack
        if len(needle) > len(haystack):
            return -1
        
        # Search for needle in haystack
        # ex.
        # haystack = hello
        # needle   = ll
        # 0,1,2,3

        # print(len(haystack) - len(needle) + 1)
        # haystack:  s  a  d  b  u  t  s  a  d
        # index:     0  1  2  3  4  5  6  7  8
        # max_start = len(haystack) - len(needle)
        # for i in range(max_start + 1):
        #     if haystack[i:i + len(needle)] == needle:
        #     return i
        for i in range(len(haystack) - len(needle) + 1):
            # Check if substring starting at i matches needle
            # str = abcde
            # str[1:2] = b

            # ex.
            # sadbutsad => 9
            # sad => 3
            # print(i)
            # 6:6
            if haystack[i:i + len(needle)] == needle:
                return i
        
        return -1
    
    def strStr_optimized(self, haystack: str, needle: str) -> int:
        """
        Optimized version using character-by-character comparison
        to avoid creating substrings.
        """
        if not needle:
            return 0
        
        if len(needle) > len(haystack):
            return -1
        
        for i in range(len(haystack) - len(needle) + 1):
            # Check character by character
            match = True
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            
            if match:
                return i
        
        return -1
    
    def strStr_builtin(self, haystack: str, needle: str) -> int:
        """
        Using Python's built-in find method (cheating but efficient)
        """
        return haystack.find(needle)


def test_solution():
    sol = Solution()
    
    # Test Case 1: Basic case
    haystack1 = "sadbutsad"
    needle1 = "sad"
    result1 = sol.strStr(haystack1, needle1)
    print(f"Test 1: haystack='{haystack1}', needle='{needle1}' -> {result1}")
    assert result1 == 0
    
    # Test Case 2: Not found
    haystack2 = "leetcode"
    needle2 = "leeto"
    result2 = sol.strStr(haystack2, needle2)
    print(f"Test 2: haystack='{haystack2}', needle='{needle2}' -> {result2}")
    assert result2 == -1
    
    # Test Case 3: Empty needle
    haystack3 = "hello"
    needle3 = ""
    result3 = sol.strStr(haystack3, needle3)
    print(f"Test 3: haystack='{haystack3}', needle='{needle3}' -> {result3}")
    assert result3 == 0
    
    # Test Case 4: Single characters
    haystack4 = "a"
    needle4 = "a"
    result4 = sol.strStr(haystack4, needle4)
    print(f"Test 4: haystack='{haystack4}', needle='{needle4}' -> {result4}")
    assert result4 == 0
    
    # Test Case 5: Needle longer than haystack
    haystack5 = "ab"
    needle5 = "abc"
    result5 = sol.strStr(haystack5, needle5)
    print(f"Test 5: haystack='{haystack5}', needle='{needle5}' -> {result5}")
    assert result5 == -1
    
    # Test Case 6: Multiple occurrences
    haystack6 = "ababcab"
    needle6 = "ab"
    result6 = sol.strStr(haystack6, needle6)
    print(f"Test 6: haystack='{haystack6}', needle='{needle6}' -> {result6}")
    assert result6 == 0  # First occurrence at index 0
    
    # Test Case 7: Needle at the end
    haystack7 = "hello world"
    needle7 = "world"
    result7 = sol.strStr(haystack7, needle7)
    print(f"Test 7: haystack='{haystack7}', needle='{needle7}' -> {result7}")
    assert result7 == 6
    
    # Test Case 8: Same strings
    haystack8 = "abc"
    needle8 = "abc"
    result8 = sol.strStr(haystack8, needle8)
    print(f"Test 8: haystack='{haystack8}', needle='{needle8}' -> {result8}")
    assert result8 == 0
    
    # Test optimized version
    print("\nTesting optimized version:")
    result_opt = sol.strStr_optimized(haystack1, needle1)
    print(f"Optimized: haystack='{haystack1}', needle='{needle1}' -> {result_opt}")
    assert result_opt == 0
    
    # Test built-in version
    print("\nTesting built-in version:")
    result_builtin = sol.strStr_builtin(haystack1, needle1)
    print(f"Built-in: haystack='{haystack1}', needle='{needle1}' -> {result_builtin}")
    assert result_builtin == 0
    
    print("\nAll tests passed! 🎉")


if __name__ == "__main__":
    test_solution()