import UtilityFunctions as utilsF

todo_lists = list()


while True:
    want = input("Do you want to create a new todo list (Y/N): ").casefold()
    if want == 'y':
        todo_lists.append(utilsF.create_todo_list())
    elif want == 'n':
        if len(todo_lists) == 0:
            break
    print("Todo List created: ", list(enumerate(todo_lists)))
    index = int(input("Enter the index of todo list to select it: "))
    try:
        selected_todo_list = todo_lists[index]
    except IndexError:
        print("Index out of range. Please, try again")
        continue
    utilsF.menu_driver(selected_todo_list)

    choice = input("Do you want to quit (Y/*): ").casefold()
    if choice == 'y':
        break



