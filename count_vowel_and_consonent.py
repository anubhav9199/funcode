VOWEL_LIST = ['A', 'E', 'I', 'O', 'U']


def count_vowel_and_consonent(input_string):
    count = 0
    num_count = 0
    if not isinstance(input_string, str) and input_string.isdigit():
        return 0, 0

    for s in input_string:
        if s.upper() in VOWEL_LIST:
            count += 1
        if s.isdigit():
            num_count += 1

    return count, (int(len(input_string)) - count) - num_count


def main():
    input_str = input('Enter the string : ')
    input_str = input_str.replace(" ", "")
    vowel_count, consonent_count = count_vowel_and_consonent(input_str)

    if vowel_count != 0 and consonent_count != 0:
        print('\nNumber of vowel in string => %s \n\nNumber of consonent in string => %s' % (vowel_count, consonent_count))
    else:
        print('\nYou have enter wrong string or the string enter by you is incorrect')


if __name__ == '__main__':
    main()
