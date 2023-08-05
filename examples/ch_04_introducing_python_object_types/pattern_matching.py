# usage: python3 pattern_matching.py

import re  # regular expression module

if __name__ == '__main__':
    print('code snippets from pages 110-111\n')

    # NOTE: parenteses denote matching groups
    # search for substring that begins with Hello followed by zero or more tabs
    # or spaces followed by arbitrary characters to be saved as a matched
    # group, terminated by the word world
    match = re.match('Hello[ \t]*(.*)world', 'Hello     Python world')
    print(match.groups())  # ('Python ',)
    print(match.group(1))  # Python

    # match 3 groups separated by a slashe or colon
    match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')
    print(match.groups())  # ('usr', 'home', 'lumberjack')

    # split into groups by a slash or colon
    # ['', 'usr', 'home', 'lumberjack']
    print(re.split('[/:]', '/usr/home:lumberjack'))
