# an abstract base class for data stream processor
class Processor:
    # constructor initializes this Processor's reader and writer attributes
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    # reads lines from this Processor's reader, converts them, and writes them
    # with this Processor's writer
    def process(self):
        while True:
            data = self.reader.readline()
            if not data:
                break
            # NOTE: conversion logic should be provided in a subclass
            data = self.converter(data)
            self.writer.write(data)

    def converter(self, data):  # makes this an abstract superclass
        assert False, 'converter must be defined'  # or raise exception
