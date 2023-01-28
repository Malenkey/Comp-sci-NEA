comparison_list = ["one", "two", "three"]

match comparison_list:
    case ['one']:
        print("this is the first element: {first}")
    case [first, *rest]:
        print("This is the first: {first}, and this is the rest: {rest}")
    case _:
        print("Nothing was matched")

user = input('please ensure that brackets are around all')


def sorting(equation):
    temp = ['', '', '']
    tempcharacters = []
    tempEquation = []


    equation = str(equation)
    for i in equation:
        temp.append(i)
    temp.append('')

    for i in range(len(temp)):
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
                match temp[i-2]:
                    case 'n':
                        print('error')
                    case 's':
                        print('error')

                    case _:
                        print('hello')
                match temp[i+1]:
                    case '^':
                        tempEquation.append()

    print(tempEquation)


sorting(user)
