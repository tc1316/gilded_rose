# -*- coding: utf-8 -*-
import unittest
from gilded_rose import GildedRose
from unittest.mock import Mock


class GildedRoseTest(unittest.TestCase):
    def setUp(self):
        apple, aged_brie, sulfuras, backstage_pass, conjured_apple = Mock(), Mock(), Mock(), Mock(), Mock()

        apple.configure_mock(name="Apple", sell_in=5, quality=10)
        aged_brie.configure_mock(name="aged brie", sell_in=5, quality=0)
        sulfuras.configure_mock(
            name="sulfuras - hand of ragnaros", sell_in=-500, quality=50)
        backstage_pass.configure_mock(
            name="backstage passes to a smash mouth concert", sell_in=15, quality=0)
        conjured_apple.configure_mock(
            name="conjured apple", sell_in=5, quality=50)

        self.items = [apple, aged_brie, sulfuras,
                      backstage_pass, conjured_apple]
        self.gilded_rose = GildedRose(self.items)

    def test_quality_degradation_base_case(self):
        self.gilded_rose.update_quality_n_times(5)
        self.assertEqual(self.gilded_rose._parsed_items[0].sell_in, 0)
        self.assertEqual(self.gilded_rose._parsed_items[0].quality, 5)

    def test_quality_degradation_doubles_past_sell_date(self):
        self.gilded_rose.update_quality_n_times(6)
        self.assertEqual(self.gilded_rose._parsed_items[0].sell_in, -1)
        self.assertEqual(self.gilded_rose._parsed_items[0].quality, 3)

    def test_quality_degradation_is_never_negative(self):
        self.gilded_rose.update_quality_n_times(1000)
        self.assertEqual(self.gilded_rose._parsed_items[0].sell_in, -995)
        self.assertEqual(self.gilded_rose._parsed_items[0].quality, 0)

    def test_quality_increases_for_aged_brie(self):
        self.gilded_rose.update_quality_n_times(5)
        self.assertEqual(self.gilded_rose._parsed_items[1].sell_in, 0)
        self.assertEqual(self.gilded_rose._parsed_items[1].quality, 5)

        self.gilded_rose.update_quality_n_times(5)
        self.assertEqual(self.gilded_rose._parsed_items[1].sell_in, -5)
        self.assertEqual(self.gilded_rose._parsed_items[1].quality, 15)

    def test_quality_cannot_be_increased_above_50(self):
        self.gilded_rose.update_quality_n_times(1000)
        self.assertEqual(self.gilded_rose._parsed_items[1].quality, 50)

    def test_sulfuras_conditions(self):
        self.gilded_rose.update_quality_n_times(1000)
        self.assertEqual(self.gilded_rose._parsed_items[2].sell_in, -500)
        self.assertEqual(self.gilded_rose._parsed_items[2].quality, 50)

    def test_backstage_passes_conditions(self):
        # 15 to 10 -> quality +1 per day
        self.gilded_rose.update_quality_n_times(5)
        self.assertEqual(self.gilded_rose._parsed_items[3].sell_in, 10)
        self.assertEqual(self.gilded_rose._parsed_items[3].quality, 5)

        # 10 to 5 -> quality +2 per day
        self.gilded_rose.update_quality_n_times(5)
        self.assertEqual(self.gilded_rose._parsed_items[3].sell_in, 5)
        self.assertEqual(self.gilded_rose._parsed_items[3].quality, 15)

        # 5 to 0 -> quality +3 per day
        self.gilded_rose.update_quality_n_times(5)
        self.assertEqual(self.gilded_rose._parsed_items[3].sell_in, 0)
        self.assertEqual(self.gilded_rose._parsed_items[3].quality, 30)

        # Quality drops to 0 post-concert
        self.gilded_rose.update_quality_n_times(1)
        self.assertEqual(self.gilded_rose._parsed_items[3].sell_in, -1)
        self.assertEqual(self.gilded_rose._parsed_items[3].quality, 0)

    def test_conjured_items(self):
        self.gilded_rose.update_quality_n_times(5)
        self.assertEqual(self.gilded_rose._parsed_items[4].sell_in, 0)
        self.assertEqual(self.gilded_rose._parsed_items[4].quality, 40)

        # Quality degradation past expiry should be 4 per day for conjured items
        self.gilded_rose.update_quality_n_times(5)
        self.assertEqual(self.gilded_rose._parsed_items[4].sell_in, -5)
        self.assertEqual(self.gilded_rose._parsed_items[4].quality, 20)


if __name__ == '__main__':
    unittest.main()
