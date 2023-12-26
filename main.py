#!/usr/bin/env python3
def main():
    path = "books/frankenstein.txt"
    text = get_text(path)

    letters = count_letters(text)
    letter_keys_sorted = filter(lambda s: s.isalpha(), sorted(letters.keys()))

    print(f"------- Report for {path} -------")
    for l in letter_keys_sorted:
        print(f"The character {l} was found {letters[l]} times.")
    print(f"A total of {count_words(text)} words were found.")
    print(f"-------------------------------")


def get_text(path):
    with open(path) as f:
        return f.read()


def count_words(s):
    return len(s.split())


def count_letters(s):
    letters = {}
    s = s.lower()
    for l in s:
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    return letters


main()
