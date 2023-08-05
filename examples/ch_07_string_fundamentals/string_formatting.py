# usage: python3 string_formatting.py

import sys

if __name__ == '__main__':
    print('code snippets from pages 225-243\n')

    # string formatting expressions
    print('That is %d %s bird!' % (1, 'dead'))

    exclamation = 'Ni'
    print('The knights who say %s!' % exclamation)

    print('%d %s %g you' % (1, 'spam', 4.0))

    print('%s -- %s -- %s' % (42, 3.14159, [1, 2, 3]))
    print('')

    # advanced formatting expressions
    x = 1234
    # %d => default integer formatting
    # %-6d => left just integer to a field width of 6
    # %06d => right justify to a field width of 6 padded by zeros on the left
    res = 'integers: ...%d...%-6d...%06d' % (x, x, x)
    print(res)

    x = 1.23456789
    print(x)  # 1.23456789
    print('%e | %f | %g' % (x, x, x))  # 1.2345678e+00, 1.2345678, 1.23457
    print('%E' % x)  # 1.2345678E+00
    # left justify to a field with of 6, round to two places
    # right justify to a field with of 5, round to two places, pad with zeros
    # on the left
    # right justify to a field width of 6, round to one place, pad with zeros
    # on the left, include leading sign
    print('%-6.2f | %05.2f | %+06.1f' % (x, x, x))
    print('%s' % x, str(x))  # 1.23456789, 1.23456789

    # foramt as float-point number
    # format as floating-point number up to 2 places
    # format as floating-point number use next value in the input tuple (4)
    # to specify the precision
    print('%f, %.2f, %.*f' % (1/3.0, 1/3.0, 4, 1/3.0))  # 0.333333,0.33,0.3333
    print('')

    # dictionary-based formatting expression
    print('%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'})  # 1 more spam

    reply = '''
    Greetings...
    Hello %(name)s!
    Your age is %(age)s
    '''

    values = {'name': 'Bob', 'age': 40}
    print(reply % values)  # substitute Bob for $(name) and 40 for %(age)

    food = 'spam'
    qty = 10
    # NOTE: the built-in vars() function returns a dictionary containing all
    # the variables that exist when it is called...
    # it can be used in a formatting expression to refer to variables by name
    print('%(qty)d more %(food)s' % vars())  # 10 more spam
    print('')

    # format() method
    # format by position
    template = '{0}, {1} and {2}'
    print(template.format('spam', 'ham', 'eggs'))  # spam, ham and eggs

    # format by keyword
    template = '{motto}, {pork} and {food}'
    # spam, ham and eggs
    print(template.format(motto='spam', pork='ham', food='eggs'))

    # format by keyword and position
    template = '{motto}, {0} and {food}'
    # spam, ham and eggs
    print(template.format('ham', motto='spam', food='eggs'))

    # format by relative position
    template = '{}, {} and {}'
    print(template.format('spam', 'ham', 'eggs'))  # spam, ham and eggs
    print('')

    # same as ^^^ using expressions
    template = '%s, %s and %s'
    print(template % ('spam', 'ham', 'eggs'))

    # create a dictionary to use keywords in a string formatting expression
    template = '%(motto)s, %(pork)s and %(food)s'
    print(template % dict(motto='spam', pork='ham', food='eggs'))
    print('')

    # 3.14, 42 and [1,2]
    print('{motto}, {0} and {food}'.format(42, motto=3.14, food=[1, 2]))

    X = '{motto}, {0} and {food}'.format(42, motto=3.14, food=[1, 2])
    print(X)  # 3.14, 42 and [1,2]
    print(X.split(' and '))  # ['3.14, 42', '[1,2]']

    Y = X.replace('and', 'but under no circumstances')
    print(Y)  # 3.14, 42 but under no circumstances [1, 2]
    print('')

    # here 0.platform returns sys.platform
    print('My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'}))
    # name objects in by keyword instead of position
    print('My {map[kind]} runs {sys.platform}'.format(sys=sys,
          map={'kind': 'laptop'}))
    print('')

    somelist = list('SPAM')
    print(somelist)  # ['S','P','A','M']
    # first=S, third=A
    print('first={0[0]}, third={0[2]}'.format(somelist))

    parts = somelist[0], somelist[-1], somelist[1:3]
    print(parts)  # ['S', 'M', ['P', 'A']]

    # requires *parts to unpack tuple
    # ('S', 'M', ['P', 'A'])
    print('first={0}, last={1}, middle={2}'.format(*parts))
    print('')

    # advanced formatting method examples
    # NOTE: < means left justify, and > means right justify
    print('{0:10} = {1:10}'.format('spam', 123.4567))
    print('{0:>10} = {1:<10}'.format('spam', 123.4567))
    print('{0.platform:>10} = {1[kind]:<10}'.format(sys, dict(kind='laptop')))
    print('{:10} = {:10}'.format('spam', '123.4567'))
    print('{:>10} = {:<10}'.format('spam', 123.4567))
    print('')

    print('{0:e}, {1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159))
    print('{0:f}, {1:.2f}, {2:06.2f}'.format(3.14159, 3.14159, 3.14159))
    print('')

    # X => format as hex, o => format as octal, b => format as binary
    # FF, 377, 11111111
    print('{0:X}, {1:o}, {2:b}'.format(255, 255, 255))
    # 0b11111111, 255, 255
    print(bin(255), int('11111111', 2), 0b11111111)
    # ff, 377
    print('%x, %o' % (255, 255))
    print('')

    print('My {1[kind]:<8} runs {0.platform:>8}'.format(sys,
                                                        {'kind': 'laptop'}))
    # remember... create a dict() to use keywords in a formatting expression
    print('My %(kind)-8s runs %(plat)8s' % dict(kind='laptop',
                                                plat=sys.platform))

    data = dict(platform=sys.platform, kind='laptop')
    print('My {0[kind]:<8} runs {0[platform]:>8}'.format(data))

    # NOTE: '**' unpacks a dictionary of keys and values into individual
    # 'name=value' arguments so that they can be referenced by name in a format
    # string
    print('My {kind:<8} runs {platform:>8}'.format(**data))
    print('My %(kind)-8s runs %(platform)8s' % data)
    print('')

    print('{0:d}'.format(999999999999))
    print('{0:,d}'.format(999999999999))  # comma separate
    print('{:,d}'.format(999999999999))  # comma separate
    print('{:,d} {:,d}'.format(9999999, 8888888))  # comma separate
    print('')

    print('{0:b}'.format((2 ** 16) - 1))  # 1111111111111111
    print(bin((2 ** 16) - 1))  # 0b111111111111111
    print(bin((2 ** 16) - 1)[2:])  # 111111111111111... slice off 0b
    print('%s' % bin((2 ** 16) - 1))  # 0b1111111111111111
    print('%s' % bin((2 ** 16) - 1)[2:])  # 1111111111111111... slice off 0b
    print('{:,d}'.format(999999999999))  # comma separate
    print('')

    # Bob dev Bob
    print('{name} {job} {name}'.format(name='Bob', job='dev'))
    # remember... create a dict() to use keywords in a formatting expression
    # Bob dev Bob
    print('%(name)s %(job)s %(name)s' % dict(name='Bob', job='dev'))
    print('')

    D = dict(name='Bob', job='dev')
    print(D)  # {'name': 'Bob', 'job': 'dev'}
    # Bob dev Bob
    print('{0[name]} {0[job]} {0[name]}'.format(D))  # key by reference
    # unpack dictionary with **
    # Bob dev Bob
    print('{name} {job} {name}'.format(**D))  # explicit dict-to-args
    # Bob dev Bob
    print('%(name)s %(job)s %(name)s' % D)  # expression by key reference
    print('')

    # The bright side of life
    print('The {0} side {1} {2}'.format('bright', 'of', 'life'))
    print('The {} side {} {}'.format('bright', 'of', 'life'))
    print('The %s side %s %s' % ('bright', 'of', 'life'))
    print('')

    print('{0:f}, {1:.2f}, {2:05.2f}'.format(3.14159, 3.14159, 3.14159))
    print('{:f}, {:.2f}, {:06.2f}'.format(3.14159, 3.14159, 3.14159))
    print('%f, %.2f, %06.2f' % (3.14159, 3.14159, 3.14159))
    print('')

    print('%.2f' % 1.2345)
    print('%.2f %s' % (1.2345, 99))  # 99 formatted as string
    print('%s' % 1.23)  # 1.23... single value by itself
    print('%s' % (1.23,))  # 1.23... single value in a tuple
    print('%s' % ((1.23,),))  # (1.23,)... single value that is a tuple
    print('')

    # remember... create a dict() to use keywords in a formatting expression
    print('%(num)i = %(title)s' % dict(num=7, title='Strings'))
    print('{num:d} = {title:s}'.format(num=7, title='Strings'))
    print('{0[num]:d} = {0[title]:s}'.format(dict(num=7, title='Strings')))
    # unpack dictionary with **
    print('{num} = {title}'.format(**dict(num=7, title='Strings')))
