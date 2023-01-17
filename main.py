from item import SingleItem


def main():
    si = SingleItem()
    si2 = SingleItem()
    si.store_next_item(si2)
    assert si.has_next_item()
    # si.add(1)
    #
    # assert 1 == si.get_added_value()
    si.get_added_value()


if __name__ == "__main__":
    main()
