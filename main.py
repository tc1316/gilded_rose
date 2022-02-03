from gilded_rose import AgedBrie, CustomItemFactory, GildedRose, Item


def main():
    items = [
        Item('Backstage passes to a TAFKAL80ETC concert', 15, 0),
        Item('aged brie', 4, 10),
        Item('Sulfuras, Hand Of Ragnaros', 12345, 80)
    ]
    items = [
        Item('aged brie', 4, 10),
    ]

    

    print("name - sell_in - quality")
    gr = GildedRose(items)
    print(gr.parsed_items)

    for _ in range(6):
        gr.update_quality()
        print(gr.parsed_items)


if __name__ == "__main__":
    main()
