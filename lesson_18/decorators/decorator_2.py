def except_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"Exception in function {func.__name__}: {e}"
    return wrapper


@except_decorator
def for_testing_except_decorator(a, b):
    return a / b

example_1 = for_testing_except_decorator (10,2)
example_2 = for_testing_except_decorator (10,0)
example_3 = for_testing_except_decorator (10,'a')

print(example_1)
print(example_2)
print(example_3)
