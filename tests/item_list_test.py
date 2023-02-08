import unittest
from parameterized import parameterized

from assets.item_list import List as MyList


class Tests(unittest.TestCase):
    """Stop complaining about doc strings in tests."""

    @parameterized.expand(
        [([2, 5, 1, 4, 3], 2, 3), ([1], 1, 1), ([None], None, None), (None, None, None)]
    )
    def test_initialize(
        self,
        input_data: list[int] | None,
        expected_head: int | None,
        expected_tail: int | None,
    ):
        """Tests we can initialize a wide range of inputs."""

        if input_data is not None:

            # Act
            item_list = MyList(input_data)

            # Arrange
            expected_length = len(input_data)
            head = input_data[0]
            tail = input_data[-1]
            length = len(item_list)

            # Assert
            self.assertEqual(head, expected_head)
            self.assertEqual(tail, expected_tail)
            self.assertEqual(length, expected_length)

        else:

            with self.assertRaises(TypeError):
                MyList(input_data)

    @parameterized.expand(
        [
            (
                [2, 5, 1, 4, 3],
                "['test', '2', '5', '1', '4', '3']",
            ),
            (
                1,
                "['test', '1']",
            ),
            (
                "Hello",
                "['test', 'Hello']",
            ),
            (
                None,
                "['test']",
            ),
        ]
    )
    def test_adding(
        self,
        input_data: list[int] | None,
        expected_list,
    ):
        """Tests we can add different data types to the item list."""

        # Act
        item_list = MyList("test")

        if input_data is None:
            with self.assertRaises(ValueError):
                item_list.add(input_data)
        else:
            item_list.add(input_data)

        # Assert
        self.assertEqual(str(item_list), expected_list)

    @parameterized.expand(
        [
            (
                [2, 0, 1, -13, 5, 4, 1000009, 3],
                "['-13', '0', '1', '2', '3', '4', '5', '1000009']",
            ),
            (
                [1, "Hello"],
                None,
            ),
            (
                ["Hello"],
                "['Hello']",
            ),
            (
                [1],
                "['1']",
            ),
        ]
    )
    def test_integer_sorting(self, data, expected):
        """Tests we can sort a list of integers in ascending order."""

        item_list = MyList(data)

        if all(isinstance(value, int) for value in data):
            item_list.sort()
            actual = str(item_list)
            self.assertEqual(actual, expected)

        elif all(isinstance(value, str) for value in data):
            item_list.sort()
            actual = str(item_list)
            self.assertEqual(actual, expected)

        else:
            with self.assertRaises(TypeError):
                item_list.sort()
