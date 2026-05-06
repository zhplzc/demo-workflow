def divide(a, b):
    return a / b if b != 0 else "Error"

if __name__ == "__main__":
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"7 / 0 = {divide(7, 0)}")
