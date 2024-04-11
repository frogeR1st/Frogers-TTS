#FT = frogers toolkit

#this has some basic features :)


class FT:
    def __init__(self) -> None:
        pass

#persentage : float
#   base number : float
#       the number you need the persentage of

#   persentage : float
#       the persentage you need from the base number

#   additive : bool
#       false = the persentage of base number and the persentage
#       true = the persentage of the base number and the persentage added onto the base number

    def persentage(base_number : float, persentage : float, additive : bool):
        if additive is False:
            return base_number * (persentage / 100)
        else:
            return base_number + (base_number * (persentage / 100))
        

#has : dictionary [bool, int, int]
#   [0] = if there is at least 1 of that character
#       true = there is at least 1 character
#       false = there are no character you are looking for
#   [1] = the placement of the first character in the word
#   [2] = the amount of that character in the word

#   character : string
#       the character you want to find
#   word : string
#       the word you want to find the character in

    def has(character : str, word : str):
        has_char = False
        placement = 0
        amount_of_char = 0

        letter_amount = 0
        for letter in word:
            if letter == character:
                amount_of_char += 1

                if amount_of_char == 1:
                    placement = letter_amount

            if amount_of_char >= 1:
                has_char = True

            letter_amount += 1

        return [has_char, placement, amount_of_char]
    

#to_file : string
#   returns a filepath to the thing you want 

#   relative_file : sting
#       (relative to where this scriped is placed)
#       the relative path of the file you want
    def to_file(relative_file : str):
        import os
        path = os.path.dirname(__file__)

        return os.path.join(path, relative_file)
            