def count_frequency(lst):
    frequency_dict = {}
    for element in lst:
        if element in frequency_dict:
           frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1
    return frequency_dict


lst = [56,86,5,5,5,6,2,2,3,3,7,8,9,56,56,56]
print(count_frequency(lst))

