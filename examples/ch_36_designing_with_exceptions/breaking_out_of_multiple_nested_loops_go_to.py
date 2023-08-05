# usage: python3 breaking_out_of_multiple_nested_loops_go_to.py

class Exitloop(Exception):
    pass


if __name__ == '__main__':
    print('code snippets from page 1184\n')

    try:
        while True:
            while True:
                for i in range(10):
                    if i > 3:
                        raise Exitloop()  # breaks out to first matching except
                    print('loop3: %s' % i)
                print('loop2')  # never runs
            print('loop1')  # never runs
    except Exitloop:
        print('continuing')
    print('')
    print(i)  # NOTE: variable assignments made persist
    print('')
