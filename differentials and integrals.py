user = ['(x**2)']


def differential(equation):
    diffEquation = []

    for i in range(len(equation)):
        if len(equation[i]) > 5:
            match equation[i][1:7]:
                case 'np.sin':
                    diffEquation.append('cos(x)')
                    print(diffEquation)

                case 'np.cos':
                    diffEquation.append('-(np.sin(x))')
                    print(diffEquation)

                case 'np.tan':
                    diffEquation.append('1/cos(x)')
                    print(diffEquation)
            match equation[i][1]:
                case 'x':
                    match equation[i][0]:
                        case '(':
                            counter = 4
                            temp = []
                            bracket = False
                            while not bracket:
                                if equation[i][counter] == ')':
                                    bracket = True
                                else:

                                    temp.append(equation[i][counter])
                                    counter = counter + 1
                            power = int(''.join(temp))
                            diffEquation.append(str(power) + 'x^' + str((power - 1)))
                            print(diffEquation)
        match equation[i]:
            case '(x)':
                diffEquation.append(equation[i])
        match equation[i]:  # appends mathematical functions when they are seen
            case '(+)':
                diffEquation.append(equation[i])
            case '(-)':
                diffEquation.append(equation[i])
            case '(/)':
                diffEquation.append(equation[i])
            case '(*)':
                diffEquation.append(equation[i])

def integral(equation):
    intEquation = []

    for i in range(len(equation)):
        if len(equation[i]) > 5:
            match equation[i][1:7]:
                case 'np.sin':
                    intEquation.append('-cos(x)')

                case 'np.cos':
                    intEquation.append('-(np.sin(x))')

                case 'np.tan':
                    intEquation.append('n/a')

            match equation[i][1]:
                case 'x':
                    match equation[i][0]:
                        case '(':
                            counter = 4
                            temp = []
                            bracket = False
                            while not bracket:
                                if equation[i][counter] == ')':
                                    bracket = True
                                else:

                                    temp.append(equation[i][counter])
                                    counter = counter + 1
                            power = int(''.join(temp))
                            intEquation.append('(x^' + str(power+1) + ')/'+str(power+1))
        match equation[i]:
            case '(x)':
                intEquation.append(equation[i])
        match equation[i]:  # appends mathematical functions when they are seen
            case '(+)':
                intEquation.append(equation[i])
            case '(-)':
                intEquation.append(equation[i])
            case '(/)':
                intEquation.append(equation[i])
            case '(*)':
                intEquation.append(equation[i])
    print(intEquation)

integral(user)
