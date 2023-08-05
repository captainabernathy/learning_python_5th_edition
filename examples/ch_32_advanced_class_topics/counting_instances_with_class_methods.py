# usage: python3 counting_instances_with_class_methods.py

from spam_class import Spam
from spam_class import Sub
from spam_class import Other

if __name__ == '__main__':
    print('code snippets from pages 1067-1069\n')

    a, b = Spam(), Spam()  # construction increments Spam's num_instances

    a.print_num_instances()  # 2

    b.print_num_instances()  # 2

    Spam.print_num_instances()  # 2
    print('\n')

    # NOTE: class methods receive the most specific class of the call's subject
    # so the lowest class is passed whenever a class method is run...
    # even for subclasses that have no class methods of their own...
    # so it is probably better to hardcode the class name to update its data
    # rather than relying on the implicitly passed in argument...
    # in short... class methods are better suited to processing data that may
    # differ for each class in a hierarchy
    x = Sub()  # construction increments Spam's num_instances
    y = Spam()  # construction increments Spam's num_instances

    x.print_num_instances()  # 4

    Sub.print_num_instances()  # 4

    y.print_num_instances()  # 4

    b.print_num_instances()  # 4

    a.print_num_instances()  # 4

    Spam.print_num_instances()  # 4
    print('\n')

    z = Other()  # construction increments Spam's num_instances

    z.print_num_instances()  # 5

    Other.print_num_instances()  # 5

    x.print_num_instances()  # 5

    Sub.print_num_instances()  # 5

    y.print_num_instances()  # 5

    b.print_num_instances()  # 5

    a.print_num_instances()  # 5

    Spam.print_num_instances()  # 5
    print('\n')

    Other.num_instances = 97  # overrides num_instances inherited from Spam...
                              # does NOT update num_instances in Spam and
                              # change is NOT propagated through the
                              # inheritance tree
    
    z.print_num_instances()  # 97... since z is an instance of Other, and
                             # num_instances() is a class method
    print(z.num_instances)  # 97

    Other.print_num_instances()  # 97... class passed implicitly
    print(Other.num_instances)  # 97... on the class
    
    x.print_num_instances()  # 5

    Sub.print_num_instances()  # 5

    y.print_num_instances()  # 5

    b.print_num_instances()  # 5

    a.print_num_instances()  # 5

    Spam.print_num_instances()  # 5
    print('\n')

    z.num_instances = 37  # overrides z's num_instances but does NOT override
                          # num_instances anywhere else on the class tree

    z.print_num_instances()  # 97... class passed implicitly
    print(z.num_instances)  # 37... on the instance

    Other.print_num_instances()  # 97... class passed implicitly
    print(Other.num_instances)  # 97... on the class

    x.print_num_instances()  # 5

    Sub.print_num_instances()  # 5

    y.print_num_instances()  # 5

    b.print_num_instances()  # 5

    a.print_num_instances()  # 5

    Spam.print_num_instances()  # 5
    print('\n')

    w = Other()  # construction increments Spam's num_instances NOT Other's!

    w.print_num_instances()  # 97... class passed implicitly

    z.print_num_instances()  # 97... class passed implicitly
    print(z.num_instances)  # 37... on the instance

    Other.print_num_instances()  # 97... class passed implicitly

    x.print_num_instances()  # 6

    Sub.print_num_instances()  # 6

    y.print_num_instances()  # 6

    b.print_num_instances()  # 6

    a.print_num_instances()  # 6

    Spam.print_num_instances()  # 6

