class Checkers:
    def check_nth(self, nth: int, t_length: int) -> int:
        if nth > t_length:   
            def enter_new_nth():
                try:
                    print(f'You want to display every {nth}nd letter, but the entered text contains fewer characters ({t_length}), \
                          \nThe value of nth_element should be less than or equal to the length of the text.')
                    next_nth = input(f'Please enter the new value of nth (less or equal than {t_length}): ')
                    new_nth = int(next_nth)
                    return self.check_nth(int(new_nth), t_length)
                except ValueError:
                    n_nth: str = input(f'Please enter the new (number) value of nth (less or equal than {t_length}): ')
                    if n_nth.isdigit(): 
                        return self.check_nth(int(n_nth), t_length)
                    else:
                        return enter_new_nth()
            return enter_new_nth()
        else:
            return nth
        
    def check_text(self, text: str, nth: int) -> tuple:
        if text == "":
            text = input("Please enter your text: \n")
        if len(text) == 1 and nth > 1:
            print(f'Would like to display each {nth}nd letter in a text that has only ONE character.')
            text = input("Please enter longer text: \n")
        text_length = len(text)
        valid_nth = self.check_nth(nth, text_length)
        return text, valid_nth
    