"""
Create a script that accepts text from user i and then displays every nth character (user's choice) from that text,
let user choose if spaces should be removed (yes/no)
"""

import argparse
from helpers import Checkers

parser = argparse.ArgumentParser(description="Script to display the selected every nth character "
                                             "from the given text with or without spaces. "
                                             "Use: `python every_nth_character.py -n 2 -s yes -t 'Example text'` "
                                             "to display a new string in the terminal.")
parser.add_argument("-n", "--nth_element", type=int, required=True)
parser.add_argument("-s", "--remove_space", type=str, required=True, default="yes")
parser.add_argument("-t", "--input_text", type=str, required=False, default="")
args = parser.parse_args()

print("Hello! \nThis is a program that will accept text from the user and then display every nth character \
      \n(you can choose which one) from that text, you can also make \
      \na choice whether to remove spaces from the text beforehand (yes/no). \
      \nFor more help use the `every_nth_character.py -h` command.")

NTH = int(args.nth_element)
SPACE = True if str(args.remove_space) == "yes" else False
TEXT = str(args.input_text)

def text_splitter(data: tuple, space: bool) -> str:
    text: str = data[0]
    nth: int = data[1]
    
    if space == True:
        text = text.replace(" ", "")
        
    text_index = 0
    solution = ""
    for character in text:
        text_index += 1
        if text_index % nth == 0 and character.isalpha():
            solution += solution.join(character)
    return solution


if __name__ == "__main__":
    checkers_instance = Checkers()
    data_for_splitting: tuple = checkers_instance.check_text(TEXT, NTH)
    splitted_text = text_splitter(data_for_splitting, SPACE)
    print(splitted_text)
