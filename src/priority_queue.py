from datetime import datetime


class TodoList:

    def __init__(self, no_of_priorities):
        self.no_of_priorities = no_of_priorities
        self.priority_map = dict()
        self.hash_map = dict()

    def create_priority_map(self, *priority_names):
        self.priority_map.fromkeys(priority_names, list())
        return "Priorities added"

    def add_task(self, task):
        if task.get_name() in self.hash_map:
            return "Duplicate entries are not allowed"
        self.priority_map[task.get_priority()].append(task)
        self.hash_map[task.get_name()] = task
        return f"{task.get_name()} added!"

    def remove_task(self, task_name):
        task_obj = self.search_task(task_name)
        del task_obj
        return f"{task_name} removed"

    def search_task(self, task_name):
        if task_name in self.hash_map:
            task_obj = self.hash_map[task_name]
            return task_obj
        return f"{task_name} not found"

    def get_no_of_priorities(self):
        return self.no_of_priorities

    def __repr__(self):
        return_str = f'''{datetime.now()}\n'''
        for priority in self.priority_map:
            return_str += f"Priority: {str(priority)}\n"
            for task in self.priority_map[priority]:
                return_str += f"{task.__repr__()}\n"
            return_str += "==============================================================\n"


