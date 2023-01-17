from item import SingleItem
from items import Items


def main():
    si = SingleItem()
    si2 = SingleItem()
    si.store_next_item(si2)
    assert si.has_next_item()
    # si.add(1)
    #
    # assert 1 == si.get_added_value()
    si.get_added_value()


def main2():
    si = SingleItem()
    si.add(1)
    i = Items()
    i.store_head(si)
    result = i.retrieve_head()

    print(result)


if __name__ == "__main__":
    main2()
