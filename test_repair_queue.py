import unittest

from RepairRequest import RepairRequest
from RepairQueue import RepairQueue


class TestRepairQueue(unittest.TestCase):
    """Tests repair request order and empty queue behavior."""

    def setUp(self):
        """Creates a fresh queue before each test."""
        self.queue = RepairQueue()

    def test_enqueue_and_dequeue(self):
        """Tests for proper enqueue and dequeue."""
        request = RepairRequest(101, "Belt slips")

        self.queue.enqueue(request)

        self.assertIs(self.queue.dequeue(), request)

    def test_fifo_order(self):
        """Checks for proper first in first out order."""
        first = RepairRequest(101, "Belt slips")
        second = RepairRequest(111, "Seat is loose")

        self.queue.enqueue(first)
        self.queue.enqueue(second)

        self.assertIs(self.queue.dequeue(), first)
        self.assertIs(self.queue.dequeue(), second)
        self.assertIsNone(self.queue.dequeue())

    def test_empty_queue(self):
        """Check for empty queue."""
        self.assertIsNone(self.queue.dequeue())

    def test_reuse_after_emptying(self):
        "Checks to make sure queue works after request removed."
        first = RepairRequest(101, "Belt slips")
        second = RepairRequest(111, "Seat is loose")

        self.queue.enqueue(first)
        self.queue.dequeue()

        self.queue.enqueue(second)

        self.assertIs(self.queue.dequeue(), second)
        self.assertIsNone(self.queue.dequeue())


if __name__ == "__main__":
    unittest.main()