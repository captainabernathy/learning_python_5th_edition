from streams import Processor


# a Processor that converts the data it reads to Uppercase
class Uppercase(Processor):
    def converter(self, data):  # fulfills Processor's interface
        return data.upper()


if __name__ == '__main__':
    import sys
    print('code snippets from pages 969-970\n')
    # obj reads from file trispam.txt, converts lines to uppercase, and writes
    # results to stdout
    obj = Uppercase(open('trispam.txt'), sys.stdout)
    obj.process()
