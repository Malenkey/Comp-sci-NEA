comparison_list = ["one", "two", "three"]

match comparison_list:
    case ['one']:
        print("this is the first element: {first}")
    case [first, *rest]:
        print("This is the first: {first}, and this is the rest: {rest}")
    case _:
        print("Nothing was matched")



def sorting():
    finished = False
    equation = []
    while not finished:
        user = input('put something in')
        match user:
            case 'sin':

                trigvalue = input('enter what value of sin you would like the graph to take')
                equation.append('sin'+'('+trigvalue+')')
                equation.append(' ')
                print(equation)

            case 'cos':
                trigvalue = input('enter what value of cos you would like the graph to take')
                equation.append('cos' + '(' + trigvalue + ')')
                equation.append(' ')
                print(equation)














sorting()
