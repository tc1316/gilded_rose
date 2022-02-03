# Gilded Rose Tech Test (Python)
Second practice exercise of a tech test with the aim of demonstrating OOD and TDD


## Requirements
- Python 3.8+ (https://www.python.org/downloads/)
- Pip 22.0.2+ (https://pip.pypa.io/en/stable/installation/)
- Coverage.py (https://coverage.readthedocs.io/en/6.3/)
- Modules (part of Python Standard Library): unittest, dataclasses, typing


# Approach
- Crux of refactor involves using the Item class as a base class. Each Item is parsed and either returns a RegularItem or one of many special item subclasses that inherit from the Item base class
  - Each Item subclass has an update_quality_conditions method that returns a dict with the keys corresponding to the appropriate change in quality and sell_in (if any)
- Used a dataclass for easier init and post_init control for GildedRose class
  - *May switch to attrs library*
- Created an instance variable called parsed_items that is created post_init of the GildedRose class. This iterates through the items list and appends respective subclasses of Item to it
  - Called .title() to normalize item names to bypass exact string matching
  - Space complexity could be decreased by overriding initial items array instead
- Update_quality method now simply fetches and executes the quality and sell_in for each item
  - Min/max functions serve as the check to ensure vals are within quality restrictions

**POST-REVIEW CHANGES**
- TBA

## Running tests (from root)
- Run "coverage run -m test_gilded_rose.py"
- To check coverage: "coverage report"


## Running code (from root)
- Run "python main.py"
- You should see:
```
name | sell_in | quality
[(Aged Brie, 3, 11), (Sulfuras - Hand Of Ragnaros, 12345, 50), (Backstage Passes To A Random Concert, 14, 1), (Foo, 14, 9), (Conjured Foo, 14, 8)]
[(Aged Brie, 2, 12), (Sulfuras - Hand Of Ragnaros, 12345, 50), (Backstage Passes To A Random Concert, 13, 2), (Foo, 13, 8), (Conjured Foo, 13, 6)]
[(Aged Brie, 1, 13), (Sulfuras - Hand Of Ragnaros, 12345, 50), (Backstage Passes To A Random Concert, 12, 3), (Foo, 12, 7), (Conjured Foo, 12, 4)]
[(Aged Brie, 0, 14), (Sulfuras - Hand Of Ragnaros, 12345, 50), (Backstage Passes To A Random Concert, 11, 4), (Foo, 11, 6), (Conjured Foo, 11, 2)]
[(Aged Brie, -1, 16), (Sulfuras - Hand Of Ragnaros, 12345, 50), (Backstage Passes To A Random Concert, 10, 5), (Foo, 10, 5), (Conjured Foo, 10, 
0)]
[(Aged Brie, -2, 18), (Sulfuras - Hand Of Ragnaros, 12345, 50), (Backstage Passes To A Random Concert, 9, 7), (Foo, 9, 4), (Conjured Foo, 9, 0)]
[(Aged Brie, -3, 20), (Sulfuras - Hand Of Ragnaros, 12345, 50), (Backstage Passes To A Random Concert, 8, 9), (Foo, 8, 3), (Conjured Foo, 8, 0)]
[(Aged Brie, -4, 22), (Sulfuras - Hand Of Ragnaros, 12345, 50), (Backstage Passes To A Random Concert, 7, 11), (Foo, 7, 2), (Conjured Foo, 7, 0)]
[(Aged Brie, -5, 24), (Sulfuras - Hand Of Ragnaros, 12345, 50), (Backstage Passes To A Random Concert, 6, 13), (Foo, 6, 1), (Conjured Foo, 6, 0)]
[(Aged Brie, -6, 26), (Sulfuras - Hand Of Ragnaros, 12345, 50), (Backstage Passes To A Random Concert, 5, 15), (Foo, 5, 0), (Conjured Foo, 5, 0)]
[(Aged Brie, -7, 28), (Sulfuras - Hand Of Ragnaros, 12345, 50), (Backstage Passes To A Random Concert, 4, 18), (Foo, 4, 0), (Conjured Foo, 4, 0)]
[(Aged Brie, -8, 30), (Sulfuras - Hand Of Ragnaros, 12345, 50), (Backstage Passes To A Random Concert, 3, 21), (Foo, 3, 0), (Conjured Foo, 3, 0)]
[(Aged Brie, -9, 32), (Sulfuras - Hand Of Ragnaros, 12345, 50), (Backstage Passes To A Random Concert, 2, 24), (Foo, 2, 0), (Conjured Foo, 2, 0)]
[(Aged Brie, -10, 34), (Sulfuras - Hand Of Ragnaros, 12345, 50), (Backstage Passes To A Random Concert, 1, 27), (Foo, 1, 0), (Conjured Foo, 1, 0)]
[(Aged Brie, -11, 36), (Sulfuras - Hand Of Ragnaros, 12345, 50), (Backstage Passes To A Random Concert, 0, 30), (Foo, 0, 0), (Conjured Foo, 0, 0)]
[(Aged Brie, -12, 38), (Sulfuras - Hand Of Ragnaros, 12345, 50), (Backstage Passes To A Random Concert, -1, 0), (Foo, -1, 0), (Conjured Foo, -1, 0)]
```

