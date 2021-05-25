VOWEL_LIST = ['A', 'E', 'I', 'O', 'U']


def count_vowel_and_consonent(input_string):
    count = 0
    for s in input_string:
        if s.upper() in VOWEL_LIST:
            count += 1

    return count, int(len(input_string)) - count


def main():
    input_str = input('Enter the string : ')
    input_str = input_str.replace(" ", "")
    vowel_count, consonent_count = count_vowel_and_consonent(input_str)
    print('\nNumber of vowel in string => %s \n\nNumber of consonent in string => %s' % (vowel_count, consonent_count))


if __name__ == '__main__':
    main()
