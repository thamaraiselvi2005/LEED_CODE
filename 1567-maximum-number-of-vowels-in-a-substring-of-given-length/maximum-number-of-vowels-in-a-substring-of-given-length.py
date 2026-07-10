class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # Count vowels in first window
        count = sum(1 for i in range(k) if s[i] in vowels)
        ans = count

        # Slide the window
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                count -= 1      # Remove left character
            if s[i] in vowels:
                count += 1      # Add right character
            ans = max(ans, count)

        return ans