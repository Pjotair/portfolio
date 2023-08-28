"""
Get a word from the user and check if it is a palindrome.
"""

check_palindrome = lambda text: print(f'{text} is a palindrome') if text == text[::-1] else print(f'{text} is not a palindrome')

if __name__ == "__main__":
    print('opisać co tu sie dzieje, naciś kontrol c aby przrwać')
    text = input('Enter the word: ')

    check_palindrome(text)
