from gilded_rose import GildedRose, Item


def main():
    items = [
        Item('aged brie', 4, 10),
        Item('sulfuras, hand of ragnaros', 12345, 80),
        Item('backstage passes to a random concert', 15, 0),
        Item("Foo", 15, 10),
        Item("conjured Foo", 15, 10)
    ]

    print("name - sell_in - quality")
    gilded_rose = GildedRose(items)
    print(gilded_rose.parsed_items)

    for _ in range(16):
        gilded_rose.update_quality()
        print(gilded_rose.parsed_items)


if __name__ == "__main__":
    main()
