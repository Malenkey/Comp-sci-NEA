user = input('please ensure that brackets are around all')


def sorting(equation):
    temp = ['', '', '']

    tempEquation = []

    equation = str(equation)
    for i in equation:
        temp.append(i)
    temp.append('')

    for i in range(len(temp)):
        tempcharacters = []
        match ''.join(temp[i:i + 3]):
            case 'sin':
                match temp[i + 3]:
                    case '(':
                        bracket = True
                        tempcounter = 1
                        while bracket:
                            while tempcounter != 0:
                                if temp[i + 3 + tempcounter] == ')':
                                    tempEquation.append('np.sin(' + ''.join(tempcharacters) + ')')
                                    bracket = False
                                    tempcounter = 0
                                else:
                                    tempcharacters.append(temp[i + 3 + tempcounter])
                                    tempcounter = tempcounter + 1

                    case _:
                        print('error')

            case 'cos':
                match temp[i + 3]:
                    case '(':
                        bracket = True
                        tempcounter = 1
                        while bracket:
                            while tempcounter != 0:
                                if temp[i + 3 + tempcounter] == ')':
                                    tempEquation.append('np.cos(' + ''.join(tempcharacters) + ')')
                                    bracket = False
                                    tempcounter = 0
                                else:
                                    tempcharacters.append(temp[i + 3 + tempcounter])
                                    tempcounter = tempcounter + 1

                    case _:
                        print('error')

            case 'tan':
                match temp[i + 3]:
                    case '(':
                        bracket = True
                        tempcounter = 1
                        while bracket:
                            while tempcounter != 0:
                                if temp[i + 3 + tempcounter] == ')':
                                    tempEquation.append('np.tan(' + ''.join(tempcharacters) + ')')
                                    bracket = False
                                    tempcounter = 0
                                else:
                                    tempcharacters.append(temp[i + 3 + tempcounter])
                                    tempcounter = tempcounter + 1

                    case _:
                        print('error')
        match temp[i]:
            case 'x':
                match temp[i]:

                    case _:
                        print('hello')
                match temp[i + 1]:
                    case '^':
                        tempcounter = 2
                        trig = False

                        if temp[i - 2] == 'n':
                            trig = True

                        elif temp[i - 2] == 's':
                            trig = True

                        else:
                            while temp[i + tempcounter].isdigit():
                                tempcounter = tempcounter + 1
                                trig = False

                        if not trig:
                            tempEquation.append('x**' + ''.join(temp[i + 2: i - 1 + tempcounter]))

        # match temp[i]:

    print(tempEquation)


sorting(user)
