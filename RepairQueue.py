class RepairQueue:
    """Stores requests in FIFO."""
    def __init__(self):
        self.requests = []

    def enqueue(self, repair_request):
        """Add repair request to end of queue."""
        self.requests.append(repair_request)

    def dequeue(self):
        """Remove oldest request. Return None if empty."""
        if len(self.requests) == 0:
            return None

        return self.requests.pop(0)