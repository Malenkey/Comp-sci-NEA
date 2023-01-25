comparison_list = ["one", "two", "three"]

match comparison_list:
    case [first]:
        print("this is the first element: {first}")
    case [first, *rest]:
        print("This is the first: {first}, and this is the rest: {rest}")
    case _:
        print("Nothing was matched")