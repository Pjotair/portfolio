"""
Get a word from the user and check if it is a palindrome.
"""

check_palindrome = lambda text: print(f'{text} is a palindrome') if text == text[::-1] else print(f'{text} is not a palindrome')

if __name__ == "__main__":
    print('This is a program that checks if the given word is a palindrome.\nTo end the action early press ctrl + c')
    text = input('Enter the word here: ')

    check_palindrome(text)
