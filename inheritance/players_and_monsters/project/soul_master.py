class Hero:
    def __init__(self, username, level):
        self.username = username
        self.level = level

    def __repr__(self):
        return f'{self.username} of type {type(self).__name__} has level {self.level}'


class Wizard(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)


class DarkWizard(Wizard):
    def __init__(self, username, level):
        super().__init__(username, level)


class SoulMaster(DarkWizard):
    def __init__(self, username, level):
        super().__init__(username, level)