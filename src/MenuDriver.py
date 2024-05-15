import UtilityFunctions as utilsF

todo_lists = list()
want = input("Do you want to create a new todo list (N/Y): ").casefold()
if want == 'y':
    todo_lists.append(utilsF.create_todo_list())

while True:
    if len(todo_lists) == 0:
        break
    print("Todo List created: ", list(enumerate(todo_lists)))
    index = int(input("Enter the index of todo list to select it: "))
    selected_todo_list = todo_lists[index]
    utilsF.menu_driver(selected_todo_list)

    choice = input("Do you want to quit (Y/*): ").casefold()
    if choice == 'y':
        break



