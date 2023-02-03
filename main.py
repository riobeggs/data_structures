from assets.item_list import List


def main():
    item_list = List([2, 5, 1, 4, 3])
    item_list.sort()

    print(item_list)


if __name__ == "__main__":
    main()
