import unittest

from collections import defaultdict

from consistentor.rendezvous import rendezvous_hash


class TestRendezvous(unittest.TestCase):
    def setUp(self):
        self.items = ["pizza", "burger", "pasta", "chili" ]

    def test_consistency(self):
        self.assertEqual("chili", rendezvous_hash("1", self.items))
        self.assertEqual("chili", rendezvous_hash("1", self.items))
        self.assertEqual("burger", rendezvous_hash("abc", self.items))
        self.assertEqual("pasta", rendezvous_hash("test12", self.items))

    def test_uniformity(self):
        keys = defaultdict(int)
        for i in range(int(1000)):
            selected = rendezvous_hash(str(i), self.items)
            keys[selected] += 1
        for key in keys:
            self.assertGreater(keys[key], 200)
