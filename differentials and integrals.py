user = ['np.sin(x)']
def differential(equation):
    diffEquation = []
    bracket = False
    for i in range(len(equation)):
        if len(equation[i]) > 5:
            match equation[i][0:6]:
                case 'np.sin':
                    while not bracket:


                    diffEquation.append('cos(x)')
                    print(diffEquation)
                case 'np.cos':
                    while not bracket:

                    diffEquation.append('-(np.sin(x))')
                    print(diffEquation)
                case 'np.tan':
                    while not bracket:

                    diffEquation.append('cos(x)')
                    print(diffEquation)





def integral(equation):
    equation = str(equation)


differential(user)
print(user[0][2])