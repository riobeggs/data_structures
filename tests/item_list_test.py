import unittest

from assets.item_list import List as MyList


class TestSorting(unittest.TestCase):
    """Stop complaining about doc strings in tests."""

    def test_initialize(self):
        """Tests we can initialize a wide range of inputs."""
        items: list[int] = [2, 5, 1, 4, 3]
        item_list: List = MyList(items)
        # item_list.add([2, 5, 1, 4, 3])

        self.assertEqual(item_list.tail.value, 3)
        self.assertEqual(item_list.head.value, 2)

        for index, item in enumerate(items):
            pass

        test = [item.value for item in item_list]
        expected = items
        self.assertEqual(test, expected)

        # # Arrange
        # expected: list[int] = [1, 2, 3, 4, 5]

        # # Act
        # item_list.sort()

        # # Assert
        # self.assertEqual(item_list, expected)

        # # print(item_list)
