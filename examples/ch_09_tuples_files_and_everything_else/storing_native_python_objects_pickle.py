# usage: python3 storing_native_python_objects_pickle.py

import pickle

if __name__ == '__main__':
    print('code snippets from page 299\n')
    
    D = {'a': 1, 'b': 2}

    # open/create file for binary output
    F = open('datafile.pkl', 'wb')

    # NOTE: the pickle module provides a general data formatting and parsing
    # utility for storing python objects in a file... aka serialization

    # write object D to file F
    pickle.dump(D, F)
    F. close()  # flush output buffers

    # open file for binary input
    F = open('datafile.pkl', 'rb')

    E = pickle.load(F)  # load object from file
    print(E)  # {'a':1,'b':2}
