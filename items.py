from item import Item


class List:
    # Stores head
    # Iterate over all items
    # Can return specific item
    # Can sort items (optional)
    def __init__(self) -> None:
        self._current = None
        self._head = None
        self._tail = None
        self._index = None

    def __str__(self) -> str:
        items = ", ".join([f'"{str(item)}"' for item in self])
        item_list = f"[{items}]"

        return item_list

    def __iter__(self):
        self._current = None
        return self

    def __next__(self):
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
        return self._head is None

    @property
    def head(self) -> Item:
        return self._head

    @head.setter
    def head(self, head):
        self._head = head

    @property
    def tail(self) -> Item:
        return self._tail

    @tail.setter
    def tail(self, tail):
        self._tail = tail

    def get_item(self, index: int):
        for _ in self:
            if self._index == index:
                return self._current

        raise IndexError(f"Index {index} is out of range")

    def remove_item(self, index: int):
        if not isinstance(index, int):
            raise Exception(f"{index} is not an integer.")

        for item in self:

            next_item = item.next_item
            # If no next item: Index is out of range
            if next_item is None:
                raise IndexError("Index out of range")

            # If current item is head
            if item is self._head:
                # If the heads is to be deleted
                if self._index is index:
                    # Store heads next item as head
                    self._head = self._head.next_item
                    break

            # If next item in list is to be deleted
            if self._index + 1 == index:
                # If next item is tail
                if next_item is self._tail:
                    # Store current item as tail
                    self._tail = item
                    break
                # Store deleted items next item as the current items next item
                item.next_item = next_item.next_item
                break
