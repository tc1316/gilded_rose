from dataclasses import dataclass, field
from typing import List


@dataclass
class GildedRose:
    items: List = field(default_factory=list)
    # special_items = ["Aged Brie", "Sulfuras, Hand of Ragnaros", "Backstage passes", "Conjured"]

    def update_quality(self):
        for item in self.items:
            # Base case
            item.sell_in -= 1
            delta_quality = -1
            max_quality = 50

            # Sulfuras case
            if item.name.title() == "Sulfuras, Hand Of Ragnaros":
                item.sell_in += 1
                delta_quality = 0
                max_quality = 80

            # Aged Brie case
            elif item.name.title() == "Aged Brie":
                delta_quality = 1

            # Backstage pass case
            elif "Backstage passes" in item.name:
                if item.sell_in >= 10:
                    delta_quality = 1
                if 5 <= item.sell_in <= 9:
                    delta_quality = 2
                elif 0 <= item.sell_in <= 4:
                    delta_quality = 3
                elif item.sell_in < 0:
                    item.quality = 0
                    continue

            if item.quality >= 0:
                if item.sell_in < 0:
                    item.quality += delta_quality * 2
                else:
                    item.quality += delta_quality
                if item.quality < 0:
                    item.quality = 0

            item.quality = min(max_quality, item.quality)

            # if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
            #     if item.quality > 0:
            #         if item.name != "Sulfuras, Hand of Ragnaros":
            #             item.quality = item.quality - 1
            # else:
            #     if item.quality < 50:
            #         item.quality = item.quality + 1
            #         if item.name == "Backstage passes to a TAFKAL80ETC concert":
            #             if item.sell_in < 11:
            #                 if item.quality < 50:
            #                     item.quality = item.quality + 1
            #             if item.sell_in < 6:
            #                 if item.quality < 50:
            #                     item.quality = item.quality + 1
            # if item.name != "Sulfuras, Hand of Ragnaros":
            #     item.sell_in = item.sell_in - 1
            # if item.sell_in < 0:
            #     if item.name != "Aged Brie":
            #         if item.name != "Backstage passes to a TAFKAL80ETC concert":
            #             if item.quality > 0:
            #                 if item.name != "Sulfuras, Hand of Ragnaros":
            #                     item.quality = item.quality - 1
            #         else:
            #             item.quality = item.quality - item.quality
            #     else:
            #         if item.quality < 50:
            #             item.quality = item.quality + 1

    def update_quality_n_times(self, num):
        for _ in range(num):
            self.update_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
