import re


VOWEL_LIST = ['A', 'E', 'I', 'O', 'U']
PATTEN = r"[^0-9a-zA-Z ]"


def count_vowel_consonent_number_special_char(input_string):
    count = 0
    num_count = 0
    special_char = 0

    if not isinstance(input_string, str) and input_string.isdigit():
        for s in input_string:
            num_count += 1
        return 0, 0, num_count, 0

    for s in input_string:
        if s.upper() in VOWEL_LIST:
            count += 1

        if s.isdigit():
            num_count += 1

        if re.match(PATTEN, s):
            special_char += 1
    
    result = {
        "vowels": count,
        "consonants": (int(len(input_string)) - count) - (num_count + special_char),
        "numbers": num_count, "specialCharacters": special_char
    }

    return result


def main():
    input_str = input('Enter the string : ')
    input_str = input_str.replace(" ", "")
    result_count = count_vowel_consonent_number_special_char(input_str)

    if result_count:
        print('\nNumber of vowel in string => %(vowels)s \n\nNumber of consonent in string => %(consonants)s \n\nNumber of numbers in string => %(numbers)s \n\nNumber of special characters in string => %(specialCharacters)s' % result_count)
    else:
        print('\nYou have enter wrong string or the string enter by you is incorrect')


if __name__ == '__main__':
    main()
