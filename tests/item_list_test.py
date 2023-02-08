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

            with self.assertRaises(ValueError):
                MyList(input_data)

    @parameterized.expand(
        [
            (
                [2, 5, 1, 4, 3],
                "['test', '2', '5', '1', '4', '3']",
                3,
            ),
            (
                1,
                "['test', '1']",
                1,
            ),
            (
                "Hello",
                "['test', 'Hello']",
                "Hello",
            ),
            (
                None,
                "['test']",
                "test",
            ),
        ]
    )
    def test_adding(
        self,
        input_data: list[int] | None,
        expected_list,
        expected_tail,
    ):
        """Tests we can add different data types to the item list."""

        # Act
        item_list = MyList("test")

        if input_data is None:
            with self.assertRaises(ValueError):
                item_list.add(input_data)
        else:
            item_list.add(input_data)

        actual_tail = item_list.tail.value

        # Assert
        self.assertEqual(str(item_list), expected_list)
        self.assertEqual(actual_tail, expected_tail)

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

    @parameterized.expand(
        [
            (
                [2, 5, 1, 4, 3],
                1,
                7,
                "not_an_int",
                5,
            )
        ]
    )
    def test_get_item_by_index(
        self,
        data,
        index,
        out_of_range_index,
        not_an_int_index,
        expected,
    ):
        """Tests we can get an item by its index."""

        item_list = MyList(data)

        item = item_list.get(index)
        actual = item.value

        self.assertEqual(
            actual,
            expected,
        )
        with self.assertRaises(IndexError):
            item_list.get(out_of_range_index)
        with self.assertRaises(TypeError):
            item_list.get(not_an_int_index)

    @parameterized.expand(
        [
            (
                [2, 5, 1, 4, 3],
                4,
                3,
                "fail",
            )
        ]
    )
    def test_get_index_of_item(self, data, value, expected_index, invalid_value):
        """Tests we can get the index of an item in the list."""

        item_list = MyList(data)
        chosen_item = None

        for item in item_list:
            if item.value is value:
                chosen_item = item

        actual_index = item_list.get_index(chosen_item)

        self.assertEqual(actual_index, expected_index)
        with self.assertRaises(ValueError):
            item_list.get_index(invalid_value)

    @parameterized.expand(
        [
            (
                [2, 5, 1, 4, 3],
                2,
                "['2', '5', '4', '3']",
                10,
            )
        ]
    )
    def test_removing(self, data, index, expected, out_of_range_index):
        """Tests we can remove an item by index."""

        item_list = MyList(data)
        item_list.remove(index)

        actual = str(item_list)

        self.assertEqual(actual, expected)

        with self.assertRaises(IndexError):
            item_list.remove(out_of_range_index)
