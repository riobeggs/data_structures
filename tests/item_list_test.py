import unittest

from parameterized import parameterized

from assets.item_list import List as MyList


class InitTests(unittest.TestCase):
    """Tests initializer runs as it should."""

    @parameterized.expand(
        [
            ([2, 5, 1, 4, 3],),
            (["2", "5", "1", "4", "3"],),
            ([1, "2", 3, "4", 5],),
            ([1],),
            (["Hi"],),
        ]
    )
    def test_initialize(
        self,
        input_data: list | int | str,
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

        input_data = [1, None, 3]
        expected_exception = "Cannot add None to list"

        with self.assertRaises(ValueError) as error_context:
            MyList(input_data)

        actual_exception = str(error_context.exception)

        self.assertEqual(actual_exception, expected_exception)

    def test_empty_initialize(self):
        """Tests we can initialize with no parameters and create an empty list."""

        expected_list = "[]"

        item_list = MyList()

        actual_list = str(item_list)

        self.assertEqual(actual_list, expected_list)


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
        expected_exception = "Cannot add None to list"

        item_list = MyList("test")

        with self.assertRaises(ValueError) as error_context:
            item_list.add(input_data)

        actual_exception = str(error_context.exception)

        self.assertEqual(actual_exception, expected_exception)


# class IntegerSortingTests(unittest.TestCase):
#     """Tests that sorting method runs as it should."""

#     def test_sorting_non_integers_fails(self):
#         """Tests sorting method raises TypeError when to sorting items that are not integers."""

#         input_data = ["Fail1", "Fail2"]
#         expected_exception = "Cannot sort non-integers"

#         item_list = MyList(input_data)

#         with self.assertRaises(TypeError) as error_context:
#             item_list.sort_integers()

#         actual_exception = str(error_context.exception)

#         self.assertEqual(actual_exception, expected_exception)

#     def test_sorting_multiple_types_fails(self):
#         """Tests sorting method raises TypeError when trying to sort a list of multiple types."""

#         input_data = [1, "2", 3]
#         expected_exception = "Cannot sort both <class 'int'> and <class 'str'>"

#         item_list = MyList(input_data)

#         with self.assertRaises(TypeError) as error_context:
#             item_list.sort_integers()

#         actual_exception = str(error_context.exception)

#         self.assertEqual(actual_exception, expected_exception)

#     def test_sorts_integers(self):
#         """Tests we can sort a list of integers in ascending order."""

#         input_data = [2, 5, 1, 4, 3, 0, -1]
#         expected_list = "[-1, 0, 1, 2, 3, 4, 5]"

#         item_list = MyList(input_data)

#         item_list.sort_integers()
#         sorted_list = str(item_list)

#         self.assertEqual(sorted_list, expected_list)


class GetItemByIndexTests(unittest.TestCase):
    """Tests we can get an item in the list by its index."""

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
        expected_exception = "6 is not in list"

        item_list = MyList(input_data)

        with self.assertRaises(ValueError) as error_context:
            item_list.get_index(item)

        actual_exception = str(error_context.exception)

        self.assertEqual(actual_exception, expected_exception)


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


class ValidIndexTests(unittest.TestCase):
    """Tests validation of an index for different inputs."""

    def test_out_of_range_index_fails(self):
        """Tests method raises an IndexError when index is out of range."""

        input_data = [1, 2, 3, 4, 5]
        index = 9
        expected_exception = "9 is out of range"

        item_list = MyList(input_data)

        with self.assertRaises(IndexError) as error_context:
            item_list._index_is_valid(index)

        actual_exception = str(error_context.exception)

        self.assertEqual(actual_exception, expected_exception)

    def test_wrong_index_type_fails(self):
        """Tests method raises TypeError when index passed in is not an integer."""

        input_data = [1, 2, 3, 4, 5]
        index = "three"
        expected_exception = "three is not an integer"

        item_list = MyList(input_data)

        with self.assertRaises(TypeError) as error_context:
            item_list._index_is_valid(index)

        actual_exception = str(error_context.exception)

        self.assertEqual(actual_exception, expected_exception)


class Sorting(unittest.TestCase):
    """Tests sorting method works as intended."""

    def test_sorting_multiple_types_fails(self):
        """Tests sorting method raises TypeError when trying to sort a list of multiple types."""

        input_data = [1, "2", 3]
        expected_exception = "Cannot sort both <class 'int'> and <class 'str'>"

        item_list = MyList(input_data)

        with self.assertRaises(TypeError) as error_context:
            item_list.sort()

        actual_exception = str(error_context.exception)

        self.assertEqual(actual_exception, expected_exception)

    def test_sorting_invalid_types_fails(self):
        """Tests the method only allows sorting a list of integers or strings."""

        input_data = [True, False]
        expected_exception = "Can only sort integers or strings"

        item_list = MyList(input_data)

        with self.assertRaises(TypeError) as error_context:
            item_list.sort()

        actual_exception = str(error_context.exception)

        self.assertEqual(actual_exception, expected_exception)

    def test_sorting_integers(self):
        """Tests we can sort a list of integers in ascending order."""

        input_data = [2, 5, 1, 4, 3, 0, -1]
        expected_list = "[-1, 0, 1, 2, 3, 4, 5]"

        item_list = MyList(input_data)

        item_list.sort()
        sorted_list = str(item_list)

        self.assertEqual(sorted_list, expected_list)

    def test_sorting_strings(self):
        """Tests we can sort a list of strings in ascending order."""

        input_data = [
            "hi",
            "bye",
            "byed",
            "-1",
            "byed",
            "z1",
            "23z",
            "-2",
            "ashd8uqwydadbuq",
            "ashd8uqaydadbuq",
        ]
        expected_list = "['-1', '-2', '23z', 'ashd8uqaydadbuq', 'ashd8uqwydadbuq', 'bye', 'byed', 'byed', 'hi', 'z1']"

        item_list = MyList(input_data)

        item_list.sort()
        sorted_list = str(item_list)

        self.assertEqual(sorted_list, expected_list)
