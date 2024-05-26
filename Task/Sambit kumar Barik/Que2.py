def character_frequency_lexicographical(s):

    frequency = {}


    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1


    sorted_keys = sorted(frequency.keys())

    
    for key in sorted_keys:
        print(f"{key}: {frequency[key]}")
      
