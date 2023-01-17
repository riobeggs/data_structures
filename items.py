from item import SingleItem


class Items:
    # Stores head
    # Iterate over all items
    # Can return specific item
    # Can sort items (optional)
    _head = None

    # def __iter__()

    # def get_item_by_index()

    def store_head(self, head: SingleItem):
        if not isinstance(head, SingleItem):
            raise Exception(f"{head} is not an instance of a SingleItem")

        self._head = head

    def retrieve_head(self) -> SingleItem:
        return self._head

    def is_empty(self) -> bool:
        return self._head is None
