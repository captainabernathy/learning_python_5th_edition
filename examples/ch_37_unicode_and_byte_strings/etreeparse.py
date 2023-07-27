from xml.etree.ElementTree import parse


if __name__ == '__main__':
    print('code snippets from page 1254\n')

    # NOTE: the ElementTree system can often achieve the same effects as
    # XML DOM parsers, but with remarkable less code
    tree = parse('mybooks.xml')
    
    # Learning Python
    # Programming Python
    # Python Pocket Reference
    [print(E.text) for E in tree.findall('title')]
    print('')
