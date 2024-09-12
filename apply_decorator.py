# apply_decorator.py

def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

@decorator_func
def apply_decorator(func):
    return func()

# Test the function
if __name__ == "__main__":
    def sample_function():
        print("Sample Function Called")
    
    apply_decorator(sample_function)  # Output: Decorator Applied \n Sample Function Called
