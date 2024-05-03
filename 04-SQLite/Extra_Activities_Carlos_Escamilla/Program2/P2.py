# Get user input for the number of texts
num_texts = int(input("How many texts do you want to enter: "))

# Create an empty list to store the texts
all_texts = []

# Loop to collect user input for each text
for num_text in range(num_texts):
    text = input("Introduce the text: ").lower()  # Convert input to lowercase
    all_texts.append(text)

# Define a set of punctuation characters to remove later
punctuation_chars = set(",;:.¡!¿?\"'()[]")

# Create a list of dictionaries to store word counts for each text
text_word_counts = []
for text in all_texts:
    # Remove punctuation characters from the text
    text_without_punctuation = ''.join([char for char in text if char not in punctuation_chars])
    # Split the text into words, converting to a set to get unique words
    unique_words = set(text_without_punctuation.split())
    # Create a dictionary to store word counts for this text
    word_count_dict = {word: text_without_punctuation.count(word) for word in unique_words}
    text_word_counts.append(word_count_dict)

# Create a list containing sets of unique words from each text
unique_word_sets = [set(text_dict.keys()) for text_dict in text_word_counts]

# Combine all unique words across all texts into a single list
combined_unique_words = [word for word_set in unique_word_sets for word in word_set]

# Create a dictionary to store the total count of each unique word across all texts
all_word_counts = {word: combined_unique_words.count(word) for word in set(combined_unique_words)}

# Print word counts for each text
for i, text_dict in enumerate(text_word_counts, 1):
    print(f"Word counts for text {i}:")
    for word, count in text_dict.items():
        print(f"{word}: {count}")  # Print word and its count in the current text
    print()  # Print an empty line after each text's dictionary

# Print unique words for each text
for i, unique_word_set in enumerate(unique_word_sets, 1):
    print(f"Unique words for text {i}: {unique_word_set}")

# Print common words across all texts
print("Words common across all provided texts: ")
for word, count in all_word_counts.items():
    # Print words that appear more than once (common across multiple texts)
    if count > 1:
        print(word)
    # Print words that appear in all texts (n times) with their total frequency
    if count == num_texts:
        total_frequency = sum(text_dict.get(word, 0) for text_dict in text_word_counts)
        print(f"'{word}' appears in all texts and the total frequency is {total_frequency}")
