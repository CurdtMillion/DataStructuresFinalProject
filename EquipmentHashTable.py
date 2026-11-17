class EquipmentHashTable:
    """Stores equipment by an ID using chaining for collisions."""
    def __init__(self, size=10):
        self.table = []

        for i in range(size):
            self.table.append([])

    def hash_key(self, equipment_id):
        """Calculates bucket index for equipment ID."""
        return equipment_id % len(self.table)

    def insert(self, equipment):
        """Adds equipment. Return false if ID exists."""
        index = self.hash_key(equipment.equipment_id)
        bucket = self.table[index]

        for existing_equipment in bucket:
            if existing_equipment.equipment_id == equipment.equipment_id:
                return False

        bucket.append(equipment)
        return True

    def lookup(self, equipment_id):
        """Returns matching equipment. Return None if ID not found."""
        index = self.hash_key(equipment_id)
        bucket = self.table[index]

        for equipment in bucket:
            if equipment.equipment_id == equipment_id:
                return equipment

        return None