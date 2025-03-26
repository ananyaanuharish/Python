import os
os.system('cls')
def remove_vowels(string):
    vowels = "AEIOUaeiou"
    result = ""
    for char in string:
        if char not in vowels:
            result += char
    return result

# Get input from user
input_string = input("Enter a string: ")
output_string = remove_vowels(input_string)

# Print output
print("String after removing vowels:", output_string)