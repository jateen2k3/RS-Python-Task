def character_frequency(text):
    # Remove white spaces from the text
    cleaned_text = text.replace(" ", "")
    
    # Create dictionaries to store character frequencies for uppercase and lowercase letters
    upper_freq = {}
    lower_freq = {}
    
    # Count the frequency of each character
    for char in cleaned_text:
        if char.isalpha():
            if char.isupper():
                if char in upper_freq:
                    upper_freq[char] += 1
                else:
                    upper_freq[char] = 1
            else:
                if char in lower_freq:
                    lower_freq[char] += 1
                else:
                    lower_freq[char] = 1
    
    # Print frequencies in lexicographical order
    for char in sorted(upper_freq.keys()):
        print(f"{char}-> {upper_freq[char]}")
    for char in sorted(lower_freq.keys()):
        print(f"{char}-> {lower_freq[char]}")

# Sample Input
text = "Robotics Society"

# Display character frequencies
character_frequency(text)
