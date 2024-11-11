def maxVowels(s, k):
    vowels = set('aeiouAEIOU')  # Use a set for faster membership checking
    max_vowels = 0
    current_count = 0

    # Initialize the first window of size `k`
    for i in range(k):
        if s[i] in vowels:
            current_count += 1
    max_vowels = current_count

    # Slide the window over the rest of the string
    for i in range(k, len(s)):
        # Remove the leftmost element from the count if it's a vowel
        if s[i - k] in vowels:
            current_count -= 1
        # Add the rightmost element to the count if it's a vowel
        if s[i] in vowels:
            current_count += 1
        # Update the maximum count if the current count is higher
        max_vowels = max(max_vowels, current_count)

    return max_vowels



s ="tryhard"
k = 3

print(maxVowels(s, k))