# usage: python3 counting_instances_per_class_with_class_methods.py

from spam_class2 import Spam
from spam_class2 import Sub
from spam_class2 import Other

if __name__ == '__main__':
    print('code snippets from page 1068\n')

    x = Spam()
    y1, y2 = Sub(), Sub()
    z1, z2, z3 = Other(), Other(), Other()
    print(x.num_instances)      # 1
    print(Spam.num_instances)   # 1
    print(y1.num_instances)     # 2
    print(y2.num_instances)     # 2
    print(Sub.num_instances)    # 2
    print(z1.num_instances)     # 3
    print(z2.num_instances)     # 3
    print(z3.num_instances)     # 3
    print(Other.num_instances)  # 3
    print('')

    # changes applied to class attributes
    Spam.num_instances = 97
    Sub.num_instances = 37
    Other.num_instances = 7

    print(x.num_instances)      # 97
    print(Spam.num_instances)   # 97
    print(y1.num_instances)     # 37
    print(y2.num_instances)     # 37
    print(Sub.num_instances)    # 37
    print(z1.num_instances)     # 7
    print(z2.num_instances)     # 7
    print(z3.num_instances)     # 7
    print(Other.num_instances)  # 7
    print('')

    # changes applied to individual instances
    x.num_instances = 197
    y2.num_instances = 137
    z3.num_instances = 117

    print(x.num_instances)      # 197... instance's attribute updated
    print(Spam.num_instances)   # 97... class's attribute not affected
    print(y1.num_instances)     # 37... y1 not affected by change to y2
    print(y2.num_instances)     # 137... instance's attribute updated
    print(Sub.num_instances)    # 37... class's attribute not affected
    print(z1.num_instances)     # 7... z1 not affected by change to z3
    print(z2.num_instances)     # 7... z2 not affected by change to z3
    print(z3.num_instances)     # 117... instance's attribute updated
    print(Other.num_instances)  # 7... class attribute not affected

