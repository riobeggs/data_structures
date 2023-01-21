class SingleItem:
    # Single item needs to know next item.
    # Returns own value
    _value = None
    _next_item = None

    def __str__(self) -> str:
        # return f"SingleItem({self._value})"
        return str(self._value)

    def add(self, value):
        self._value = value

    def value(self):
        return self._value

    def set_next_item(self, next_item: "SingleItem"):
        if not isinstance(next_item, SingleItem):
            raise Exception(f"{next_item} is not an instance of a SingleItem")
        self._next_item = next_item

    def next_item(self) -> "SingleItem":
        return self._next_item

    def has_next_item(self) -> bool:
        # if self.get_next_item == None:
        #     return False

        # return True

        return self._next_item is not None
