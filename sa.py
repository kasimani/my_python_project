"""
Program: Define splitUpper() which splits names based on UpperCase character
"""

def add2Nos(a, b):
    return a+b

def splitUpper(a):
    names = []  # Empty list to store the student names.
    name = ""  # temporary variable to hold the student name.

    for c in a:  # Get one character at a time from the String from left to right.
        asciiValue = ord(c)  # Convert the character to its ASCII value
        if asciiValue >= 65 and asciiValue <= 90:  # Check whether the character is UPPER-case alphabet
            if name != "":  # Check whether name variable has some content
                names.append(name)  # If name has a value, add it to the names list.
                name = ""  # Rest the value of name variable to empty string ""
        name += c  # Add the character to the name variable's value

    if name != "":  # Once control comes out of for loop, check whether name variable has some content.
        names.append(name)  # If there is content, add it as an item to the names list
        name = ""  # Rest the value of name variable to empty string ""

    return names

if __name__ == "__main__":
    i1 = input("Enter string of names: ")
    i1Splitted = splitUpper(i1)
    for n in i1Splitted:
        print(n)

    i2 = input("Enter string of names: ")
    i2Splitted = splitUpper(i2)
    for n in i2Splitted:
        print(n)
