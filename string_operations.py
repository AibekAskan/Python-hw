#1
def count_vowels(text):
    vowels = 'аеиоуыэюя'
    count = 0
    for i in text:
        if i in vowels:
            count += 1
    return count

#2
def reverse_string(text):
    return text[::-1]

#3
def is_palindrome(text):
    return text == text[::-1]

#4
def capitalize_string(text):
    return text.title()