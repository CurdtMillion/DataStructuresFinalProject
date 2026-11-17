import unittest

from Equipment import Equipment
from EquipmentHashTable import EquipmentHashTable


class TestEquipmentHashTable(unittest.TestCase):
    """Tests equipment insertion, collisions, and lookup."""

    def setUp(self):
        """Creates a fresh table before each test."""
        self.table = EquipmentHashTable()

    def test_insert_and_lookup(self):
        """Verify insertion."""
        equipment = Equipment(101, "Treadmill", "Cardio area")

        self.assertTrue(self.table.insert(equipment))
        self.assertIs(self.table.lookup(101), equipment)

    def test_duplicate_id(self):
        """Check for dup IDs."""
        original = Equipment(101, "Treadmill", "Cardio area")
        duplicate = Equipment(101, "Bike", "Cardio area")

        self.table.insert(original)

        self.assertFalse(self.table.insert(duplicate))
        self.assertIs(self.table.lookup(101), original)

    def test_collision(self):
        """Check for collisions in bucket."""
        # Both IDs will hash to bucket 1.
        first = Equipment(101, "Treadmill", "Cardio area")
        second = Equipment(111, "Leg press", "Weight room")

        self.assertTrue(self.table.insert(first))
        self.assertTrue(self.table.insert(second))

        self.assertIs(self.table.lookup(101), first)
        self.assertIs(self.table.lookup(111), second)

    def test_missing_id(self):
        """Check for a missing ID."""
        self.table.insert(Equipment(101, "Treadmill", "Cardio area"))
        self.assertIsNone(self.table.lookup(121))


if __name__ == "__main__":
    unittest.main()