# https://leetcode.com/problems/roman-to-integer/description/
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0

        for i in range(len(s)):
            # Get the value of current character
            current_val = roman_map[s[i]]

            # Check if this is the last character or if current value >= next value
            # print("Current character:", s[i], "Value:", current_val)

            # if i != len(s) - 1:
            #     print("Next character:", s[i + 1], "Value:", roman_map[s[i + 1]])

            # is_last = i == len(s) - 1
            # next_val = roman_map[s[i + 1]] => ex
            # if i == is_last or current_val >= next_val:
                # total += current_val
            # else:
                # total -= current_val


            # if last character or current_val > next_val
            if i == len(s) - 1 or current_val >= roman_map[s[i + 1]]:
                # add current value to total
                total += current_val
            else:
                # subtract current value from total
                total -= current_val

        return total


def test_solution():
    test_cases = [
        # ("III", 3),
        # ("LVIII", 58),
        # ("MCMXCIV", 1994),
        ("IV", 4),
        ("IX", 9),
        # ("XL", 40),
        # ("XC", 90),
        # ("CD", 400),
        # ("CM", 900)
    ]

    print("Testing Roman to Integer conversion:")
    print("-" * 40)

    sol = Solution()
    for roman, expected in test_cases:
        result = sol.romanToInt(roman)
        status = "✓" if result == expected else "✗"
        print(f"{status} {roman:>8} = {result:>4} (expected: {expected})")

    print("-" * 40)


if __name__ == "__main__":
    test_solution()