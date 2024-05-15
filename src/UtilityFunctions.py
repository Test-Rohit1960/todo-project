from src.Task import Task
from TodoList import TodoList


def create_todo_list() -> TodoList:
    """
    Create a todo list.

    :return: The created todo list object.
    """
    no_of_priorities = int(input("How many priorities do you want to create: "))
    priority_names = [input("Enter a priority name: ").casefold() for _ in range(no_of_priorities)]
    todo_list_obj = TodoList(no_of_priorities)
    todo_list_obj.create_priority_map(*priority_names)
    print("Todo list created")
    return todo_list_obj


def create_task(todo_list: TodoList) -> None:
    """
    Create a task and add it to the todo list.

    :param todo_list: The todo list to which the task will be added.
    """
    task_name = input("Enter the task name: ").casefold()
    task_priority = input("Set a task priority: ").casefold()
    task = Task(task_name, task_priority)
    print(todo_list.add_task(task))


def edit_task(todo_list: TodoList) -> None:
    """
    Edit a task in the todo list.

    :param todo_list: The todo list containing the task to be edited.
    """
    task_name = input("Enter the task name you want to edit: ").casefold()
    task = todo_list.search_task(task_name)

    if isinstance(task, str):
        print(task)
        return

    field = input("Do you want to edit the task name or its priority or both (N/P/B): ").casefold()
    if field == 'n' or field == 'b':
        new_task_name = input("Enter the new task name: ").casefold()
        task.set_task_name(new_task_name)
        temp = todo_list.hash_map[task_name]
        del todo_list.hash_map[task_name]
        todo_list.hash_map[new_task_name] = temp
        task_name = new_task_name

    if field == 'p' or field == 'b':
        new_priority = input("Enter the new priority: ").casefold()
        if new_priority in todo_list.priority_map.keys():
            todo_list.remove_task(task_name)
            new_task = Task(task_name, new_priority)
            print(todo_list.add_task(new_task))
        else:
            print("Priority not found")
            return
    print("Task edited!")


def list_tasks(todo_list: TodoList) -> None:
    """
    List all tasks in the todo list.

    :param todo_list: The todo list to be listed.
    """
    print(todo_list)


def delete_task(todo_list: TodoList) -> None:
    """
    Delete a task from the todo list.

    :param todo_list: The todo list containing the task to be deleted.
    """
    task_name = input("Enter task name to be deleted: ").casefold()
    print(todo_list.remove_task(task_name))


def search_task(todo_list: TodoList) -> None:
    """
    Search for a task in the todo list.

    :param todo_list: The todo list to search for the task.
    """
    task_name = input("Enter task name to be searched: ")
    task = todo_list.search_task(task_name)
    print(task)


def tasks_backup(todo_list: TodoList) -> None:
    """
    Take backup of the todo list tasks.

    :param todo_list: The todo list to backup.
    """
    string = todo_list.__str__()
    with open('backup.txt', 'a+') as backup:
        backup.write('\n')
        backup.write(string)


def menu_driver(todo_list: TodoList) -> None:
    """
    Drive the menu for the todo list operations.

    :param todo_list: The todo list to perform operations on.
    """
    while True:
        print("\nTODO App Menu:")
        print("1. Create Task")
        print("2. Edit Task")
        print("3. List Tasks")
        print("4. Delete Task")
        print("5. Search Tasks")
        print("6: Take backup")
        print("7. Quit")

        try:
            choice = int(input("Enter your choice: "))
            assert 1 <= choice <= 7
        except (ValueError, AssertionError):
            print("Invalid Choice. Please try again")
            continue

        if choice == 1:
            create_task(todo_list)
        elif choice == 2:
            edit_task(todo_list)
        elif choice == 3:
            list_tasks(todo_list)
        elif choice == 4:
            delete_task(todo_list)
        elif choice == 5:
            search_task(todo_list)
        elif choice == 6:
            tasks_backup(todo_list)
        elif choice == 7:
            return
