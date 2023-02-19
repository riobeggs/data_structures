from typing import List as TList

from assets.item import Item


class List:
    """
    A list class for storing items.
    An item has a reference to the next item, but not the previous item.
    """

    # Stores head
    # Iterate over all items
    # Can return specific item
    # Can sort items (optional)

    def __init__(self, items: int | list[int]) -> None:
        self._current: None | Item = None
        self._head: None | Item = None
        self._tail: None | Item = None
        self._index: None | int = None
        self._length: int = 0

        if items is None:
            raise ValueError("Cannot add None to list")

        if isinstance(items, list):

            previous_item: None | Item = None

            for index, value in enumerate(items):
                self._length += 1

                item: Item = Item()
                item.value = value

                if previous_item is None:
                    previous_item = item
                    self._head = item

                else:
                    previous_item.next_item = item

                if (index + 1) is len(items):
                    self._tail = item

                previous_item = item

        else:
            item: Item = Item()
            item.value = items
            self._head = item
            self._tail = item

    def __str__(self) -> str:
        items = []
        for item in self:
            items.append(item.value)

        item_list = f"{items}"

        return item_list

        # items = ", ".join([f"{str(item)}" for item in self])
        # item_list = f"[{items}]"

        # return item_list

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

    def add(self, items: Item | TList[Item] | int | str) -> None:
        """
        Adds an item or list of items to the list.
        """
        if items is None:
            raise ValueError("Cannot add None to list")

        if not isinstance(items, list):
            items = [items]

        for val in items:

            item: Item = Item()
            item.value = val
            self._length += 1

            if self._tail is not None:
                current_tail = self._tail
                current_tail.next_item = item
                item.next_item = None
                self._tail = item

            else:
                self._head = item
                self._tail = item

    def _index_is_valid(self, index: int) -> bool:
        """
        Reports if a given index is valid regarding length of list.

        Raises a TypeError if given index is not an integer.
        Raises an IndexError if index is out of range.
        """

        if not isinstance(index, int):
            try:
                index = int(index)
            except Exception as exc:
                raise TypeError(f"{index} is not an integer") from exc

        if index >= self._length:
            raise IndexError(f"{index} is out of range")

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

    def get_index(self, chosen_item: Item | int) -> int:
        """
        Retrieves the index for an item in the list.

        Raises a value error is the item doesnt exist.
        """
        if isinstance(chosen_item, Item):
            for item in self:
                if item is chosen_item:

                    return self._index

            raise ValueError(f"{chosen_item} is not in list")

        for item in self:
            if item.value is chosen_item:

                return self._index

        raise ValueError(f"{chosen_item} is not in list")

    def sort_integers(self) -> None:
        """
        Sorts the list in ascending order.
        """
        previous_node = None
        items_sorted: bool = False

        # INTEGERS
        while not items_sorted:

            for item in self:

                current_node = item
                next_node = item.next_item

                if not isinstance(current_node.value, int):
                    raise TypeError("Cannot sort non-integers")

                if next_node is not None and not isinstance(
                    current_node.value, type(next_node.value)
                ):
                    raise TypeError(
                        f"Cannot sort both {type(current_node.value)} and {type(next_node.value)}"
                    )

                # If end of list, items are sorted.
                if current_node is self._tail:
                    items_sorted = True
                    break

                if current_node.value > next_node.value:

                    if current_node is self._head:
                        self._head = next_node
                        previous_node = current_node

                    elif next_node.next_item is None:
                        self._tail = current_node
                        previous_node.next_item = next_node

                    else:
                        previous_node.next_item = next_node

                    previous_node = current_node
                    current_node.next_item = next_node.next_item
                    next_node.next_item = current_node
                    break

                previous_node = current_node
