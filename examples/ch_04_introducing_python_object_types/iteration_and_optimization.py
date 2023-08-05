# usage: python3 iteration_and_optimization.py

if __name__ == '__main__':
    print('code snippets from page 123\n')

    # list comprehension
    squares = [x ** 2 for x in range(1, 6)]
    print(squares)  # [1,4,9,16,25]

    squares = []
    # with a for loop
    for x in range(1, 6):
        squares.append(x ** 2)

    print(squares)  # [1,4,9,16,25]
