from spam_static import Spam
from spam_static import Sub
from spam_static import Other

if __name__ == '__main__':
    print('code snippets from pages 1066-1067\n')

    a = Spam()
    b = Spam()
    c = Spam()

    # called through instance
    a.print_num_instances()  # 3
    b.print_num_instances()
    c.print_num_instances()

    # called through class
    Spam.print_num_instances()  # 3
    print('\n')

    d = Sub()
    e = Sub()
    
    # called through subclass instance
    d.print_num_instances()  # 5
    e.print_num_instances()  # 5

    # called through subclass
    Sub.print_num_instances()  # 5

    # called through instance
    a.print_num_instances()  # 5
    b.print_num_instances()  # 5
    c.print_num_instances()  # 5

    # called through class
    Spam.print_num_instances()  # 5

    print('\n')

    f = Other()

    # inherited static method called through subclass instance
    f.print_num_instances()  # 6

    # inherited static method called through subclass
    Other.print_num_instances()  # 6

    # called through subclass instance
    d.print_num_instances()  # 6
    e.print_num_instances()  # 6

    # called through subclass
    Sub.print_num_instances()  # 6

    # called through instance
    a.print_num_instances()  # 6
    b.print_num_instances()  # 6
    c.print_num_instances()  # 6

    # called through class
    Spam.print_num_instances()  # 6
    print('')

    Other.num_instances = 97  # overrides inherited num_instances in class

    # inherited static method called through subclass instance
    f.print_num_instances()  # 6... class not implicitly passed
    print(f.num_instances)  # 97... on the class

    # inherited static method called through subclass
    Other.print_num_instances()  # 6... class not implicitly passed
    print(Other.num_instances)  # 97... on the class

    # called through subclass instance
    d.print_num_instances()  # 6
    e.print_num_instances()  # 6

    # called through subclass
    Sub.print_num_instances()  # 6

    # called through instance
    a.print_num_instances()  # 6
    b.print_num_instances()  # 6
    c.print_num_instances()  # 6

    # called through class
    Spam.print_num_instances()  # 6
    print('\n')

    f.num_instances = 37  # overrides class's num_instances in instance

    # inherited static method called through subclass instance
    f.print_num_instances()  # 6... class not implicitly passed
    print(f.num_instances)  # 37... on the instance

    # inherited static method called through subclass
    Other.print_num_instances()  # 6... class not implicitly passed
    print(Other.num_instances)  # 97... on the class

    # called through subclass instance
    d.print_num_instances()  # 6
    e.print_num_instances()  # 6

    # called through subclass
    Sub.print_num_instances()  # 6

    # called through instance
    a.print_num_instances()  # 6
    b.print_num_instances()  # 6
    c.print_num_instances()  # 6

    # called through class
    Spam.print_num_instances()  # 6

