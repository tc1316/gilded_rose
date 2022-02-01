# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def setUp(self) -> None:
        foo_item = Item("foo", 5, 10)
        aged_brie = Item("Aged Brie", 5, 0)
        sulfuras = Item("Sulfuras, Hand of Ragnaros", -500, 80)
        bsp = Item("Backstage passes to a TAFKAL80ETC concert", 15, 0)

        self.items = [foo_item, aged_brie, sulfuras, bsp]
        self.gilded_rose = GildedRose(self.items)

    def test_quality_degradation_base_case(self):
        self.gilded_rose.update_quality_n_times(5)
        self.assertEqual(self.gilded_rose.items[0].sell_in, 0)
        self.assertEqual(self.gilded_rose.items[0].quality, 5)

    def test_quality_degradation_doubles_past_sell_date(self):
        self.gilded_rose.update_quality_n_times(6)
        self.assertEqual(self.gilded_rose.items[0].sell_in, -1)
        self.assertEqual(self.gilded_rose.items[0].quality, 3)

    def test_quality_degradation_is_never_negative(self):
        self.gilded_rose.update_quality_n_times(1000)
        self.assertEqual(self.gilded_rose.items[0].quality, 0)

    def test_quality_increases_for_aged_brie(self):
        self.gilded_rose.update_quality_n_times(5)
        self.assertEqual(self.gilded_rose.items[1].sell_in, 0)
        self.assertEqual(self.gilded_rose.items[1].quality, 5)

        self.gilded_rose.update_quality_n_times(5)
        self.assertEqual(self.gilded_rose.items[1].sell_in, -5)
        self.assertEqual(self.gilded_rose.items[1].quality, 15)

    def test_quality_cannot_be_increased_above_50(self):
        self.gilded_rose.update_quality_n_times(1000)
        self.assertEqual(self.gilded_rose.items[1].quality, 50)

    def test_sulfuras_conditions(self):
        self.gilded_rose.update_quality_n_times(1000)
        self.assertEqual(self.gilded_rose.items[2].sell_in, -500)
        self.assertEqual(self.gilded_rose.items[2].quality, 80)

    def test_backstage_passes_conditions(self):
        # 15 to 10 -> quality +1 per day
        self.gilded_rose.update_quality_n_times(5)
        self.assertEqual(self.gilded_rose.items[3].sell_in, 10)
        self.assertEqual(self.gilded_rose.items[3].quality, 5)

        # 10 to 5 -> quality +2 per day
        self.gilded_rose.update_quality_n_times(5)
        self.assertEqual(self.gilded_rose.items[3].sell_in, 5)
        self.assertEqual(self.gilded_rose.items[3].quality, 15)

        # 5 to 0 -> quality +3 per day
        self.gilded_rose.update_quality_n_times(5)
        self.assertEqual(self.gilded_rose.items[3].sell_in, 0)
        self.assertEqual(self.gilded_rose.items[3].quality, 30)

        # Quality drops to 0 post-concert
        self.gilded_rose.update_quality_n_times(1)
        self.assertEqual(self.gilded_rose.items[3].sell_in, -1)
        self.assertEqual(self.gilded_rose.items[3].quality, 0)


if __name__ == '__main__':
    unittest.main()
