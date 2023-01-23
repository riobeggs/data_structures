from item import Item
from items import List


# def main():
#     si = Item()
#     si2 = Item()
#     si.next_item(si2)
#     assert si.has_next_item()
#     # si.add(1)
#     #
#     # assert 1 == si.get_added_value()
#     si.value()


# def main2():
#     si = Item()
#     si.value(1)
#     i = List()
#     i.set_head(si)
#     result = i.head()

#     print(result)


# def main3():
#     si1 = Item()
#     si1.value(1)
#     si2 = Item()
#     si2.value(2)
#     si3 = Item()
#     si3.value(3)
#     si1.next_item(si2)
#     si2.next_item(si3)
#     i = List()
#     i.set_head(si1)
#     for item in i:
#         print(item)


# def main4():
#     si1 = Item()
#     si1.value("a")
#     si2 = Item()
#     si2.value("b")
#     si3 = Item()
#     si3.value("c")
#     si4 = Item()
#     si4.value("d")
#     si5 = Item()
#     si5.value("e")

#     si1.next_item(si2)
#     si2.next_item(si3)
#     si3.next_item(si4)
#     si4.next_item(si5)

#     item_list = List()

#     item_list.set_head(si1)
#     item_list.set_tail(si5)

#     result = item_list.get_item_by_index(3)
#     print(result)


# def main5():
#     si1 = Item()
#     si1.set_value("a")
#     si2 = Item()
#     si2.set_value("b")
#     si3 = Item()
#     si3.set_value("c")
#     si4 = Item()
#     si4.set_value("d")
#     si5 = Item()
#     si5.set_value("e")

#     si1.set_next_item(si2)
#     si2.set_next_item(si3)
#     si3.set_next_item(si4)
#     si4.set_next_item(si5)

#     item_list = List()
#     item_list.set_head(si1)
#     item_list.set_tail(si5)

#     item_list.remove_item_by_index(3)

#     for item in item_list:
#         print(item)


def main6():
    item1 = Item()
    item1.value = "a"
    item2 = Item()
    item2.value = "b"
    item3 = Item()
    item3.value = "c"

    item1.next_item = item2
    item2.next_item = item3

    item_list = List()
    item_list.head = item1
    item_list.tail = item3

    print(item_list)


if __name__ == "__main__":
    main6()
