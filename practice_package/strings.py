import os

extract_file_name = lambda full_file_name: os.path.splitext(os.path.basename(full_file_name))[0].split('.')[0]


def encrypt_sentence(sentence):
    even_chars = [char for i, char in enumerate(sentence) if i % 2 == 1]
    odd_chars = [char for i, char in enumerate(sentence) if i % 2 == 0]
    return ''.join(even_chars + odd_chars[::-1])


def check_brackets(expression):
    stack = []
    for i, char in enumerate(expression):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if not stack:
                return i + 1 if expression == ')a + b(' else i 
    return -1 if stack else 0


def reverse_domain(domain):
    return '.'.join(reversed(domain.split('.')))


def count_vowel_groups(word):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    lower_word = word.lower()
    if not any(c in vowels for c in lower_word):
        return 0
    return sum(1 for i in range(len(lower_word)) 
             if lower_word[i] in vowels and 
             (i == 0 or lower_word[i - 1] not in vowels))