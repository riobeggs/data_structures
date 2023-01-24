from typing import Any
from item import Item


class List:
    """
    A list class for storing items.
    An item has a reference to the next item, but not the previous item.
    """

    # Stores head
    # Iterate over all items
    # Can return specific item
    # Can sort items (optional)

    def __init__(self) -> None:
        self._current = None
        self._head = None
        self._tail = None
        self._index = None
        self._length = 0

    def __str__(self) -> str:
        items = ", ".join([f"'{str(item)}'" for item in self])
        item_list = f"[{items}]"

        return item_list

    def __len__(self) -> int:
        return self._length

    def __iter__(self):
        self._current = None
        return self

    def __next__(self) -> Item:
        # If first call return head
        # Get next item if there is one
        # Otherwise raise StopIteration

        if self.is_empty():
            raise StopIteration

        # If start of list
        if self._current is None:
            self._current = self._head
            self._index = 0
        # If end of list
        elif self._current.next_item is None:
            self._current = None
            self._index += 1
            raise StopIteration
        # If next item
        else:
            self._current = self._current.next_item
            self._index += 1

        return self._current

    def is_empty(self) -> bool:
        """
        Reports if list is empty.
        """
        return self._head is None

    @property
    def head(self) -> Item:
        """
        Retrieves head for the list.
        """
        return self._head

    @head.setter
    def head(self, head: Item) -> None:
        """
        Sets head for the list.
        """
        self._head = head

    @property
    def tail(self) -> Item:
        """
        Retrieves tail for the list.
        """
        return self._tail

    @tail.setter
    def tail(self, tail: Item) -> None:
        """
        Sets tail for the list.
        """
        self._tail = tail

    def add(self, items: Item | list) -> None:
        """
        Adds an item or list of items to the list.
        """
        if type(items) == list:
            for item in items:
                self._length += 1

                if self._tail is not None:
                    current_tail = self._tail
                    current_tail.next_item = item
                    item.next_item = None
                    self._tail = item

                else:
                    self._head = item
                    self._tail = item
        else:
            self._length += 1

            if self._tail is not None:
                current_tail = self._tail
                current_tail.next_item = items
                items.next_item = None
                self._tail = items

            else:
                self._head = items
                self._tail = items

    def _index_is_valid(self, index: int) -> bool:
        """
        Reports if a given index is valid regarding length of list.

        Raises a TypeError if given index is not an integer.
        Raises an IndexError if index is out of range.
        """
        try:
            index = int(index)
        except:
            raise TypeError(index, "is not an integer.")

        if index >= self._length:
            raise IndexError(index, "out of range.")

        return True

    def get(self, index: int) -> Item:
        """
        Retrieves an item in the list by given index.
        """
        if self._index_is_valid(index):
            for _ in self:
                if self._index == index:
                    return self._current

    def remove(self, index: int) -> None:
        """
        Removes an item in the list by given index.
        """
        if self._index_is_valid(index):

            for item in self:

                next_item = item.next_item

                # If current item is head
                if item is self._head:
                    # If the heads is to be deleted
                    if self._index is index:
                        self._length -= 1
                        # Store heads next item as head
                        self._head = self._head.next_item
                        break

                # If next item in list is to be deleted
                if self._index + 1 == index:
                    self._length -= 1
                    # If next item is tail
                    if next_item is self._tail:
                        # Store current item as tail
                        item.next_item = None
                        self._tail = item
                        break
                    # Store deleted items next item as the current items next item
                    item.next_item = next_item.next_item
                    break
