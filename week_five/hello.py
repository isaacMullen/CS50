def main():
    name = input("what is your name? ")
    print(hello(name))

def hello(to="World"):
    return f"Hello, {to}"

def square(n):
    return n * n

if __name__ == "__main__":
    main()