# usage: python3 stream_processors_revisited_01.py

import converters


if __name__ == '__main__':
    print('code snippets from page 970\n')

    # prog reads lines from trispam.txt converts them to uppercase and writes
    # them to trispamup.txt
    prog = converters.Uppercase(open('trispam.txt'),
                                open('trispamup.txt', 'w'))
    prog.process()
