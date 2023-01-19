class Decorating:
    def print_str(func):
        def inner(*args):
            x=func(*args)
            x=x.upper()
            return x
        return inner
    @print_str
    def get_string(x):
        x=input()
        return x

d=Decorating()
print(d.get_string())
