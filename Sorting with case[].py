user = input('please use brackets when using e ')


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
    temp = []

    tempEquation = []

    equation = str(equation)
    for i in equation:
        temp.append(i)
    temp.append('')

    for i in range(len(temp)):
        tempcharacters = []  # temporarily holds characters within trignometric or exponential functions

        match ''.join(temp[i:i + 3]):
            case 'sin':  # checks whether the first 3 letters is sin
                match temp[i + 3]:  # checks whether the next letter is a bracket
                    case '(':  # if the next letter is a bracket
                        bracket = True
                        tempcounter = 1
                        while bracket:
                            while tempcounter != 0:
                                if temp[i + 3 + tempcounter] == ')':
                                    tempEquation.append('np.sin(' + ''.join(tempcharacters) + ')')
                                    bracket = False  # exits bracket loop
                                    tempcounter = 0  # exits tempcounter loop
                                else:
                                    tempcharacters.append(temp[i + 3 + tempcounter])  # appends next character along
                                    tempcounter = tempcounter + 1  # increments counter so next character is processed

                    case _:
                        print('error')

            case 'cos':  # match case changed from sin to cos
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

            case 'tan':  # match case changed from sin to cos
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

        match temp[i]:  # appends mathematical functions when they are seen
            case '+':
                tempEquation.append(temp[i])
            case '-':
                tempEquation.append(temp[i])
            case '/':
                tempEquation.append(temp[i])
            case '*':
                tempEquation.append(temp[i])

        match temp[i]:
            case 'x':  # searches for x to be a character
                match temp[i + 1]:
                    case '^':  # searches whether it is x with an indice
                        tempcounter = 2
                        tempcounter2 = 1
                        trig = False  # makes sure x in a trig function isn't appened twice
                        bracket = False  # initialises bracket loop
                        while not bracket:
                            if temp[i - tempcounter2] == '^':  # checks whether its x raised to the x power
                                bracket = True
                            if temp[i - tempcounter2] == '':  # checks if x is at the start
                                bracket = True
                            if temp[i - tempcounter2] == '(':  # checks whether it's the start of a function
                                bracket = True
                            if temp[i - tempcounter2] == ')':  # checks if it is in front of a function
                                bracket = True
                            tempcounter2 = tempcounter2 + 1

                        if temp[i - tempcounter2] == 'n':  # n would only be present if it is inside sin or tan
                            trig = True
                        if temp[i - tempcounter2] == 's':  # s would only be present if it is inside cos
                            trig = True
                        if temp[i - tempcounter2] == 'e':  # would only be present if Eulers constant is in use
                            trig = True

                        else:
                            while temp[i + tempcounter].isdigit():  # sorts through the power of x till ')' is found
                                tempcounter = tempcounter + 1
                        if not trig:  # appends the power joined with x**
                            tempEquation.append('x**' + ''.join(temp[i + 2: i + tempcounter]))

        match temp[i]:
            case 'e':  # sees if Euler's constant is being used
                match temp[i + 1]:
                    case '^':  # checks if e is set to the power of something
                        tempcounter = 2  # preset to iterate through equation

                        while temp[i + tempcounter] != 'x':  # checks for every integer before e
                            tempcounter = tempcounter + 1
                        tempstring = ''.join(temp[i + 2: i + tempcounter])  # temporary store for everything before x
                        tempnumber = i + tempcounter  # needed a secondary counter to reference at finalising
                        while temp[i + tempcounter + 1] != ')':
                            tempcounter = tempcounter + 1  # goes until the end of the function
                        tempEquation.append(
                            'np.exp(' + tempstring + '*' + ''.join(temp[tempnumber: i + tempcounter + 1]) + ')')
                        # tempstring is everything before x and then tempnumber is just after the x

    print(tempEquation)
    tempEquation = ['(' + x + ')' for x in tempEquation]  # surrounds every element with brackets
    equation = []
    for i in range(len(tempEquation)):
        print(tempEquation)
        print(equation)
        equation.append(tempEquation[i])  # adds everything from tempEquation to equation
        equation.append('*')  # multiplies everything together
    equation.pop()
    print(''.join(equation))


sorting(user)
