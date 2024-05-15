from datetime import datetime
import src.Task as ts  # Assuming Task class is defined in src.Task
import re


class TodoList:
    """
    A class representing a todo list.
    """

    def __init__(self, no_of_priorities: int):
        """
        Initialize the TodoList.

        :param no_of_priorities: The number of priorities in the todo list.
        """
        self.priority_map = None
        self.no_of_priorities = no_of_priorities
        self.hash_map = dict()

    def create_priority_map(self, *priority_names: str) -> str:
        """
        Create a priority map for the todo list.

        :param priority_names: Names of the priorities.
        :return: A message indicating the priorities are added.
        """
        priority_names = tuple(map(lambda x: x.casefold(), priority_names))
        self.priority_map = dict.fromkeys(priority_names, None)
        return "Priorities added"

    def add_task(self, task: ts.Task) -> str:
        """
        Add a task to the todo list.

        :param task: The task to be added.
        :return: A message indicating the task is added.
        """
        if task.get_task_name() in self.hash_map:
            return "Duplicate entries are not allowed"
        if self.priority_map[task.get_priority()] is None:
            self.priority_map[task.get_priority()] = []
        self.priority_map[task.get_priority()].append(task)
        self.hash_map[task.get_task_name()] = task
        return f"{task.get_task_name()} added!"

    def remove_task(self, task_name: str) -> str:
        """
        Remove a task from the todo list.

        :param task_name: The name of the task to be removed.
        :return: A message indicating the task is removed.
        """
        task_name = task_name.casefold()
        task_obj = self.search_task(task_name)
        try:
            self.priority_map[task_obj.get_priority()].remove(task_obj)
        except AttributeError:
            return f"{task_name} is not present in the list"
        del task_obj
        del self.hash_map[task_name]
        return f"{task_name} removed"

    def search_task(self, task_name: str):
        """
        Search for a task in the todo list.

        :param task_name: The name of the task to search for.
        :return: The task object if found, otherwise a message indicating the task is not found.
        """
        # tasks = list()
        task_name = task_name.lower()
        if task_name in self.hash_map:
            task_obj = self.hash_map[task_name]
            # tasks.append(task_obj)
            return task_obj

        # tasks = []
        # for key in self.hash_map.keys():
        #     match = re.fullmatch(task_name, key)
        #     if match:
        #         tasks.append(self.hash_map[key])  # Append the value associated with the matching key
        #
        # # After the loop, you can return the list of tasks or process it further
        # return tasks

    def get_no_of_priorities(self) -> int:
        """
        Get the number of priorities in the todo list.

        :return: The number of priorities.
        """
        return self.no_of_priorities

    def __str__(self) -> str:
        """
        Return a string representation of the todo list.

        :return: A string representation of the todo list.
        """
        return_str = f'''{datetime.now()}\nTodolist Id: {id(self)}\n'''
        for priority in self.priority_map:
            return_str += f"Priority: {str(priority)}\n"
            if self.priority_map[priority] is None:
                return_str += "==============================================================\n"
                continue
            for task in self.priority_map[priority]:
                return_str += f"{task.__str__()}\n"
            return_str += "==============================================================\n"
        return return_str



if __name__ == "__main__":
    todolist1 = TodoList(3)
    todolist1.create_priority_map("High", "Med", "Low")
    todolist1.add_task(ts.task1)
    todolist1.add_task(ts.task2)
    print(todolist1.search_task("buy*"))
    print(todolist1)
