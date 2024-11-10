from player import Player


class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nation):
        players = [pl for pl in self.players if pl.nation == nation]
        return sorted(players, reverse=True, key=Player.sortByPoints)
