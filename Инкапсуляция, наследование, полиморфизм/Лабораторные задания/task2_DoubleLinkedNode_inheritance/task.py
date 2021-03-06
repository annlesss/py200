from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_  # вызовется setter

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_

# TODO реализовать класс DoubleLinkedNode


class DoubleLinkedNode(Node):
    def __init__( self, value: None, next_ = None, prev_ = None ):
        super().__init__(value, next_)
        self.prev = prev_

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev_: Optional[DoubleLinkedNode] = None):
        return self._prev


    def __repr__(self):
        next_repr: str = str(None) \
            if self.next is None \
            else f"DoubleLinkedNode({self.next.value}, {None}, {None})"
        prev_repr: str = str(None) \
            if self.prev is None \
            else f"DoubleLinkedNode({self.prev.value}, {None}, {None})"
        return f"DoubleLinkedNode({self.value}, {next_repr}, {prev_repr})"


    if __name__ == 'main':
        first_node = DoubleLinkedNode(1)
        second_node = DoubleLinkedNode(2)
        third_node = DoubleLinkedNode(3)
        fourth_node = DoubleLinkedNode(4)

        first_node.mext = second_node

        second_node.prev = first_node
        second_node.next = third_node

        third_node.prev = second_node
        third_node.next = fourth_node

        print(repr(first_node))
        print(repr(second_node))
        print(repr(third_node))


