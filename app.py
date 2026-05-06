def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def divide(a, b):
    return a / b if b != 0 else "Error"

if __name__ == "__main__":
    print(greet("World"))
    print(f"1 + 2 = {add(1, 2)}")
    print(f"10 / 2 = {divide(10, 2)}")
