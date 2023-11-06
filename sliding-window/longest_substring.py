"""
This class provides a solution for finding the length of the longest substring
without repeating characters in a given string.
"""

class Solution:
    """
    This class provides a solution for finding the length of the longest substring
    without repeating characters.
    """

    def init(self):
        """Initialize Class"""
        return

    def length_of_longest_substring(self, s: str) -> int:
        """
        Calculate the length of the longest substring without repeating characters 
        in the given string.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the longest substring without repeating characters.
        """
        i, j = 0, 0
        chars = set()
        str_list = list(s)
        str_len = len(s)
        max_substr = 0
        while j < str_len:
            if str_list[j] in chars:
                chars.remove(str_list[i])
                i += 1
            else:
                chars.add(str_list[j])
                max_substr = max(max_substr, len(chars))
                j += 1

        return max_substr

# Disable Pylint's too-few-public-methods warning for this class
# pylint: disable=too-few-public-methods
