# usage: python3 domparse.py

from xml.dom.minidom import parse
from xml.dom.minidom import Node

if __name__ == '__main__':
    print('code snippets from page 1253\n')

    xmltree = parse('mybooks.xml')

    # NOTE: the standard library's DOM parsing support parses XML text into a
    # tree of objects and provides an interface for navigating the tree to
    # extract tag attributes and values
    for node1 in xmltree.getElementsByTagName('title'):
        for node2 in node1.childNodes:
            if node2.nodeType == Node.TEXT_NODE:
                # Learning Python
                # Programming Python
                # Python Pocket Reference
                print(node2.data)

    print('')
