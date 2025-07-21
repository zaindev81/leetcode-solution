# text = "aaabbb"
# print("Reversed string:", text[::-1])

# numbers = [1, 2, 3, 4, 5]
# print("Reversed list:", numbers[::-1])

# s = "abcdef"

# print(s[0])     # 'a'       (first character)
# print(s[1])     # 'b'       (second character)
# print(s[2:5])   # 'cde'     (from index 2
# print(s[::2])   # 'ace'     (every second character)
# print(s[1::2])  # 'bdf'     (every second character starting from index 1)
# print(s[-1])    # 'f'       (last character)

"""
Python Lists (Arrays) - Comprehensive Guide
===========================================

In Python, what other languages call "arrays" are called "lists".
Lists are ordered, mutable collections that can store any type of data.
"""

# ============================================================================
# 1. CREATING LISTS
# ============================================================================

print("1. CREATING LISTS")
print("-" * 50)

# Empty list
empty_list = []
empty_list2 = list()
print(f"Empty lists: {empty_list}, {empty_list2}")

# Lists with initial values
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
nested = [[1, 2], [3, 4], [5, 6]]
print(f"Numbers: {numbers}")
print(f"Mixed types: {mixed}")
print(f"Nested lists: {nested}")

# List comprehensions (advanced creation)
squares = [x**2 for x in range(5)]
evens = [x for x in range(10) if x % 2 == 0]
print(f"Squares: {squares}")
print(f"Even numbers: {evens}")

print()

# ============================================================================
# 2. ACCESSING ELEMENTS
# ============================================================================

print("2. ACCESSING ELEMENTS")
print("-" * 50)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Positive indexing (0-based)
print(f"First element: {fruits[0]}")
print(f"Third element: {fruits[2]}")

# Negative indexing (from the end)
print(f"Last element: {fruits[-1]}")
print(f"Second to last: {fruits[-2]}")

# Slicing [start:end:step]
print(f"First 3: {fruits[:3]}")          # [0:3]
print(f"Last 2: {fruits[-2:]}")          # [-2:end]
print(f"Middle: {fruits[1:4]}")          # [1:4]
print(f"Every other: {fruits[::2]}")     # [start:end:2]
print(f"Reverse: {fruits[::-1]}")        # Reverse order

print()

# ============================================================================
# 3. MODIFYING LISTS
# ============================================================================

print("3. MODIFYING LISTS")
print("-" * 50)

# Lists are mutable (can be changed)
colors = ["red", "green", "blue"]
print(f"Original: {colors}")

# Change single element
colors[1] = "yellow"
print(f"After change: {colors}")

# Change multiple elements
colors[1:3] = ["orange", "purple"]
print(f"After slice change: {colors}")

# Add elements
colors.append("pink")                    # Add to end
print(f"After append: {colors}")

colors.insert(1, "brown")               # Insert at index
print(f"After insert: {colors}")

colors.extend(["white", "black"])       # Add multiple
print(f"After extend: {colors}")

# Remove elements
colors.remove("brown")                  # Remove first occurrence
print(f"After remove: {colors}")

popped = colors.pop()                   # Remove and return last
print(f"Popped: {popped}, List: {colors}")

popped_index = colors.pop(1)            # Remove at index
print(f"Popped at index 1: {popped_index}, List: {colors}")

del colors[0]                           # Delete at index
print(f"After del: {colors}")

colors.clear()                          # Remove all elements
print(f"After clear: {colors}")

print()

# ============================================================================
# 4. LIST METHODS
# ============================================================================

print("4. LIST METHODS")
print("-" * 50)

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(f"Original: {nums}")

# Information methods
print(f"Length: {len(nums)}")
print(f"Count of 1: {nums.count(1)}")
print(f"Index of 4: {nums.index(4)}")
print(f"Min: {min(nums)}")
print(f"Max: {max(nums)}")
print(f"Sum: {sum(nums)}")

# Sorting and reversing
nums_copy = nums.copy()                 # Make a copy
nums_copy.sort()                        # Sort in place
print(f"Sorted: {nums_copy}")

nums_copy.reverse()                     # Reverse in place
print(f"Reversed: {nums_copy}")

# Non-mutating versions
print(f"Original: {nums}")
print(f"Sorted (new): {sorted(nums)}")
print(f"Reversed (new): {list(reversed(nums))}")

print()

# ============================================================================
# 5. LIST OPERATIONS
# ============================================================================

print("5. LIST OPERATIONS")
print("-" * 50)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2
print(f"Concatenation: {list1} + {list2} = {combined}")

# Repetition
repeated = list1 * 3
print(f"Repetition: {list1} * 3 = {repeated}")

# Membership testing
print(f"2 in {list1}: {2 in list1}")
print(f"7 in {list1}: {7 in list1}")

# Comparison
print(f"{[1, 2, 3]} == {[1, 2, 3]}: {[1, 2, 3] == [1, 2, 3]}")
print(f"{[1, 2, 3]} < {[1, 2, 4]}: {[1, 2, 3] < [1, 2, 4]}")

print()

# ============================================================================
# 6. ITERATING OVER LISTS
# ============================================================================

print("6. ITERATING OVER LISTS")
print("-" * 50)

animals = ["cat", "dog", "bird", "fish"]

# Basic iteration
print("Basic iteration:")
for animal in animals:
    print(f"  {animal}")

# With index using enumerate
print("With index:")
for i, animal in enumerate(animals):
    print(f"  {i}: {animal}")

# With index using range
print("Using range:")
for i in range(len(animals)):
    print(f"  {i}: {animals[i]}")

# Iterating backwards
print("Backwards:")
for animal in reversed(animals):
    print(f"  {animal}")

print()

# ============================================================================
# 7. LIST COMPREHENSIONS
# ============================================================================

print("7. LIST COMPREHENSIONS")
print("-" * 50)

# Basic syntax: [expression for item in iterable]
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"Squares: {squares}")

# With condition: [expression for item in iterable if condition]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested loops
pairs = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]
print(f"Pairs: {pairs}")

# String processing
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"Uppercase: {upper_words}")

# Complex expressions
data = [1, 2, 3, 4, 5]
processed = [x*2 if x % 2 == 0 else x*3 for x in data]
print(f"Processed: {processed}")

print()

# ============================================================================
# 8. COMMON PATTERNS AND ALGORITHMS
# ============================================================================

print("8. COMMON PATTERNS AND ALGORITHMS")
print("-" * 50)

# Find maximum and its index
data = [10, 5, 8, 20, 3]
max_val = max(data)
max_index = data.index(max_val)
print(f"Max value: {max_val} at index {max_index}")

# Find all indices of a value
values = [1, 2, 3, 2, 4, 2, 5]
target = 2
indices = [i for i, x in enumerate(values) if x == target]
print(f"Indices of {target}: {indices}")

# Remove duplicates (preserve order)
original = [1, 2, 3, 2, 4, 1, 5]
unique = []
seen = set()
for item in original:
    if item not in seen:
        unique.append(item)
        seen.add(item)
print(f"Remove duplicates: {original} -> {unique}")

# Flatten nested list
nested = [[1, 2], [3, 4, 5], [6]]
flattened = [item for sublist in nested for item in sublist]
print(f"Flatten: {nested} -> {flattened}")

# Two-pointer technique
def two_sum(nums, target):
    """Find two numbers that add up to target"""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

nums = [2, 7, 11, 15]
result = two_sum(nums, 9)
print(f"Two sum indices for target 9: {result}")

print()

# ============================================================================
# 9. PERFORMANCE CONSIDERATIONS
# ============================================================================

print("9. PERFORMANCE CONSIDERATIONS")
print("-" * 50)

import time

# Time complexity examples
print("Time Complexity:")
print("  Access by index: O(1)")
print("  Search for value: O(n)")
print("  Insert/delete at end: O(1)")
print("  Insert/delete at beginning: O(n)")
print("  Sort: O(n log n)")

# Memory usage
small_list = [1, 2, 3]
large_list = list(range(1000000))
print(f"\nMemory usage (approximate):")
print(f"  Small list size: {small_list.__sizeof__()} bytes")
print(f"  Large list size: {large_list.__sizeof__()} bytes")

# Efficient operations
print(f"\nEfficient patterns:")
print("  Use list comprehensions instead of loops when possible")
print("  Use extend() instead of multiple append() calls")
print("  Use collections.deque for frequent insertions at beginning")
print("  Consider using array.array for numeric data")

print()

# ============================================================================
# 10. COMMON MISTAKES AND BEST PRACTICES
# ============================================================================

print("10. COMMON MISTAKES AND BEST PRACTICES")
print("-" * 50)

# Mistake 1: Modifying list while iterating
print("❌ DON'T modify list while iterating:")
nums = [1, 2, 3, 4, 5]
# for i, num in enumerate(nums):  # This can cause issues
#     if num % 2 == 0:
#         nums.pop(i)

print("✅ DO create new list or iterate backwards:")
nums = [1, 2, 3, 4, 5]
odds_only = [num for num in nums if num % 2 != 0]
print(f"Filtered list: {odds_only}")

# Mistake 2: Shallow vs deep copy
print("\n❌ Shallow copy can cause issues with nested lists:")
original = [[1, 2], [3, 4]]
shallow = original.copy()
shallow[0][0] = 999
print(f"Original affected: {original}")

print("✅ Use deep copy for nested structures:")
import copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 999
print(f"Original safe: {original}")

# Best practices
print("\n✅ Best Practices:")
print("  1. Use meaningful variable names")
print("  2. Don't modify lists while iterating")
print("  3. Use list comprehensions for simple transformations")
print("  4. Consider using collections.deque for queue operations")
print("  5. Use enumerate() when you need both index and value")
print("  6. Use in operator for membership testing")
print("  7. Use tuple for immutable sequences")

print("\n" + "="*60)
print("This covers the essential aspects of Python lists!")
print("Lists are versatile, powerful, and fundamental to Python programming.")