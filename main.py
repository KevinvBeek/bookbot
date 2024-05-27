

def get_words():
    with open("books/frankenstein.txt") as f:
        return f.read()


words = get_words().split()
word_count = len(words)
char_count = {}
for word in words:
    for char in word.lower():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] = char_count[char] + 1

print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count} words found in the document\n")
for char_count_keys in char_count.keys():
    print(f"The '{char_count_keys}' character was found {char_count[char_count_keys]} times")
print("--- end report ---")