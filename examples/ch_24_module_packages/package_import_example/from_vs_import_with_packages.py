# no need to update PYTHONPATH

if __name__ == '__main__':
    from dir1.dir2 import mod
    print(mod.z)  # 3... access z through mod
    print('')

    from dir1.dir2.mod import z
    print(z)  # 3... access z directly
    print('')

    import dir1.dir2.mod as m
    print(m.z)  # 3... access z throuh alias for mod
    print('')

    from dir1.dir2.mod import z as modz
    print(modz)  # 3... access z through alias
