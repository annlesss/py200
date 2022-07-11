from task import Node
import unittest


class Test_Node(unittest.TestCase):

    def test_link_node(self):
        """Проверка на связь узлов"""
        second_node = Node('second_node')
        first_node = Node('first_node', next_= second_node)
        expected_value = second_node
        actual_value = first_node.next
        self.assertIs(expected_value, actual_value, msg = "Узлы не связались")

    def test_str(self):
        some_value = 3
        node = Node(some_value)
        expected_value= str(some_value)

        self.assertEqual(expected_value, str(node))
        self.assertEqual(expected_value, f"{node}")