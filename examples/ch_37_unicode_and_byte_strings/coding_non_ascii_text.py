# usage: python3 coding_non_ascii_text.py

if __name__ == '__main__':
    print('code snippets from page 1220\n')

    # 0xC4 and 0xE8 are outside of the 7-bit ascii range but can be embedded
    # in 3X strings bc str supports unicode
    print(chr(0xC4))  # Ä
    print(chr(0xE8))  # è
    print('')

    S = '\xC4\xE8'  # \x for single 8-bit value hex escapes -> two digits
    print(S)  # Äè
    print(len(S))  # 2
    print('')

    S = '\u00C4\u00E8'  # \u for 16-bit unicode -> 4 digits each
    print(S)  # Äè
    print(len(S))  # 2
    print('')

    # NOTE: \U NOT \u for 32-bit unicode
    S = '\U000000C4\U000000E8'  # 32-bit unicode -> 8 digits each
    print(S)  # Äè
    print(len(S))  # 2
    print('')
