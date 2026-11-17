class EquipmentHashTable:
    def __init__(self, size=10):
        self.table = []

        for i in range(size):
            self.table.append([])

    def hash_key(self, equipment_id):
        return equipment_id % len(self.table)

    def insert(self, equipment):
        index = self.hash_key(equipment.equipment_id)
        bucket = self.table[index]

        for existing_equipment in bucket:
            if existing_equipment.equipment_id == equipment.equipment_id:
                return False

        bucket.append(equipment)
        return True

    def lookup(self, equipment_id):
        index = self.hash_key(equipment_id)
        bucket = self.table[index]

        for equipment in bucket:
            if equipment.equipment_id == equipment_id:
                return equipment

        return None