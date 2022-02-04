from dataclasses import dataclass, field
from typing import List

# Base Item class instantiation left untouched
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        # Edited below to use f string and brackets when outputting; functionality unchanged
        return f"({self.name}, {self.sell_in}, {self.quality})"


@dataclass
class GildedRose:
    items: List[Item] = field(default_factory=list)
    _parsed_items: List = field(default_factory=list, init=False)

    def __post_init__(self):
        special_items = {"Aged Brie": AgedBrie, "Sulfuras - Hand Of Ragnaros": Sulfuras,
                         "Backstage Passes To": BackstagePass, "Conjured": ConjuredItem}

        for item in self.items:
            item.name = item.name.title()
            args = [item.name, item.sell_in, item.quality]

            special = False
            for k, class_name in special_items.items():
                if item.name == k or k in item.name:
                    self._parsed_items.append(class_name(*args))
                    special = True

            if not special:
                self._parsed_items.append(RegularItem(*args))

    def update_quality(self):
        max_quality = 50
        min_quality = 0

        for item in self._parsed_items:
            delta_quality = item.update_quality_conditions()['delta_quality']
            delta_sell_in = item.update_quality_conditions()['delta_sell_in']

            item.sell_in += delta_sell_in

            if item.sell_in < 0:
                item.quality += delta_quality * 2
            else:
                item.quality += delta_quality

            item.quality = max(min_quality, item.quality)
            item.quality = min(max_quality, item.quality)

    def update_quality_n_times(self, num):
        for _ in range(num):
            self.update_quality()

    def __repr__(self):
        return f"{self._parsed_items}"


# Generic, non-special item
class RegularItem(Item):
    def update_quality_conditions(self) -> dict:
        return {"delta_quality": -1, "delta_sell_in": -1}


class AgedBrie(Item):
    def update_quality_conditions(self) -> dict:
        return {"delta_quality": 1, "delta_sell_in": -1}


class Sulfuras(Item):
    def update_quality_conditions(self) -> dict:
        return {"delta_quality": 0, "delta_sell_in": 0}


class BackstagePass(Item):
    def update_quality_conditions(self) -> dict:
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
    def update_quality_conditions(self) -> dict:
        return {"delta_quality": -2, "delta_sell_in": -1}
