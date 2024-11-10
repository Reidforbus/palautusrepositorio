class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nation = dict['nationality']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.games = dict['games']
        self.id = dict['id']

    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} {self.team} {self.goals:3} + {self.assists:3} = {self.points}"

    def get_table_data(self):
        return self.name, self.team, self.goals, self.assists, self.points

    def sortByPoints(player):
        return player.points
