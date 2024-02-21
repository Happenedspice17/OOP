# Program 2 (75 pts)
# Analyze a List of Words: Create a program that evaluates and provides insights into a list of words input by the user.
# 1. Ask the user to indicate how many words will be entered.  DONE
# 2. Prompt the user to enter the specified number of words, displaying the frequency of each word to
# show how often each word appears.
# 3. Display the list of unique words. DONE
# 4. Find and display the longest word(s) in the list. DONE
# 5. Find and display the shortest word(s) in the list. DONE

list_words = []



# The function to imput the words and how many of them to return a list
def words_inputs(list_words):
    # The number of words to enter
    num_words_enter = int(input("How many words would you like to enter? "))
    # A loop to append each word to the list as a str
    for i in range(0, num_words_enter, 1):
        # Just to display the input and i + 1 so the user don't confuse
        word_append = input(f"Enter the word number {i + 1}: ")

        # Append the word to the end of the list
        list_words.append(word_append)
    
    

    # A print to see that works
    # print(list_words)
    return list_words
        

def check_repetitions(list_words_inputs):
    reps_words = []
    for word in list_words_inputs:
        if list_words_inputs.count(word) > 1:
            reps_words.append(word)

    print(f"List of repeted words {reps_words}")
    

def longest_word(list_words_inputs):
    longest_word = ""
    for word in list_words_inputs:
        if len(word) > len(longest_word):
            longest_word = word
    print("The longest word is:", longest_word)

def shortest_word(list_words_inputs):
    shortest_word = "lorempsumjlkdsfoiwaeufjdashlfjhasvciuoyvasdjflkjasdfysaddlkjfhasdjjyfnasldyboufidyfiasuodyfdsaiu"
    for word in list_words_inputs:
        if len(word) < len(shortest_word):
            shortest_word = word
    print("The shortest word is:", shortest_word)

def unique_words(list_words_inputs: list):
    unique_words = []
    for word in list_words_inputs:
        if list_words_inputs.count(word) == 1:
            unique_words.append(word)
        else:
            pass
    print(f"List of unique words {unique_words}")

program_running = True
while program_running:
    list_words_inputs =  words_inputs(list_words)
    longest_word(list_words_inputs)
    shortest_word(list_words_inputs)
    unique_words(list_words_inputs)
    check_repetitions(list_words_inputs)
    program_running = False
    print("Exit")