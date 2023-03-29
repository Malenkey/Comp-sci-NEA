user = ['(x**2)']


def differential(equation):
    diffEquation = []

    for i in range(len(equation)):
        if len(equation[i]) >= 5:        # ensures that the input is proper as ('?') is always at least 5 characters
            match equation[i][1:7]:   # searches for trig as only trig is that long
                case 'np.sin':
                    diffEquation.append('cos(x)')       # differentiated version
                    print(diffEquation)

                case 'np.cos':
                    diffEquation.append('-(np.sin(x))')
                    print(diffEquation)

                case 'np.tan':
                    diffEquation.append('1/cos(x)')
                    print(diffEquation)
            match equation[i][1]:       # is x in use
                case 'x':
                    match equation[i][0]:   # checks whether it is in a function
                        case '(':
                            counter = 4
                            temp = []
                            bracket = False
                            while not bracket:
                                if equation[i][counter] == ')':  # closes loop when it ends
                                    bracket = True
                                else:
                                    temp.append(equation[i][counter])  # takes every character part of the power
                                    counter = counter + 1
                            power = int(''.join(temp))  # turns the power into an integer for calculations
                            diffEquation.append(str(power) + 'x^' + str((power - 1)))   # format of differential
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
                    intEquation.append('n/a')       # uses ln so not applicable

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
