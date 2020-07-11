class Equipment:
    autoincremented_id = 1

    def __init__(self, name):
        self.name = name
        self.id = Equipment.autoincremented_id
        Equipment.autoincremented_id += 1

    @staticmethod
    def get_next_id():
        return Equipment.autoincremented_id

    def __repr__(self):
        return f'Equipment <{self.id}> {self.name}'
