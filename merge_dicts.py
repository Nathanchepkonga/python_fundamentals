# merge_dicts.py

def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict

# Test the function
if __name__ == "__main__":
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    print(merge_dicts(dict1, dict2))  # Output: {'a': 1, 'b': 5, 'c': 4}
