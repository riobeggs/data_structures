from item import SingleItem


class Items:
    # Stores head
    # Iterate over all items
    # Can return specific item
    # Can sort items (optional)
    _head = None
    _tail = None
    _current = None
    _index = 0

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
        # If tail
        elif self._current is self._tail:
            self._current = None
            self._index += 1
            raise StopIteration
        # If next item
        elif self._current.has_next_item():
            self._current = self._current.get_next_item()
            self._index += 1

        return self._current

    def get_item_by_index(self, index: int):
        for _ in self:
            if self._index == index:
                return self._current

        raise IndexError(f"Index {index} is out of range")

    def store_head(self, head: SingleItem):
        if not isinstance(head, SingleItem):
            raise Exception(f"{head} is not an instance of a SingleItem")

        self._head = head

    def retrieve_head(self) -> SingleItem:
        return self._head

    def store_tail(self, tail: SingleItem):
        if not isinstance(tail, SingleItem):
            raise Exception(f"{tail} is not an instance of a SingleItem")

        self._tail = tail

    def retrieve_tail(self) -> SingleItem:
        return self._tail

    def is_empty(self) -> bool:
        return self._head is None

    def remove_item(self, delete_item: SingleItem):
        if not isinstance(delete_item, SingleItem):
            raise Exception(f"{delete_item} is not an instance of a SingleItem")

        for item in self:

            if item is self._head:

                if item is delete_item:
                    self.store_head(item.get_next_item())
                    break

            if item.get_next_item() is delete_item:

                if item.get_next_item() is self._tail:
                    self.store_tail(item)
                    break

                item.store_next_item(delete_item.get_next_item())
                break
