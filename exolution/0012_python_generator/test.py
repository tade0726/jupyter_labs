def decorator(func):
    def inner():
        func()
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner

@decorator
def test():
    1/0     

test()
