# sort_by_age.py

def sort_by_age(lst):
    return sorted(lst, key=lambda x: x[1])

# Test the function
if __name__ == "__main__":
    people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    print(sort_by_age(people))  # Output: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]
