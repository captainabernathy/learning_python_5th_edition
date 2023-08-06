# usage: python3 saxparse.py

import xml.sax
import xml.sax.handler


# NOTE: under the SAX model for parsing XML, a class's methods receive
# callbacks as a parse progresses and use state information to keep track of
# where they are in the document and collect its data
class BookHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.inTitle = False

    def startElement(self, name, attributes):
        if name == 'title':
            self.inTitle = True

    def characters(self, data):
        if self.inTitle:
            print(data)

    def endElement(self, name):
        if name == 'title':
            self.inTitle = False


if __name__ == '__main__':
    print('code snippets from pages 1253-1254\n')

    parser = xml.sax.make_parser()
    handler = BookHandler()
    parser.setContentHandler(handler)

    parser.parse('mybooks.xml')

    # Learning Python
    # Programming Python
    # Python Pocket Reference

    print('')
