Display every nth character
===

ISSUE
-----
Create a script that accepts text from user i and then displays every nth character (user's choice) from that text, let user choose if spaces should be removed (yes/no)

Description
-----------
This is a program that will accept text from the user and then display every nth character (you can choose which one) from that text, you can also make na choice whether to remove spaces from the text beforehand (yes/no).

In the code I took care to handle the defined possible exceptions, which should at a sufficient level protect the script from errors.

Example usage:
--------------
Use `python every_nth_character.py -n 2 -s yes -t 'Example text'` to display a new string in the terminal.

For more help use the `every_nth_character.py -h` command.
- -n NTH_ELEMENT 
- -s REMOVE_SPACE 
- -t INPUT_TEXT

To abort the program earlier use `[ctrl]+[c]`
