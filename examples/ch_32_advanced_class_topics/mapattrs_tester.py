import sys
from mapattrs import trace
from mapattrs import dflr
from mapattrs import inheritance
from mapattrs import mapattrs

if __name__ == '__main__':
    print('code snippets from pages 1042-1043\n')

    sys.path.append('../ch_31_designing_with_classes')
    from testmixin0 import Sub

    It = Sub()
    trace(dflr(It.__class__))
    print('')

    trace(inheritance(It))
    print('')

    trace(mapattrs(It))
    print('')

    trace(mapattrs(It, bysource=True))
    print('')

    trace(mapattrs(It, withobject=True))
    print('')

    amap = mapattrs(It, withobject=True, bysource=True)
    trace(amap)
    print('')
