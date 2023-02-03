from assets.item_list import List


def main():
    item_list = List([2, 3, 7, 43, 2, 6, 87, 3, 5, 132, 0, -13, 14])
    item_list.sort()

    print(item_list)


if __name__ == "__main__":
    main()
