from gilded_rose import GildedRose, Item


def main():
    items = [
        Item('Backstage passes to a TAFKAL80ETC concert', 15, 0),
        Item('aged brie', 4, 10),
        Item('Sulfuras, Hand Of Ragnaros', 12345, 80)
    ]

    print("name - sell_in - quality")
    gr = GildedRose(items)
    for _ in range(6):
        gr.update_quality()
        print(gr.items)


if __name__ == "__main__":
    main()