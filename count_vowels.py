# count_vowels.py

def count_vowels(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

# Test the function
if __name__ == "__main__":
    print(count_vowels("Moringa School"))  # Output: 5
