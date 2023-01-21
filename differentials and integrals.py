user = input("type something bozo")






def differential(equation):
    temp = []
    equation = str(equation)
    for i in equation:
        temp.append(i)

    for i in range (len(temp)):
        if ''.join(temp[i:i+6]) == 'sin(x)':
            element = 'np.sin(x)'
            print(element)



def integral(equation):
    equation = str(equation)


differential(user)