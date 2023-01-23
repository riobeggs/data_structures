class Item:
    # Single item needs to know next item.
    # Returns own value
    def __init__(self) -> None:
        self._value = None
        self._next_item = None

    def __str__(self) -> str:
        return str(self._value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value) -> None:
        self._value = value

    @property
    def next_item(self):
        return self._next_item

    @next_item.setter
    def next_item(self, next_item) -> None:
        self._next_item = next_item

    # def has_next_item(self) -> bool:
    #     # if self.get_next_item == None:
    #     #     return False

    #     # return True

    #     return self._next_item is not None
