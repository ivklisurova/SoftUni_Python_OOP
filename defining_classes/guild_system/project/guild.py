class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player in self.players:
            return f'Player {player.name} is already in the guild.'
        if player.guild != 'Unaffiliated':
            return f'Player {player.name} is in another guild.'
        self.players.append(player)
        player.guild = self.name
        return f'Welcome player {player.name} to the guild {self.name}'

    def kick_player(self, player_name: str):
        if player_name not in [p.name for p in self.players]:
            return f'Player {player_name} is not in the guild.'
        p = [p for p in self.players if p.name == player_name][0]
        self.players.remove(p)
        p.guild = 'Unaffiliated'
        return f'Player {player_name} has been removed from the guild.'

    def guild_info(self):
        result = f'Guild: {self.name}\n'
        for x in self.players:
            result += x.player_info()
        return result

