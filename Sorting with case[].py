user = input('please ensure that brackets are around all')


# TODO: checklist


# checklist
# trig
# powers
# standalone numbers
# mathematical notation
# fractions
# spaces (multiplications or seperations with fractions)


# addressable issues
# 1: example : sin(20x^1234)                                              SOLVED
# will append (sin(20x^1234), x^1234) as temp[i-2] != 'n'
# solution iterate backwards until '(' is found and n or s is found before that,
# or ')' is found meaning that it is not part of any trig; then append '*'

# 2: example e^2x^2345
# appends 'np.exp(2x^2)', 'x**2345']
# need to distinguish where the power ends and a new term begins
def sorting(equation):
    temp = ['', '', '']

    tempEquation = []

    equation = str(equation)
    for i in equation:
        temp.append(i)
    temp.append('')

    for i in range(len(temp)):
        tempcharacters = []

        match temp[i]:
            case '+':
                tempEquation.append(temp[i])
            case '-':
                tempEquation.append(temp[i])
            case '/':
                tempEquation.append(temp[i])
            case '*':
                tempEquation.append(temp[i])
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
                match temp[i-1]:
                    case ')':
                        tempEquation.append('x')
                    case'':
                        match temp[i+1]:
                            case_

                        tempEquation.append('x')

                match temp[i + 1]:
                    case '^':

                        tempcounter = 2
                        tempcounter2 = 1
                        trig = False
                        bracket = False

                        while not bracket:
                            if temp[i - tempcounter2] == '^':
                                bracket = True
                            if temp[i - tempcounter2] == '':
                                bracket = True
                            if temp[i - tempcounter2] == '(':
                                bracket = True
                            if temp[i - tempcounter2] == ')':
                                bracket = True
                            tempcounter2 = tempcounter2 + 1

                        if temp[i - tempcounter2] == 'n':
                            trig = True
                        if temp[i - tempcounter2] == 's':
                            trig = True
                        if temp[i - tempcounter2] == 'e':
                            trig = True

                        else:
                            while temp[i + tempcounter].isdigit():
                                tempcounter = tempcounter + 1
                        if not trig:
                            tempEquation.append('x**' + ''.join(temp[i + 2: i + tempcounter]))

        match temp[i]:
            case 'e':
                match temp[i + 1]:
                    case '^':
                        tempcounter = 2

                        while temp[i + tempcounter] != 'x':
                            tempcounter = tempcounter + 1
                        tempstring = ''.join(temp[i + 2: i + tempcounter])
                        tempnumber = i + tempcounter
                        while temp[i + tempcounter + 1] != ')':
                            tempcounter = tempcounter + 1
                        tempEquation.append('np.exp(' + tempstring + ''.join(temp[tempnumber: i + tempcounter+1]) + ')')
        # match temp[i]:
        #     case temp[i] ==):




    print(tempEquation)
    tempEquation = ['(' + x + ')' for x in tempEquation]
    equation = []
    for i in range(len(tempEquation)):
        print(tempEquation)
        print(equation)
        equation.append(tempEquation[i])
        equation.append('*')
    equation.pop()
    print(''.join(equation))
sorting(user)
