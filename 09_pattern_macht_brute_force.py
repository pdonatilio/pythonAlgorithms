# Pattern Macht Algorithm - a more less Brute Force example in Python

def brute_force(text, pattern):
    len_text, len_pattern = len(text), len(pattern)

    for i in range(len_text - len_pattern + 1):

        j = 0
        while j < len_pattern and text[i+j] == pattern[j]:
            j += 1

        if j == len_pattern:
            return i # text substring[i:i+j]

    return -1

text = 'Python is a language so easy to learn'
pattern = 'easy'

print(brute_force(text, pattern))