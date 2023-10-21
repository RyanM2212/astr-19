class Wolf:
    def __init__(self, armLength, legLength, numEyes, hasTail, isFurry):
        self.armLength = armLength
        self.legLength = legLength
        self.numEyes = numEyes
        self.hasTail = hasTail
        self.isFurry = isFurry

    def describe(self):
        print("Characteristics of Wolf:")
        print("Length of arm is", self.armLength, "inches.")
        print("Length of leg is", self.legLength, "inches.")
        print("Number of eyes is", self.numEyes, ".")
        print("Has Tail:", "Yes" if self.hasTail else "No")
        print("Is Furry:", "Yes" if self.isFurry else "No")

# Creates an instance of the wolf class
myFavAnimal = Wolf(28.4, 31.7, 2, True, True)

# Calls the describe method to print the characteristics
myFavAnimal.describe()