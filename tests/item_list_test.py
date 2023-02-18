import unittest

from parameterized import parameterized

from assets.item_list import List as MyList


class InitTests(unittest.TestCase):
    """Tests initializer runs as it should."""

    @parameterized.expand([([2, 5, 1, 4, 3],), ([1],)])
    def test_initialize(
        self,
        input_data: list[int],
    ):
        """Tests we can initialize a wide range of inputs."""

        # Act
        item_list = MyList(input_data)

        # Arrange
        expected_length = len(input_data)
        length = len(item_list)

        # Assert
        self.assertEqual(length, expected_length)

    def test_initializing_none_fails(self):
        """Tests that initializer raises ValueError when None passed in."""

        input_data = None

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

    def test_adding_none_fails(self):
        """Tests that adding method raises a ValueError when trying to add None."""

        input_data = None

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

    def test_sorts_integers(self):
        """Tests we can sort a list of integers in ascending order."""

        input_data = [2, 5, 1, 4, 3, 0, -1]
        expected_list = "[-1, 0, 1, 2, 3, 4, 5]"

        item_list = MyList(input_data)

        item_list.sort_integers()
        sorted_list = str(item_list)

        self.assertEqual(sorted_list, expected_list)


class GetItemByIndexTests(unittest.TestCase):
    """Tests we can get an item in the list by its index."""

    def test_out_of_range_index_fails(self):
        """Tests method raises IndexError when index passed in is out of range."""

        input_data = [5, 10, 15, 20, 25]
        index = 7

        item_list = MyList(input_data)

        with self.assertRaises(IndexError):
            item_list.get(index)

    def test_wrong_index_type_fails(self):
        """Tests method raises TypeError when index passed in is not an integer."""

        input_data = [5, 10, 15, 20, 25]
        index = "7"

        item_list = MyList(input_data)

        with self.assertRaises(TypeError):
            item_list.get(index)

    def test_gets_item(self):
        """Tests gets correct item in list by index."""

        input_data = [5, 10, 15, 20, 25]
        index = 2
        expected_item = 15

        item_list = MyList(input_data)

        item = item_list.get(index)
        actual_item = item.value

        self.assertEqual(actual_item, expected_item)


class GetIndexOfItemTest(unittest.TestCase):
    """Tests we can get the index of an item in the list."""

    def test_gets_index(self):
        """Tests method retrieves correct index of an item in the list."""

        input_data = [2, 5, 1, 4, 3]
        item = 5
        expected_index = 1

        item_list = MyList(input_data)

        actual_index = item_list.get_index(item)

        self.assertEqual(actual_index, expected_index)

    def test_get_nonexistent_item_fails(self):
        """Tests method raises a ValueError when item is not in the list."""

        input_data = [2, 5, 1, 4, 3]
        item = 6

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

    def test_out_of_range_index_fails(self):
        """Tests method raises an IndexError when index is out of range."""

        input_data = [2, 5, 1, 4, 3]
        index = 6

        item_list = MyList(input_data)

        with self.assertRaises(IndexError):
            item_list.remove(index)
