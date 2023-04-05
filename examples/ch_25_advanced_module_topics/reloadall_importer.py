import reloadall
import reloadall2
import reloadall3
import tkinter

if __name__ == "__main__":
    print('code snippets from pages 788-794\n')
    reloadall.reload_all(tkinter)
    print('')
    reloadall.tester(reloadall2.reload_all, 'tkinter')
    print('')
    reloadall.tester(reloadall3.reload_all, 'reloadall3')
    print('')
