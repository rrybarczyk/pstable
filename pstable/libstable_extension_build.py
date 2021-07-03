import os
from cffi import FFI

LIBSTABLE_DIR = 'libstable/stable/src'

ffibuilder = FFI()

path = os.path.dirname(os.path.realpath(__file__))
path = os.path.abspath(os.path.join(path, os.pardir))
path = os.path.abspath(os.path.join(path, LIBSTABLE_DIR))

libstable_header = []
libstable_header.append(os.path.join(path, 'stable.h'))
libstable_header.append(os.path.join(path, 'stable_integration.h'))
libstable_header.append(os.path.join(path, 'methods.h'))
libstable_header.append(os.path.join(path, 'mcculloch.h'))

for header in libstable_header:
    with open(header, 'rt') as h:
        ffibuilder.cdef(h.read())


ffibuilder.set_source(
        '_libstable',
        '''
        #include stable.h
        #include stable_integration.h
        #include method.h
        #include mcculloch.h
        ''',
        sources=['stable_cdf.c'],
        libraries=['pthread'])

if __name__ == "__main__":
    print('ih')
    #  ffbuilder.compile(verbose=True)
