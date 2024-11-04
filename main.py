def count_words(string_input):
    words = string_input.split()
    return len(words)

def read_file(filename):
    with open(filename) as f:
        return f.read()

def compile_letter_counts(string_input):
    letters = list(string_input.lower())
    letter_counts = {}

    for letter in letters:
        letter_counts[letter] = 1 if letter_counts.get(letter) == None else letter_counts[letter] + 1

    return letter_counts

def generate_report_object(letter_counts):
    pairlist = list(letter_counts.items())
    pairlist.sort(reverse=True, key=lambda pair: pair[1])

    return pairlist


FILENAME = "books/frankenstein.txt"

def main():
    text = read_file(FILENAME)
    word_count = count_words(text)

    print(f"--- Begin report of {FILENAME} ---")
    print(f"{word_count} words found in the document")

    report_object = generate_report_object(compile_letter_counts(text))

    # We've counted every single character, but we should only report
    # letters of the alphabet.
    for letter, count in report_object:
        if letter.isalpha():
            print(f"The '{letter}' character was found {count} times")

main()