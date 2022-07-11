from collections.abc import MutableSequence
from typing import Any, Optional, Iterable
from node import Node
from node import DoubleLinkedNode


class LinkedList(MutableSequence):

    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None
        self.tail = self.head
        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """Добавление элеменка в конец связного списка"""
        append_node = Node(value)
        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node
        self.len +=1

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] ):
        """
        Функция, которая связывает два узла
        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    def step_by_step_on_nodes(self, index: int):
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError
        if not 0 <= index < self.len:
            raise IndexError
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node

    def __getitem__(self, index: int):
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """Метод устанавливает значение узла по указанному индексу"""
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, key):
        """Удаление элемента по ключу"""
        if not isinstance(key, int):
            raise TypeError
        del Node[key]

    def __len__(self):
        return len(self.step_by_step_on_nodes(index=0))

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def insert(self, index: int, value: Any) -> None:
        """Вставка значения по указанному индексу"""
        node_value = self.step_by_step_on_nodes(index)
        return node_value


class DoubleLinkedList(LinkedList):
    @staticmethod
    def linked_nodes(left_node: DoubleLinkedNode, right_node: Optional[DoubleLinkedNode] = None) -> None:
        left_node.next = right_node
        right_node.prev = left_node

    def append(self, value: Any):
        append_node = DoubleLinkedNode(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1


if __name__ == "__main__":
    dllist = DoubleLinkedList()
    dllist.append(1)
    dllist.append(2)
    dllist.append(3)
    dllist.append(4)
    print(repr(dllist))
    print(str(dllist))
    print(dllist.len)
    print(dllist.to_list())
