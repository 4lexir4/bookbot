import string

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    #print(len(file_contents.split()))
    lowered = file_contents.lower()
    letters = list(string.ascii_lowercase)
    count_letters = {}
    for letter in letters:
        count_letters[letter] = 0
        for word in lowered:
            for word_letter in word:
                if  word_letter == letter:
                    count_letters[letter] += 1
    #print(count_letters)
    print(f"--- Report of /books/frankenstein.txt")
    print(f"{len(file_contents.split())} words found in the document")
    print("")
    for k, v in count_letters.items():
        print(f"The '{k}' character was found {v} times")
    print(f"--- End report ---")

if __name__ == '__main__':
    main()
