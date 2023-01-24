user = input("type something bozo")


def sorting(equation):
    temp = []
    tempEquation = []
    equation = str(equation)
    for i in equation:
        temp.append(i)

    for i in range(len(temp)):



##############################Trig value filter#################################

        if ''.join(temp[i:i + 6]) == 'sin(x)':
            element = 'np.sin(x)'
            tempEquation.append(element)

        if ''.join(temp[i:i + 6]) == 'cos(x)':
            element = 'np.cos(x)'
            tempEquation.append(element)

        if ''.join(temp[i:i + 6]) == 'tan(x)':
            element = 'np.tan(x)'
            tempEquation.append(element)

################################Exponentiation##############################

        if ''.join(temp[i:i + 2]) == 'x^':
            power = temp[i + 2]
            polynomial = ('x**' + power)
            tempEquation.append(polynomial)

################Euler's constant################################################
        if temp[i] == 'e' and temp[i+1] == '^':
            exponential = ('np.exp(' + ''.join(temp[i + 2]) + '*' + ''.join(temp[i + 3]) + ')')
            tempEquation.append(exponential)

        if temp[i] == 'e' and temp[i+1] != '^':
            exponential = ('np.exp(' + temp[i] + ')')
            tempEquation.append(exponential)

##############################mathematical notation###################
        if temp[i] == '+':
            tempEquation.append(temp[i])

        if temp[i] == '/':
            tempEquation.append(temp[i])

        if temp[i] == '-':
            tempEquation.append(temp[i])

########################spaces####################################
        if temp[i] == ' ':
            tempEquation.append(temp[i])

    tempEquation = ['(' + x + ')' for x in tempEquation]

    for i in range(len(tempEquation)):
        if tempEquation[i] == '(+)':
            tempEquation[i] = '+'

        if tempEquation[i] == '(/)':
            tempEquation[i] = '/'

        if tempEquation[i] == '(-)':
            tempEquation[i] = '-'

        if tempEquation[i] == '( )':
            tempEquation[i] = ' '

    tempEquation.remove(' ')

    print(tempEquation)
    print(''.join(tempEquation))















    # for i in range(len(tempEquation)):
    #     if tempEquation[i] == '/':
    #
    #         print('what is up')
    #
    #         if tempEquation[i-1][0] == '(':
    #
    #             print('good')
    #
    #             counter = 1
    #
    #             while counter > 0:
    #                 temp_counter = 0
    #                 if temp_counter == 0:
    #                     counter = counter - 1
    #                     temp_counter == 1
    #                 for u in range(len(tempEquation[i-1])):
    #                     if tempEquation[i-1][u] == '(':
    #                         counter = counter + 1
    #                     elif tempEquation[i-1][u] == ')':
    #                         counter = counter - 1
    #
    #             print('hello')



sorting(user)

