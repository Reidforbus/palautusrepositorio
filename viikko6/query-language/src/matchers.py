class All:
    def __init__(self):
        pass

    def test(self, player):
        return True


class QueryBuilder():
    def __init__(self, matcher=All()):
        self._matcher = matcher

    def build(self):
        return self._matcher

    def plays_in(self, team):
        return QueryBuilder(And(PlaysIn(team), self._matcher))

    def has_at_least(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value, attr), self._matcher))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value, attr), self._matcher))

    def one_of(self, q1, q2):
        return QueryBuilder(Or(q1, q2))


class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value


class Not:
    def __init__(self, tester):
        self.tester = tester

    def test(self, player):
        return not self.tester.test(player)


class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)
        return player_value < self._value


class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True
        return False
