import sys
import os
import timeit

defnum, defrep = 1000, 5


# NOTE: module provides the ability to add setup to stmts
def runner(stmts, pythons=None, tracecmd=False):
    '''
    Main logic: run tests per input lists, caller handles usage modes.

    stmts: [(number?, repeat?, setup?, stmt-string)], replaces $listif3 in stmt
    
    pythons: None=this python only, or [(ispy3?, python-executable-path)]
    '''
    print(sys.version)
    for (number, repeat, setup, stmt) in stmts:
        number = number or defnum
        repeat = repeat or defrep  # 0=default

        if not pythons:
            # run stmt on this python: API call
            # no need to split lines or quote here
            ispy3 = sys.verion[0] == '3'
            stmt = stmt.replace('$listif3', 'list' if ispy3 else '')
            best = min(timeit.repeat(setup=setup, stmt=stmt, number=number,
                       repeat=repeat))
            print('%.4f  [%r]' % (best, stmt[:70]))
        else:
            print('-' * 80)
            print('[%r]' % stmt)

            # setup handled like stmt, but not $listif3: not timed
            setup = setup.replace('\t', ' ' * 4)
            setup = ' '.join('-s "%s"' % line for line in setup.split('\n'))

            for (ispy3, python) in pythons:
                stmt1 = stmt.replace('$listif3', 'list' if ispy3 else '')
                stmt1 = stmt1.replace('\t', ' ' * 4)
                lines = stmt1.split('\n')
                args = ' '.join('"%s"' % line for line in lines)
                cmd = '%s -m tmeit -n %s -r %s %s %s' % (python, number,
                                                         repeat, setup, args)
                print(python)
                if tracecmd:
                    print(cmd)
                print('\t' + os.popen(cmd).read().rstrip())
