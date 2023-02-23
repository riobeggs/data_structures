import unittest

from parameterized import parameterized

from assets.item import Item


class ValueTests(unittest.TestCase):
    """Tests value setter and getter methods."""

    @parameterized.expand(
        [
            (2,),
            (-2,),
            ("2",),
            ("two",),
        ]
    )
    def test_value(self, values: int | str):
        """Tests method can set and get a value for the item."""

        item = Item()
        item.value = values

        actual_value = item.value
        expected_value = values

        self.assertEqual(actual_value, expected_value)

    @parameterized.expand(
        [
            (2, 5),
            (-2, -5),
            ("2", "5"),
            ("two", "five"),
        ]
    )
    def test_override_value(self, values: int | str, override_values: int | str):
        """Tests method can override the items value without failure."""

        item = Item()
        item.value = values

        actual_value = item.value
        expected_value = values

        self.assertEqual(actual_value, expected_value)

        item.value = override_values

        actual_value = item.value
        expected_value = override_values

        self.assertEqual(actual_value, expected_value)


class NextNodeTests(unittest.TestCase):
    """Tests next node setter and getter methods."""

    @parameterized.expand([(1, 2), ("1", "2"), (1, "2")])
    def test_next_node(self, values: int | str, next_values: int | str):
        """Tests method can set and get a next node for the item."""

        item1 = Item()
        item1.value = values

        item2 = Item()
        item2.value = next_values

        item1.next_item = item2

        actual_next_item = item1.next_item
        expected_next_item = item2

        self.assertEqual(actual_next_item, expected_next_item)
