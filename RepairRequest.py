class RepairRequest:
    """Stores the equipment ID and issue in a repair request."""
    def __init__(self, equipment_id, description):
        self.equipment_id = equipment_id
        self.description = description