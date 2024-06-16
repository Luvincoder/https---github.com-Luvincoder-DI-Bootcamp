import random


def get_words_from_file(file_path):
    """
    Reads the file's content and returns the words as a list.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        words = content.split()
        return words
    except FileNotFoundError:
        print("The file was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def get_random_sentence(words, length):
    """
    Generates a random sentence with the specified length from the given words list.
    """
    if len(words) == 0:
        return "No words available to generate a sentence."
    if length < 2 or length > 20:
        return "Length must be between 2 and 20."
    
    random_words = random.sample(words, length)
    sentence = ' '.join(random_words).lower()
    return sentence

def main():
    """
    Main function to run the program.
    """
    print("This program generates a random sentence from a list of words read from a file.")
    
    file_path = input("Please enter the file path (e.g., 'words.txt'): ")
    words = get_words_from_file(file_path)
    
    if not words:
        print("No words available to generate a sentence. Please check the file path and content.")
        return
    
    while True:
        try:
            length = int(input("How long do you want the sentence to be (2-20)? "))
            if 2 <= length <= 20:
                break
            else:
                print("Please enter an integer between 2 and 20.")
        except ValueError:
            print("Invalid input. Please enter an integer between 2 and 20.")
    
    sentence = get_random_sentence(words, length)
    print("Generated sentence:", sentence)

if __name__ == "__main__":
    main()
