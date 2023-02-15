import unittest

from parameterized import parameterized

from assets.item_list import List as MyList


class InitTests(unittest.TestCase):
    """Tests initializer runs as it should."""

    @parameterized.expand([([2, 5, 1, 4, 3], 2, 3), ([1], 1, 1)])
    def test_initialize(
        self,
        input_data: list[int],
        expected_head: int,
        expected_tail: int,
    ):
        """Tests we can initialize a wide range of inputs."""

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

    @parameterized.expand([([None])])
    def test_initializing_none_fails(self, input_data: None):
        """Tests that initializer raises ValueError when None passed in."""

        with self.assertRaises(ValueError):
            MyList(input_data)


class AddingTests(unittest.TestCase):
    """Tests method for adding items to the list."""

    @parameterized.expand(
        [
            (
                [2, 5, 1, 4, 3],
                "['test', 2, 5, 1, 4, 3]",
                3,
            ),
            (
                1,
                "['test', 1]",
                1,
            ),
            (
                "Hello",
                "['test', 'Hello']",
                "Hello",
            ),
        ]
    )
    def test_adding(
        self, input_data: list, expected_list: list, expected_tail: int | str
    ):
        """Tests we can add different data types to the item list."""

        # Act
        item_list = MyList("test")
        item_list.add(input_data)

        actual_list = str(item_list)
        actual_tail = item_list.tail.value

        # Assert
        self.assertEqual(actual_list, expected_list)
        self.assertEqual(actual_tail, expected_tail)

    @parameterized.expand([([None])])
    def test_adding_none_fails(self, input_data: None):
        """Tests that adding method raises a ValueError when trying to add None."""

        item_list = MyList("test")

        with self.assertRaises(ValueError):
            item_list.add(input_data)


class IntegerSortingTests(unittest.TestCase):
    """Tests that sorting method runs as it should."""

    @parameterized.expand(
        [
            ([1, "Fail"],),
            (["Fail1", "Fail2"],),
        ]
    )
    def test_sorting_non_integers_fails(self, input_data: list):
        """Tests sorting method raises TypeError when to sorting items that are not integers."""

        item_list = MyList(input_data)

        with self.assertRaises(TypeError):
            item_list.sort_integers()

    @parameterized.expand([([2, 5, 1, 4, 3, 0, -1], "[-1, 0, 1, 2, 3, 4, 5]")])
    def test_sorts_integers(self, input_data: list[int], expected_list: str):
        """Tests we can sort a list of integers in ascending order."""

        item_list = MyList(input_data)

        item_list.sort_integers()
        sorted_list = str(item_list)

        self.assertEqual(sorted_list, expected_list)


class GetItemByIndexTests(unittest.TestCase):
    """Tests we can get an item in the list by its index."""

    @parameterized.expand([([5, 10, 15, 20, 25], 7)])
    def test_out_of_range_index_fails(self, input_data: list[int], index: int):
        """Tests method raises IndexError when index passed in is out of range."""

        item_list = MyList(input_data)

        with self.assertRaises(IndexError):
            item_list.get(index)

    @parameterized.expand([([5, 10, 15, 20, 25], "7")])
    def test_wrong_index_type_fails(self, input_data: list[int], index: str):
        """Tests method raises TypeError when index passed in is not an integer."""

        item_list = MyList(input_data)

        with self.assertRaises(TypeError):
            item_list.get(index)

    @parameterized.expand([([5, 10, 15, 20, 25], 2, 15)])
    def test_gets_item(self, input_data: list[int], index: int, expected_item: int):
        """Tests gets correct item in list by index."""

        item_list = MyList(input_data)

        item = item_list.get(index)
        actual_item = item.value

        self.assertEqual(actual_item, expected_item)


class GetIndexOfItemTest(unittest.TestCase):
    """Tests we can get the index of an item in the list."""

    @parameterized.expand([([2, 5, 1, 4, 3], 5, 1)])
    def test_gets_index(self, input_data: list[int], item: int, expected_index: int):
        """Tests method retrieves correct index of an item in the list."""

        item_list = MyList(input_data)

        actual_index = item_list.get_index(item)

        self.assertEqual(actual_index, expected_index)

    @parameterized.expand([([2, 5, 1, 4, 3], 6)])
    def test_get_nonexistent_item_fails(self, input_data: list[int], item: int):
        """Tests method raises a ValueError when item is not in the list."""

        item_list = MyList(input_data)

        with self.assertRaises(ValueError):
            item_list.get_index(item)


class RemovingTests(unittest.TestCase):
    """Tests we can remove an item by index."""

    @parameterized.expand(
        [
            ([1, 2, 3, 4, 5], 0, "[2, 3, 4, 5]"),
            ([1, 2, 3, 4, 5], 4, "[1, 2, 3, 4]"),
            ([1, 2, 3, 4, 5], 2, "[1, 2, 4, 5]"),
        ]
    )
    def test_removes_item(self, input_data: list[int], index: int, expected_list: str):
        """Tests method removes correct item."""

        item_list = MyList(input_data)

        item_list.remove(index)
        actual_list = str(item_list)

        self.assertEqual(actual_list, expected_list)

    @parameterized.expand([([1, 2, 3, 4, 5], 6)])
    def test_out_of_range_index_fails(self, input_data: list[int], index: int):
        """Tests method raises an IndexError when index is out of range."""

        item_list = MyList(input_data)

        with self.assertRaises(IndexError):
            item_list.remove(index)
