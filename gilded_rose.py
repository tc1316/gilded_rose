from dataclasses import dataclass, field
from typing import List


@dataclass
class GildedRose:
    items: List = field(default_factory=list)
    parsed_items: List = field(default_factory=list, init=False)

    def __post_init__(self):
        for item in self.items:
            item.name = item.name.title()
            if item.name == "Aged Brie":
                self.parsed_items.append(
                    AgedBrie(item.name, item.sell_in, item.quality))
            elif item.name == "Sulfuras, Hand Of Ragnaros":
                self.parsed_items.append(
                    Sulfuras(item.name, item.sell_in, item.quality))
            elif "Backstage Passes To" in item.name:
                self.parsed_items.append(BackstagePass(
                    item.name, item.sell_in, item.quality))
            elif "Conjured" in item.name:
                self.parsed_items.append(ConjuredItem(
                    item.name, item.sell_in, item.quality))
            else:
                self.parsed_items.append(RegularItem(
                    item.name, item.sell_in, item.quality))

    def update_quality(self):
        max_quality = 50
        min_quality = 0
        for item in self.parsed_items:

            # Establish deltas
            delta_quality = item.update_quality_conditions()['delta_quality']
            delta_sell_in = item.update_quality_conditions()['delta_sell_in']

            item.sell_in += delta_sell_in

            if item.quality >= 0:
                if item.sell_in < 0:
                    item.quality += delta_quality * 2
                else:
                    item.quality += delta_quality

            item.quality = max(min_quality, item.quality)
            item.quality = min(max_quality, item.quality)

    def update_quality_n_times(self, num):
        for _ in range(num):
            self.update_quality()


# Base Item class left untouched
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class RegularItem(Item):
    def update_quality_conditions(self) -> list:
        return {"delta_quality": -1, "delta_sell_in": -1}


class AgedBrie(Item):
    def update_quality_conditions(self) -> list:
        return {"delta_quality": 1, "delta_sell_in": -1}


class Sulfuras(Item):
    def update_quality_conditions(self) -> list:
        return {"delta_quality": 0, "delta_sell_in": 0}


class BackstagePass(Item):
    def update_quality_conditions(self) -> list:
        if self.sell_in > 10:
            delta_quality = 1
        elif 5 < self.sell_in <= 10:
            delta_quality = 2
        elif 0 < self.sell_in <= 5:
            delta_quality = 3
        elif self.sell_in <= 0:
            self.quality = 0
            delta_quality = 0

        return {"delta_quality": delta_quality, "delta_sell_in": -1}


class ConjuredItem(Item):
    def update_quality_conditions(self) -> list:
        return {"delta_quality": -2, "delta_sell_in": -1}