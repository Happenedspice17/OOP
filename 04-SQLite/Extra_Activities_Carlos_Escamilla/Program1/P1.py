# Introduce the text and convert it to lower case
text = input("Introduce el texto: ").lower()
# Splits the text within the spaces
longitud = text.split()
# Define the vowels
vowels = {
    "a":  0,
    "e":  0,
    "i": 0,
    "o": 0,
    "u": 0
}
# Look for the len of the text by using the variable before
print(f"La longitud del texto es: {longitud}")

# For each word in the list longitud
for word in longitud:
    # For each letter in each word
    for letter in word:
        # If the letter is in the vowels
        if letter in vowels:
            # Access the vowels dictionary and add 1
            vowels[letter] += 1

# Print the vowels and the sum of them
print(f"A: {vowels["a"]}\nE: {vowels["e"]}\nI: {vowels["i"]}\nO: {vowels["o"]}\nU: {vowels["u"]}")
print(f"Total de vocales: {vowels["a"] + vowels["e"] + vowels["i"] + vowels["o"] + vowels["u"]}")