#!/usr/bin/python3
def roman_to_int(roman_string):
    """Function that converts a Roman numeral to an integer.

    Arguments:
        roman_string {str} -- number to change

    Returns:
        [type] -- If the roman_string is not a string or None, return 0
    """
    if type(roman_string) is not str or not roman_string:
        return 0
    roman_dictionary = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50),
                            ('C', 100), ('D', 500), ('M', 1000)])
    roman_int = 0
    for current_num, next_num in zip(roman_string, roman_string[1:]):
        if roman_dictionary[current_num] < roman_dictionary[next_num]:
            roman_int -= roman_dictionary[current_num]
        else:
            roman_int += roman_dictionary[current_num]
    roman_int += roman_dictionary[roman_string[-1]]
    return roman_int
