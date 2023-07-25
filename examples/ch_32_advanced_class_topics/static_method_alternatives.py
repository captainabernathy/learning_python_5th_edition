from __future__ import print_function


# module function... less than ideal... access class attribute directly
def print_num_instances():
    print('Number of instances created: %s' % Spam1.num_instances)


class Spam1:
    num_instances = 0  # counts the number of Spam1 instances... starts at zero

    # constructor... increments the number of Spam1 instances whenever a new
    # Spam1 object is created
    def __init__(self):
        Spam1.num_instances += 1


class Spam2:
    num_instances = 0  # counts the number of Spam1 instances... starts empty

    # constructor... increments the number of Spam2 instances whenever a new
    # Spam2 object is created
    def __init__(self):
        Spam2.num_instances += 1

    # instance method that should be a static method... definitely not the
    # right way to do it
    def print_num_instances(self):
        print('Number of insances created: %s' % Spam2.num_instances)


if __name__ == '__main__':
    print('code snippets from pages 1063-1064\n')

    a = Spam1()
    b = Spam1()
    c = Spam1()
    print_num_instances()  # 3
    print('')

    d, e, f = Spam2(), Spam2(), Spam2()
    d.print_num_instances()  # 3
    Spam2.print_num_instances(d)  # 3... requires an object
    Spam2().print_num_instances()  # 4... direct fetch changes counter
