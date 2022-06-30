class Node:
    """ Класс, который описывает узел связного списка. """
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return f"(node for node in self)"

    def __repr__(self):
        pass

    def is_valid(self):
        pass




class DoubleLinkedNode(Node):
    ...


if __name__ == "__main__":
    ...
