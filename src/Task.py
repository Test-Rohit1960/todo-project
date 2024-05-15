class Task:
    task_id_counter = [1]

    def __init__(self, task_name: str, priority: str):
        """
        Initialize a Task object.

        :param task_name: The name of the task.
        :param priority: The priority of the task.
        """
        self.__task_id = Task.task_id_counter[0]
        self.__task_name = task_name.casefold()
        self.__priority = str(priority).casefold()
        Task.task_id_counter[0] += 1

    def get_task_id(self) -> int:
        """
        Get the task ID.

        :return: The task ID.
        """
        return self.__task_id

    def get_task_name(self) -> str:
        """
        Get the task name.

        :return: The task name.
        """
        return self.__task_name

    def set_task_name(self, task_name: str) -> None:
        """
        Set the task name.

        :param task_name: The new task name.
        """
        self.__task_name = task_name

    def get_priority(self) -> str:
        """
        Get the task priority.

        :return: The task priority.
        """
        return self.__priority

    def set_priority(self, priority: str) -> None:
        """
        Set the task priority.

        :param priority: The new task priority.
        """
        self.__priority = priority

    def __str__(self) -> str:
        """
        Return a string representation of the task.

        :return: A string representation of the task.
        """
        return f"Task Id: {self.get_task_id()}\nTask Name: {self.get_task_name()}\nTask Priority: {self.get_priority()}"


task1 = Task("Buy Milk", "High")
task2 = Task("Buy soyabean", "Low")
