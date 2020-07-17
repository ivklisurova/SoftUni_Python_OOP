class Hero:
    def __init__(self, username, level):
        self.username = username
        self.level = level

    def __repr__(self):
        return f'{self.username} of type {type(self).__name__} has level {self.level}'


class Knight(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)


class DarkKnight(Knight):
    def __init__(self, username, level):
        super().__init__(username, level)