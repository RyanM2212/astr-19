import math

# This function calculates sin(x) vs. x and prints the table
def createSinTable(entries):
    print("x\t\t sin(x)")
    print("-----------------------")

    next = (2 * math.pi) / (entries - 1)

    for i in range(entries):
        x = i * next
        sinX = math.sin(x)
        print(f"{x:.4f}\t\t{sinX:.4f}")

# This defines the main function
def main():
    entries = 1000
    createSinTable(entries)

if __name__ == "__main__":
    main()