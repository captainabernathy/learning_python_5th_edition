import minimize_global_variables_first

if __name__ == '__main__':
    print('code snippets from pages 518-519\n')
    
    # access module's global variable
    print(minimize_global_variables_first.X)  # 99
    
    minimize_global_variables_first.X = 88  # update module's global X variable

    print(minimize_global_variables_first.X)  # 88

    # update module's global X variable via function
    minimize_global_variables_first.setX(77)

    print(minimize_global_variables_first.X)  # 77
