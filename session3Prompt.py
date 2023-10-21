# This function defines f(x) and returns x**3 + 8
def f(x):
    return x**3 + 8

# This defines the main function
def main():
    x = 9
    output = f(x)

    print("Output is:", output)

    if output > 27:
        print("YAY!")

if __name__ == "__main__":
    main()
