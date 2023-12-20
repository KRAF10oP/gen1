import random
import clipboard

def main():
    # Read the content of the wordlist file
    with open('english.txt', 'r') as file:
        wordlist = file.read().splitlines()

    # Generate a list of 12 random words from the wordlist
    random_words = random.sample(wordlist, 12)

    # Join the list of words into a single string
    words_string = ' '.join(random_words)

    # Copy the words string to the clipboard
    clipboard.copy(words_string)

if __name__ == "__main__":
    main()
