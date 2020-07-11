class Trainer:
    autoincremented_id = 1

    def __init__(self, name):
        self.name = name
        self.id = Trainer.autoincremented_id
        Trainer.autoincremented_id += 1

    @staticmethod
    def get_next_id():
        return Trainer.autoincremented_id

    def __repr__(self):
        return f'Trainer <{self.id}> {self.name}'
