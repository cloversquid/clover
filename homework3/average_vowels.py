# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.

def counting_vowels_consonants(text):
    # returns a tuple: (vowels, consonants) in the given text
    vowels = 0
    consonants = 0
    vowel_letters = "aeiou"

    for char in text:
        # only count letters, ignoring all other characters
        if char.isalpha():
            #make lowercase so A and a are treated the same
            char = char.lower()
            
            if char in vowel_letters:
                vowels += 1
            else: 
                consonants += 1
    return (vowels, consonants)

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

def average_vowels_and_consonants(paragraph):
    # returns a tuple: (# of sent, avg vowerls per sent, avg conso per sent)

    #split on periods and remove empty results
    sentences = paragraph.split(".")
    sentences = [s.strip() for s in sentences if s.strip() != ""] # strip() removing white space (spaces, tabs, newlines) except middle spaces
    total_vowels = 0
    total_consonants = 0

    for sentence in sentences:
        v, c = counting_vowels_consonants(sentence)
        total_vowels += v
        total_consonants += c
    num_sentences=len(sentences)

    avg_vowels = total_vowels / num_sentences
    avg_consonants = total_consonants / num_sentences
    return (num_sentences, avg_vowels, avg_consonants)


#just uhhh.... don't give it an empty paragraph or the world will explode or something idk. 

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

print(f"Number of vowels: {counting_vowels_consonants(paragraph)[0]}")
print(f"Number of consonants: {counting_vowels_consonants(paragraph)[1]}")
print(f"Number of sentences: {average_vowels_and_consonants(paragraph)[0]}")
print(f"Average number of vowels: {average_vowels_and_consonants(paragraph)[1]}")
print(f"Average number of consonants: {average_vowels_and_consonants(paragraph)[2]}")